import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Currency} from "../interfaces/currency";
import {CurrencyRateService} from "../currency-rate.service";
import {Observable} from "rxjs";
import {DataToSend} from "../interfaces/data-to-send";
import {HttpClient} from "@angular/common/http";


@Component({
  selector: 'app-currency-exchange-rate',
  templateUrl: './currency-exchange-rate.component.html',
  styleUrls: ['./currency-exchange-rate.component.css']
})
export class CurrencyExchangeRateComponent implements OnInit{
    formValidator : FormGroup;
    availableCurrencies$: Observable<any>;
    parsedData: any;
    constructor(private fb: FormBuilder,
                private service: CurrencyRateService,
                private http: HttpClient) {
    }

    ngOnInit(): void{
      this.formValidator = this.fb.group({
        currency: ['', [Validators.required]],
        currency2: ['', [Validators.required]]
      })
      this.availableCurrencies$ = this.service.fetchCurrencies()
    }


    sendData(){


    }
}
