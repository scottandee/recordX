$(function () {
  const open = $('[data-open-modal]');
  const close = $('[data-close-modal]');
  const modal = $('[data-modal]');

  open.on('click', () => {
    modal[0].showModal();
  });
  close.on('click', () => {
    modal[0].close();
  });
});
