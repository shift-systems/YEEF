// Expenses Reducer

const savings = [];
const error = '';

export const getExpenseSuccess = (state = savings, action) => {
  switch (action.type) {
    case 'GET_SAVINGS_SUCCESS':
      return [...state, action.expense];
    default:
      return state;
  }
};

export const getExpenseFail = (state = error, action) => {
  switch (action.type) {
    case 'GET_SAVINGS_FAIL':
      return [...state, action.expense];
    default:
      return state;
  }
};
