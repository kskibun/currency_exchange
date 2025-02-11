import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map, pipe, tap} from "rxjs";
import {Currency} from "./interfaces/currency";

@Injectable({
  providedIn: 'root'
})
export class CurrencyRateService {

  backendUrl: string = "http://127.0.0.1:8000/"
  constructor(private http: HttpClient) { }

  fetchCurrencies(){
    return this.http.get<any[]>('/api/currency/').pipe(map
    (res=>res.map(item=>item.currency_code)))
  }
}
