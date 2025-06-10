export function formatImageUrl(url) {
  if (!url) return '';
  try {
    const hasProtocol = url.startsWith('http://') || url.startsWith('https://');
    const fullUrl = hasProtocol ? url : 'http://' + url;
    const parsed = new URL(fullUrl);

    if (parsed.port) return parsed.toString();

    parsed.port = '8100';
    return parsed.toString();
  } catch (e) {
    return url;
  }
}
