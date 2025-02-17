import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map} from "rxjs";
import {Currency} from "./interfaces/currency";
import {environment} from "../environments/environment.development";

@Injectable({
  providedIn: 'root'
})
export class CurrencyRateService {

  constructor(private http: HttpClient) { }

  fetchCurrencies(){
    return this.http.get<Currency[]>(`${environment.apiUrl}/currency/`).pipe(map
    (res=>res.map(item=>item.currency_code)))
  }
}
