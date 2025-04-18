

def app_str(wave: int, instance: int):
    appstr = f"""
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata: 
  name: app{wave}-{instance:02}
  namespace: argocd
  annotations:
    argocd.argoproj.io/sync-wave: "{wave}"
spec: 
  destination: 
    namespace: dcp
    server: "https://kubernetes.default.svc"
  project: default
  source: 
    path: guestbook
    repoURL: "https://github.com/ppngiap/argocd-example-apps.git"
    targetRevision: master
  syncPolicy:
    syncOptions:
      - CreateNamespace=true
"""
    return appstr

def gen_app(waves: int, instances: int):
    for wave in range(0, waves):
        for instance in range(0, instances):
            filename = f"directory-of-apps/app{wave}-{instance:02}.yaml"
            with open(filename, "w") as f:
                f.write(app_str(wave, instance))


gen_app(3,3)