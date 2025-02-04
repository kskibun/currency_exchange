import {Component, Input, OnInit} from '@angular/core';
import {FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-currency-input',
  templateUrl: './currency-input.component.html',
  styleUrls: ['./currency-input.component.css']
})
export class CurrencyInputComponent implements OnInit{
  @Input() formGrp: any;
  @Input() label: string;
  @Input() currencies: any;
  @Input() selectedCtrl: any;

  ngOnInit(): void {
    console.log(this.currencies)
  }
}
