class ObjectUtilities {
  /* Your magic here */
  static mergeObjects(...args) {
    //const newObj = { ...A, ...B };
    return args.reduce((p, c) => {
      return { ...p, ...c };
    });
  }
  static removePassword(A) {
    const B = { ...A };
    delete B.password;
    return B;
  }
  static freezeObj(A) {
    return Object.freeze(A);
  }
  static getOnlyValues(A) {
    return Object.values(A);
  }
  static getOnlyProperties(A) {
    return Object.keys(A);
  }
}
const objA = {
  name: "Nicolas",
  favFood: "Kimchi",
};
const objB = {
  password: "12345",
};
const user = ObjectUtilities.mergeObjects(objA, objB);
console.log(user);
const cleanUser = ObjectUtilities.removePassword(user);
console.log(cleanUser);
const frozenUser = ObjectUtilities.freezeObj(cleanUser);
const onlyValues = ObjectUtilities.getOnlyValues(frozenUser);
console.log(onlyValues);
const onlyProperties = ObjectUtilities.getOnlyProperties(frozenUser);
console.log(onlyProperties);
frozenUser.name = "Hello!"; // This should show an error
