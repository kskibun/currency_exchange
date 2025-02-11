import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {DataToSend} from "../interfaces/data-to-send";

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
  @Output() currenciesToSentEvent = new EventEmitter();
  selectedData: any;

  ngOnInit(): void {
  }


  xxx(chosenCurrency: DataToSend){
    this.selectedData = chosenCurrency
    this.currenciesToSentEvent.emit([this.selectedData, this.label])
  }
}
