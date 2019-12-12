import React, { Component } from 'react';
import moment from 'moment';
import { SingleDatePicker } from 'react-dates';

export const SavingsForm = ({
  handleSubmit,
  onCommentChange,
  onAmountChange,
  onDateChange,
  onFocusChange,
  state
}) => (
  <form className="form" onSubmit={handleSubmit}>
    {state.error && <p className="form__error">{state.error}</p>}

    <div className="form-saving">
      <SingleDatePicker
        date={state.savedOn}
        onDateChange={onDateChange}
        focused={state.calendarFocused}
        onFocusChange={onFocusChange}
        numberOfMonths={1}
        isOutsideRange={() => false}
      />
      <select className="form-saving__select">
        <option value="EURO">EURO</option>
        <option value="UGSH">UGSH</option>
      </select>
    </div>
    <input
      type="text"
      placeholder="Amount"
      className="text-input"
      value={state.amount}
      onChange={onAmountChange}
    />
    <textarea
      placeholder="Add a comment for this saving (optional)"
      className="textarea"
      value={state.comment}
      onChange={onCommentChange}
    ></textarea>

    <button className="button">Continue</button>
  </form>
);

export default SavingsForm;
