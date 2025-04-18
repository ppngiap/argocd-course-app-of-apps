

def app_str(namespace: str, appname: str, wave: int):
    appstr = f"""
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata: 
  name: {appname}
  namespace: argocd
  annotations:
    argocd.argoproj.io/sync-wave: "{wave}"
spec: 
  destination: 
    namespace: {namespace} 
    server: "https://kubernetes.default.svc"
  project: dcp
  source: 
    path: guestbook
    repoURL: "https://github.com/ppngiap/argocd-example-apps.git"
    targetRevision: master
  syncPolicy:
  automated:
    prune: true
    selfHeal: true
    syncOptions:
      - CreateNamespace=true
"""
    return appstr

def gen_app(waves: int, instances: int):
    for wave in range(0, waves):
        for instance in range(0, instances):
            appname = f"app{wave}-{instance:02}"
            namespace = appname
            filename = f"directory-of-apps/{appname}.yaml"
            with open(filename, "w") as f:
                f.write(app_str(namespace, appname, wave))


gen_app(3,3)