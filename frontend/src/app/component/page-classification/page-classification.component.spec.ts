import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageClassificationComponent } from './page-classification.component';

describe('PageClassificationComponent', () => {
  let component: PageClassificationComponent;
  let fixture: ComponentFixture<PageClassificationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageClassificationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageClassificationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
