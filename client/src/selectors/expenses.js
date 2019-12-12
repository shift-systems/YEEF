import moment from 'moment';

// Get visible savings

export default (savings, { text, sortBy, startDate, endDate }) => {
  return savings
    .filter(saving => {
      const savedOnMoment = moment(saving.saveOn);
      const startDateMatch = startDate
        ? startDate.isSameOrBefore(savedOnMoment, 'day')
        : true;
      const endDateMatch = endDate
        ? endDate.isSameOrAfter(savedOnMoment, 'day')
        : true;
      const textMatch = saving.saver.email
        .toLowerCase()
        .includes(text.toLowerCase());

      return startDateMatch && endDateMatch && textMatch;
    })
    .sort((a, b) => {
      if (sortBy === 'date') {
        return a.saveOn < b.saveOn ? 1 : -1;
      } else if (sortBy === 'amount') {
        return a.amount < b.amount ? 1 : -1;
      }
    });
};
