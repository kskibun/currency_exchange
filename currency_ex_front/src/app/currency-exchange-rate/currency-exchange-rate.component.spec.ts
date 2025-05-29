import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrencyExchangeRateComponent } from './currency-exchange-rate.component';

describe('CurrencyExchangeRateComponent', () => {
  let component: CurrencyExchangeRateComponent;
  let fixture: ComponentFixture<CurrencyExchangeRateComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CurrencyExchangeRateComponent]
    });
    fixture = TestBed.createComponent(CurrencyExchangeRateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
