import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  index: any;
  pagesDefined= {Home: 'home', CurrencyExchangeRate: 'exchange_rate', unknown: ''}

  isActive(index){
    this.index = index
  }
}
