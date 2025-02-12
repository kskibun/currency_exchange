import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map, pipe, tap} from "rxjs";
import {Currency} from "./interfaces/currency";

@Injectable({
  providedIn: 'root'
})
export class CurrencyRateService {

  constructor(private http: HttpClient) { }

  fetchCurrencies(){
    return this.http.get<Currency[]>('/api/currency/').pipe(map
    (res=>res.map(item=>item.currencyCode)))
  }
}
