# AMQP Directory

## Adding or updating components

The metadata describing the components is stored in yaml files inside
the `data` directory.  To add or update a component, edit one of the
following files:

```
data/apis.yaml
data/servers.yaml
data/services.yaml
data/integrations.yaml
data/tools.yaml
```

For example, the Qpid JMS API component looks like this:

```json
components:
  - name: Apache Qpid JMS
    url: https://qpid.apache.org/components/jms
    docs_url: http://qpid.apache.org/releases/qpid-jms-0.34.0/docs/index.html
    api_url: https://docs.oracle.com/javaee/7/api/index.html?javax/jms/package-summary.html
    examples_url: https://github.com/apache/qpid-jms/tree/0.34.0/qpid-jms-examples
    maven_url: http://qpid.apache.org/maven.html#qpid-jms-amqp-10
    source_url: https://github.com/apache/qpid-jms
    icon_file: apache.svg
    tags: [jms, java]
    description: >-
      A mature AMQP implementation of the JMS 2.0 API
```

When you're ready, submit a pull request.  There's no need to make it
perfect.  I can fill in the details and ask follow up questions if I
need to.
