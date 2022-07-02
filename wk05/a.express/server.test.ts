import request, { HttpVerb } from 'sync-request';

import { SERVER_URL } from './config';

function requestHelper(method: HttpVerb, path: string, payload: object) {
  let qs = {};
  let json = {};
  if (['GET', 'DELETE'].includes(method)) {
    qs = payload;
  } else {
    // PUT/POST
    json = payload;
  }
  const res = request(method, SERVER_URL + path, { qs, json });
  return JSON.parse(res.getBody('utf-8'));
}

// ========================================================================= //

// Wrapper functions

function requestAddNameAge(name: string, age: number) {
  return requestHelper('POST', '/addnameage', { name, age });
}

function requestGetNamesAges(minAge?: number) {
  return requestHelper('GET', '/getnamesages', { minAge });
}

function requestEditNameAge(name: string, age: number) {
  return requestHelper('PUT', '/editnameage', { name, age });
}

function requestRemoveNameAge(name: string) {
  return requestHelper('DELETE', '/removenameage', { name });
}

function requestGetStats() {
  return requestHelper('GET', '/getstats', {});
}

function requestClear() {
  return requestHelper('DELETE', '/clear', {});
}

// ========================================================================= //

const ERROR = { error: 'error' };

beforeEach(() => {
  requestClear();
});

describe('/addnameage', () => {
  describe('error', () => {
    test.each([
      { name: '', age: 20 },
      { name: 'valid', age: 0 },
    ])('name=$name, age=$age', ({ name, age }) => {
      expect(requestAddNameAge(name, age)).toStrictEqual(ERROR);
    });
  });

  test('return value', () => {
    expect(requestAddNameAge('valid', 20)).toStrictEqual({});
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [{ name: 'valid', age: 20 }] });
  });
});

describe('/getnamesages', () => {
  describe('no minAge', () => {
    test('empty', () => {
      expect(requestGetNamesAges()).toStrictEqual({ namesAges: [] });
    });

    test('one item', () => {
      requestAddNameAge('one', 1);
      expect(requestGetNamesAges()).toStrictEqual({ namesAges: [{ name: 'one', age: 1 }] });
    });

    test('multiple items', () => {
      requestAddNameAge('alsothree', 3);
      requestAddNameAge('two', 2);
      requestAddNameAge('one', 1);
      requestAddNameAge('three', 3);
      expect(requestGetNamesAges()).toStrictEqual({
        namesAges:
          [
            { name: 'alsothree', age: 3 },
            { name: 'three', age: 3 },
            { name: 'two', age: 2 },
            { name: 'one', age: 1 },
          ]
      });
    });
  });

  describe('with minAge', () => {
    test('error: minAge negative', () => {
      requestAddNameAge('three', 3);
      expect(requestGetNamesAges(0)).toStrictEqual(ERROR);
    });

    test('minAge means empty', () => {
      requestAddNameAge('three', 3);
      expect(requestGetNamesAges(4)).toStrictEqual({ namesAges: [] });
    });

    test('minAge filter', () => {
      requestAddNameAge('three', 3);
      requestAddNameAge('five', 5);
      expect(requestGetNamesAges(4)).toStrictEqual({ namesAges: [{ name: 'five', age: 5 }] });
    });
  });
});

describe('/editnameage', () => {
  describe('error', () => {
    test('does not exist', () => {
      expect(requestEditNameAge('invalid', 20)).toStrictEqual(ERROR);
    });

    test('negative age', () => {
      requestAddNameAge('valid', 10);
      expect(requestEditNameAge('valid', -20)).toStrictEqual(ERROR);
    });
  });

  test('successful edit', () => {
    requestAddNameAge('valid', 10);
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [{ name: 'valid', age: 10 }] });
    expect(requestEditNameAge('valid', 20)).toStrictEqual({});
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [{ name: 'valid', age: 20 }] });
  });
});

describe('/removenameage', () => {
  describe('error', () => {
    test('does not exist', () => {
      expect(requestRemoveNameAge('invalid')).toStrictEqual(ERROR);
    });

    test('double remove', () => {
      requestAddNameAge('valid', 10);
      expect(requestRemoveNameAge('valid')).toStrictEqual({});
      expect(requestRemoveNameAge('valid')).toStrictEqual(ERROR);
    });
  });

  test('successful remove', () => {
    requestAddNameAge('valid', 10);
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [{ name: 'valid', age: 10 }] });
    requestRemoveNameAge('valid');
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [] });
  });
});

describe('/getstats', () => {
  describe('error', () => {
    test('empty data', () => {
      expect(requestGetStats()).toStrictEqual(ERROR);
    });
  });

  test('single entry', () => {
    requestAddNameAge('valid', 10);
    expect(requestGetStats()).toStrictEqual({
      minAge: 10,
      maxAge: 10,
      averageAge: 10,
    });
  });

  test('multiple entries', () => {
    requestAddNameAge('one', 1);
    requestAddNameAge('five', 5);
    requestAddNameAge('three', 3);
    requestAddNameAge('two', 2);
    requestAddNameAge('four', 4);
    expect(requestGetStats()).toStrictEqual({
      minAge: 1,
      maxAge: 5,
      averageAge: 3,
    });
  });
});

describe('clear', () => {
  test('clear on empty', () => {
    expect(requestClear()).toStrictEqual({});
  });

  test('clear success', () => {
    requestAddNameAge('one', 1);
    expect(requestClear()).toStrictEqual({});
    expect(requestGetNamesAges()).toStrictEqual({ namesAges: [] });
  });
});
