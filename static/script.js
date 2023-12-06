// h1タグを取得
const h1Tag = document.querySelector('h1');

// h1タグがクリックされたときのイベントリスナーを追加
h1Tag.addEventListener('click', function() {
  // テキストの色を赤に変更
  h1Tag.style.color = 'red';
});
