function solution(id) {
  id = String(id)
    .toLowerCase()
    .replace(/[^\w-_\.]/g, "")
    .replace(/\.{2,}/g, ".")
    .replace(/^\.|\.$/g, "")
    .replace(/^$/g, "a")
    .slice(0, 15)
    .replace(/\.$/, "");

  if (id.length <= 2) {
    id = id + id.charAt(id.length - 1).repeat(3 - id.length);
  }
  return id;
}
