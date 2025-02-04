import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Observable} from "rxjs";
import {Currency} from "../interfaces/currency";

@Component({
  selector: 'app-currency-exchange-rate',
  templateUrl: './currency-exchange-rate.component.html',
  styleUrls: ['./currency-exchange-rate.component.css']
})
export class CurrencyExchangeRateComponent implements OnInit{
    formValidator : FormGroup;
    // availableCurrencies$: Observable<Currency>;
    testCurrencies: any;
    constructor(private fb: FormBuilder) {
    }

    ngOnInit(): void{
      this.formValidator = this.fb.group({
        currency: ['', [Validators.required]],
        currency2: ['', [Validators.required]]
      })
      this.testCurrencies = {'dupa': 'papa', "[a[a":'japa'}
    }



}
