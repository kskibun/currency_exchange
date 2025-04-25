import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {CalculatedCurrencyAmount, Currency} from "../interfaces/currency";
import {CurrencyRateService} from "../currency-rate.service";
import {Observable} from "rxjs";
import {DataToSend} from "../interfaces/data-to-send";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment.development";
import {getCurrencySymbol} from "@angular/common";


@Component({
  selector: 'app-currency-exchange-rate',
  templateUrl: './currency-exchange-rate.component.html',
  styleUrls: ['./currency-exchange-rate.component.css']
})
export class CurrencyExchangeRateComponent implements OnInit{
    formValidator : FormGroup;
    availableCurrencies$: Observable<any>;
    chosenCurrency1: string;
    chosenCurrency2: string;
    validCurrencies: boolean;
    buttonDisabled: boolean = true;
    amountLabel: string;
    calcOutput: number;
    chosenCurrencyAmount: number;
    constructor(private fb: FormBuilder,
                private service: CurrencyRateService,
                private http: HttpClient) {
    }

    ngOnInit(): void{
      this.formValidator = this.fb.group({
        currency: [null, [Validators.required]],
        currency2: [null, [Validators.required]],
        currency1Amount: [null, [Validators.required, Validators.pattern('^[0-9]*$')]],
        calculatedCurrency: [{value:null, disabled:true}]
      })
      this.availableCurrencies$ = this.service.fetchCurrencies()
      this.formValidator.valueChanges.subscribe(()=> this.checkCurrencyCodeInput())
    }


    sendData(){
      this.http.get<any[]>(`${environment.apiUrl}/currencies/${this.chosenCurrency1}/${this.chosenCurrency2}/${this.chosenCurrencyAmount}` ).subscribe(
        {
          next: (value: Object)=>(Object.values(value).map((s: CalculatedCurrencyAmount)=>
          {if (s.calc_amount) this.formValidator.get('calculatedCurrency').setValue(s.calc_amount)})),
          error: (err)=> alert(err.error)
        }
      )
    }

    checkCurrencyCodeInput(){
      const boolArr = Object.keys(this.formValidator.controls).map(key=>{
        const ctrl = this.formValidator.get(key)
        return ctrl?.valid || ctrl.disabled
      })
      this.buttonDisabled = boolArr.some(val => val ===false)
      }
}
