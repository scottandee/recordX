$(function () {
  const open = $('[data-open-create-modal]');
  const close = $('[data-close-create-modal]');
  const modal = $('[data-create-modal]');

  open.on('click', () => {
    modal[0].showModal();
  });
  close.on('click', () => {
    modal[0].close();
  });
});
$(function () {
  const close = $('[data-close-update-modal]');
  const modal = $('[data-update-modal]');

  close.on('click', () => {
    $('#selected-courses-update').empty();
    modal[0].close();
  });
});
