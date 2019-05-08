import { TestBed } from '@angular/core/testing';

import { MyServiceService } from './myser.service';

describe('MyserviceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MyServiceService = TestBed.get(MyServiceService);
    expect(service).toBeTruthy();
  });
});
