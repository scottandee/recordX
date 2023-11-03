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

$(function () {
  const close = $('[data-confirm-close]');
  const open = $('[data-confirm-open]');
  const modal = $('[data-confirm]');

  open.on('click', () => {
    modal[0].showModal();
  });
  close.on('click', () => {
    modal[0].close();
  });
});
