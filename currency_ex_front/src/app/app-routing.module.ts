import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {CurrencyExchangeRateComponent} from "./currency-exchange-rate/currency-exchange-rate.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'exchange_rate', component: CurrencyExchangeRateComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
