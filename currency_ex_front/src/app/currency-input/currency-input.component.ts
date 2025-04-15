import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {DataToSend} from "../interfaces/data-to-send";
import {FormGroup} from "@angular/forms";

@Component({
  selector: 'app-currency-input',
  templateUrl: './currency-input.component.html',
  styleUrls: ['./currency-input.component.css']
})
export class CurrencyInputComponent implements OnInit{
  @Input() formGrp: FormGroup;
  @Input() label: string;
  @Input() currencies: any;
  @Input() currencyControl: any;
  @Input() currencyAmountControl: any;
  @Output() currenciesToSentEvent = new EventEmitter();
  @Output() validityEvent = new EventEmitter();
  selectedCurrency: any;

  ngOnInit(): void {
  }


  emitChosenCurrency(chosenCurrency: DataToSend){
    this.selectedCurrency = chosenCurrency
    this.currenciesToSentEvent.emit([this.selectedCurrency])
  }

}
