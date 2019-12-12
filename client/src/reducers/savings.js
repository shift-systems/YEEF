const savings = [];
const errors = {};

export const savingSuccess = (state = savings, action) => {
  switch (action.type) {
    case 'SAVE_SUCCESS':
      return [...state, ...action.payload];
    default:
      return state;
  }
};

export const savingFail = (state = errors, action) => {
  switch (action.type) {
    case 'SAVE_FAIL':
      return { errors: action.payload };
    default:
      return state;
  }
};
