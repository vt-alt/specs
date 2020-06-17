# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname azure-sdk-for-ruby
%define        gemname azure-sdk-for-ruby

Name:          %pkgname
Version:       20200316
Release:       alt1.2
Summary:       Ruby SDK for Azure Resource Manager
License:       MIT
Group:         Development/Ruby
Url:           https://aka.ms/azure-sdk-for-ruby
Vcs:           https://github.com/Azure/azure-sdk-for-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%gem_replace_version unf_ext ~> 0.0.7
%gem_replace_version timeliness ~> 0.4
%gem_replace_version azure-storage ~> 0.15

%description
Ruby SDK for Azure Resource Manager: build and manage your Azure cloud
infrastructure (Compute, Virtual Networks, Storage, etc...) using Ruby.

This project provides a Ruby package for Azure Resource Management (ARM).

%package       -n gem-azure-sdk
Version:       0.52.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-sdk
Microsoft Azure SDK - Azure Client Library for Ruby


%package       -n gem-azure-sdk-doc
Version:       0.52.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-sdk-doc
Documentation files for %gemname gem.

%description   -n gem-azure-sdk-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-alerts-management
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume AlertsManagement
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-alerts-management
Official Ruby client library to consume AlertsManagement


%package       -n gem-azure-mgmt-alerts-management-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-alerts-management-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-alerts-management-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-recovery-services-site-recovery
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Recovery Services Site Recovery.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services-site-recovery
Microsoft Azure Recovery Services Site Recovery Services Library for Ruby


%package       -n gem-azure-mgmt-recovery-services-site-recovery-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services-site-recovery-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-recovery-services-site-recovery-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-edgegateway
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Edge Gateway services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-edgegateway
Microsoft Azure Edge Gateway Client Library for Ruby


%package       -n gem-azure-mgmt-edgegateway-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-edgegateway-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-edgegateway-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-container-instance
Version:       0.17.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Container Instance.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-instance
Microsoft Azure Container Instance Services Library for Ruby


%package       -n gem-azure-mgmt-container-instance-doc
Version:       0.17.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-instance-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-container-instance-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-notification-hubs
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Notification Hubs Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-notification-hubs
Microsoft Azure Notification Hubs Management Client Library for Ruby


%package       -n gem-azure-mgmt-notification-hubs-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-notification-hubs-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-notification-hubs-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-iot-central
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure IotCentral Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-iot-central
Microsoft Azure IotCentral Management Client Library for Ruby


%package       -n gem-azure-mgmt-iot-central-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-iot-central-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-iot-central-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-cognitive-services
Version:       0.19.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-cognitive-services
Microsoft Azure Cognitive Services Management Client Library for Ruby


%package       -n gem-azure-mgmt-cognitive-services-doc
Version:       0.19.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-cognitive-services-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-cognitive-services-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-relay
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Relay.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-relay
Microsoft Azure Relay Library for Ruby


%package       -n gem-azure-mgmt-relay-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-relay-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-relay-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-redis
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Redis Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-redis
Microsoft Azure Redis Management Client Library for Ruby


%package       -n gem-azure-mgmt-redis-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-redis-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-redis-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-reservations
Version:       0.19.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Reservations
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-reservations
Official Ruby client library to consume Reservations


%package       -n gem-azure-mgmt-reservations-doc
Version:       0.19.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-reservations-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-reservations-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-resource-health
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume ResourceHealth
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-resource-health
Official Ruby client library to consume ResourceHealth.


%package       -n gem-azure-mgmt-resource-health-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-resource-health-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-resource-health-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-marketplace-ordering
Version:       0.17.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Marketplace Ordering.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-marketplace-ordering
Microsoft Azure Marketplace Ordering Library for Ruby


%package       -n gem-azure-mgmt-marketplace-ordering-doc
Version:       0.17.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-marketplace-ordering-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-marketplace-ordering-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-iot-hub
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure IoT Hub Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-iot-hub
Microsoft Azure IoT Hub Management Client Library for Ruby


%package       -n gem-azure-mgmt-iot-hub-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-iot-hub-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-iot-hub-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-bot-service
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume BotService
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-bot-service
Official Ruby client library to consume BotService


%package       -n gem-azure-mgmt-bot-service-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-bot-service-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-bot-service-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-adhybridhealth-service
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume AdhybridhealthService
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-adhybridhealth-service
Official Ruby client library to consume AdhybridhealthService


%package       -n gem-azure-mgmt-adhybridhealth-service-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-adhybridhealth-service-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-adhybridhealth-service-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-labservices
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Labservices.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-labservices
Microsoft Azure Labservices Library for Ruby


%package       -n gem-azure-mgmt-labservices-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-labservices-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-labservices-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-sqlvirtualmachine
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure SQL Virtual Machine Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-sqlvirtualmachine
Microsoft Azure SQL Virtual Machine Management Client Library for Ruby


%package       -n gem-azure-mgmt-sqlvirtualmachine-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-sqlvirtualmachine-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-sqlvirtualmachine-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-stream-analytics
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Stream Analytics services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-stream-analytics
Microsoft Azure Stream Analytics Client Library for Ruby


%package       -n gem-azure-mgmt-stream-analytics-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-stream-analytics-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-stream-analytics-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-batch
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Batch Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-batch
Microsoft Azure Batch Management Client Library for Ruby


%package       -n gem-azure-mgmt-batch-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-batch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-batch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-mixedreality
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Mixed Reality Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-mixedreality
Microsoft Azure Mixed Reality Management Client Library for Ruby


%package       -n gem-azure-mgmt-mixedreality-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-mixedreality-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-mixedreality-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-postgresql
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Postgresql
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-postgresql
Official Ruby client library to consume Postgresql


%package       -n gem-azure-mgmt-postgresql-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-postgresql-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-postgresql-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-media-services
Version:       0.20.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Media Services Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-media-services
Microsoft Azure Media Services Management Client Library for Ruby


%package       -n gem-azure-mgmt-media-services-doc
Version:       0.20.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-media-services-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-media-services-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-maintenance
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Maintenance
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-maintenance
Official Ruby client library to consume Maintenance.


%package       -n gem-azure-mgmt-maintenance-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-maintenance-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-maintenance-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-managed-applications
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Managed Applications.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-managed-applications
Microsoft Azure Managed Applications Library for Ruby


%package       -n gem-azure-mgmt-managed-applications-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-managed-applications-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-managed-applications-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-cdn
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure CDN Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-cdn
Microsoft Azure CDN Management Client Library for Ruby


%package       -n gem-azure-mgmt-cdn-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-cdn-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-cdn-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-subscriptions
Version:       0.18.1
Release:       alt1.2
Summary:       Official ruby client library to consume Microsoft Azure Subscription Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-subscriptions
Microsoft Azure Subscription Management Client Library for Ruby


%package       -n gem-azure-mgmt-subscriptions-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-subscriptions-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-subscriptions-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-time-series-insights
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume TimeSeriesInsights
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-time-series-insights
Official Ruby client library to consume TimeSeriesInsights.


%package       -n gem-azure-mgmt-time-series-insights-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-time-series-insights-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-time-series-insights-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-traffic-manager
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Traffic Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-traffic-manager
Microsoft Azure Traffic Management Client Library for Ruby


%package       -n gem-azure-mgmt-traffic-manager-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-traffic-manager-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-traffic-manager-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-vmware-cloudsimple
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume TimeSeriesInsights
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-vmware-cloudsimple
Official Ruby client library to consume TimeSeriesInsights.


%package       -n gem-azure-mgmt-vmware-cloudsimple-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-vmware-cloudsimple-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-vmware-cloudsimple-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-operations-management
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume OperationsManagement
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-operations-management
Official Ruby client library to consume OperationsManagement


%package       -n gem-azure-mgmt-operations-management-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-operations-management-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-operations-management-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-peering
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Peering
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-peering
Official Ruby client library to consume Peering.


%package       -n gem-azure-mgmt-peering-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-peering-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-peering-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-web
Version:       0.17.5
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Web Apps Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-web
Microsoft Azure Web Apps Management Client Library for Ruby


%package       -n gem-azure-mgmt-web-doc
Version:       0.17.5
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-web-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-web-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-stor-simple8000-series
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Stor Simple 8000 Series.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-stor-simple8000-series
Microsoft Azure Stor Simple 8000 Series Library for Ruby


%package       -n gem-azure-mgmt-stor-simple8000-series-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-stor-simple8000-series-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-stor-simple8000-series-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-msi
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Managed Service Identity services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-msi
Microsoft Azure Managed Service Identity Library for Ruby


%package       -n gem-azure-mgmt-msi-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-msi-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-msi-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-privatedns
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Private DNS Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-privatedns
Microsoft Azure Private DNS Management Client Library for Ruby


%package       -n gem-azure-mgmt-privatedns-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-privatedns-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-privatedns-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-monitor
Version:       0.17.5
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Monitor services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-monitor
Microsoft Azure Monitor Library for Ruby


%package       -n gem-azure-mgmt-monitor-doc
Version:       0.17.5
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-monitor-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-monitor-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-recovery-services
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Recovery services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services
Microsoft Azure Recovery Services Library for Ruby


%package       -n gem-azure-mgmt-recovery-services-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-recovery-services-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-policy-insights
Version:       0.17.5
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Policy Insights Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-policy-insights
Microsoft Azure Resource Policy Insights Management Client Library for Ruby


%package       -n gem-azure-mgmt-policy-insights-doc
Version:       0.17.5
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-policy-insights-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-policy-insights-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-data-factory
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume DataFactory
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-data-factory
Official Ruby client library to consume DataFactory


%package       -n gem-azure-mgmt-data-factory-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-data-factory-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-data-factory-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-links
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Links.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-links
Microsoft Azure Links Library for Ruby


%package       -n gem-azure-mgmt-links-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-links-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-links-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-sql
Version:       0.19.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure SQL Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-sql
Microsoft Azure SQL Management Client Library for Ruby


%package       -n gem-azure-mgmt-sql-doc
Version:       0.19.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-sql-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-sql-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-event-hub
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Event Hub services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-event-hub
Microsoft Azure Event Hub Library for Ruby


%package       -n gem-azure-mgmt-event-hub-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-event-hub-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-event-hub-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-advisor
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Advisor services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-advisor
Microsoft Azure Advisor Services Library for Ruby


%package       -n gem-azure-mgmt-advisor-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-advisor-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-advisor-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-kusto
Version:       0.19.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Kusto Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-kusto
Microsoft Azure Kusto Management Client Library for Ruby


%package       -n gem-azure-mgmt-kusto-doc
Version:       0.19.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-kusto-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-kusto-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-signlr
Version:       0.0.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Signlr
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-signlr
Official Ruby client library to consume Signlr


%package       -n gem-azure-mgmt-signlr-doc
Version:       0.0.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-signlr-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-signlr-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-cosmosdb
Version:       0.21.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Cosmosdb
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-cosmosdb
Official Ruby client library to consume Cosmosdb


%package       -n gem-azure-mgmt-cosmosdb-doc
Version:       0.21.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-cosmosdb-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-cosmosdb-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-key-vault
Version:       0.17.5
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Management Key Vault services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-key-vault
Microsoft Azure Resource Management Key Vault Client Library for Ruby


%package       -n gem-azure-mgmt-key-vault-doc
Version:       0.17.5
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-key-vault-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-key-vault-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-automation
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Automation.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-automation
Microsoft Azure Automation Services Library for Ruby


%package       -n gem-azure-mgmt-automation-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-automation-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-automation-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-powerbi-dedicated
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume PowerbiDedicated
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-powerbi-dedicated
Official Ruby client library to consume PowerbiDedicated


%package       -n gem-azure-mgmt-powerbi-dedicated-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-powerbi-dedicated-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-powerbi-dedicated-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-machine-learning-services
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Machine Learning Services Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-machine-learning-services
Microsoft Azure Machine Learning Services Management Client Library for Ruby


%package       -n gem-azure-mgmt-machine-learning-services-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-machine-learning-services-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-machine-learning-services-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-service-fabric
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Service Fabric.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-service-fabric
Microsoft Azure Service Fabric Library for Ruby


%package       -n gem-azure-mgmt-service-fabric-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-service-fabric-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-service-fabric-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-azurestack
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Azurestack
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-azurestack
Official Ruby client library to consume Azurestack


%package       -n gem-azure-mgmt-azurestack-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-azurestack-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-azurestack-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-security
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Security Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-security
Microsoft Azure Security Management Client Library for Ruby


%package       -n gem-azure-mgmt-security-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-security-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-security-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-features
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Provider Feature Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-features
Microsoft Azure Resource Provider Feature Management Client Library for Ruby


%package       -n gem-azure-mgmt-features-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-features-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-features-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-batchai
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Batchai
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-batchai
Official Ruby client library to consume Batchai


%package       -n gem-azure-mgmt-batchai-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-batchai-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-batchai-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-dev-spaces
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Management DevSpaces.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-dev-spaces
Microsoft Azure Management DevSpaces Library for Ruby


%package       -n gem-azure-mgmt-dev-spaces-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-dev-spaces-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-dev-spaces-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-datalake-analytics
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Provider DataLake Analytics Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-datalake-analytics
Microsoft Azure Resource Provider DataLake Analytics Client Library for Ruby


%package       -n gem-azure-mgmt-datalake-analytics-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-datalake-analytics-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-datalake-analytics-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-netapp
Version:       0.18.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure NetApp services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-netapp
Microsoft Azure NetApp Library for Ruby


%package       -n gem-azure-mgmt-netapp-doc
Version:       0.18.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-netapp-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-netapp-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-event-grid
Version:       0.17.10
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Event Grid.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-event-grid
Microsoft Azure Event Grid Services Library for Ruby


%package       -n gem-azure-mgmt-event-grid-doc
Version:       0.17.10
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-event-grid-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-event-grid-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-data-migration
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Data Migration.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-data-migration
Microsoft Azure Data Migration Services Library for Ruby


%package       -n gem-azure-mgmt-data-migration-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-data-migration-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-data-migration-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-resources-management
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resources Management.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-resources-management
Microsoft Azure Resources Management Library for Ruby


%package       -n gem-azure-mgmt-resources-management-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-resources-management-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-resources-management-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-container-service
Version:       0.20.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Container Service Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-service
Microsoft Azure Container Service Management Client Library for Ruby


%package       -n gem-azure-mgmt-container-service-doc
Version:       0.20.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-service-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-container-service-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-databox
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Databox
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-databox
Official Ruby client library to consume Databox


%package       -n gem-azure-mgmt-databox-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-databox-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-databox-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-analysis-services
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Analysis services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-analysis-services
Microsoft Azure Analysis Services Library for Ruby


%package       -n gem-azure-mgmt-analysis-services-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-analysis-services-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-analysis-services-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-api-management
Version:       0.18.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure API Management.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-api-management
Microsoft Azure API Management Library for Ruby


%package       -n gem-azure-mgmt-api-management-doc
Version:       0.18.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-api-management-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-api-management-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-container-registry
Version:       0.18.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Container Registry.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-registry
Microsoft Azure Container Registry Services Library for Ruby


%package       -n gem-azure-mgmt-container-registry-doc
Version:       0.18.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-container-registry-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-container-registry-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-consumption
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Consumption.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-consumption
Microsoft Azure Consumption Services Library for Ruby


%package       -n gem-azure-mgmt-consumption-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-consumption-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-consumption-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-devtestlabs
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Dev Test Labs Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-devtestlabs
Microsoft Azure Dev Test Lab Management Client Library for Ruby


%package       -n gem-azure-mgmt-devtestlabs-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-devtestlabs-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-devtestlabs-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-resourcegraph
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Graph.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-resourcegraph
Microsoft Azure Resource Graph Library for Ruby


%package       -n gem-azure-mgmt-resourcegraph-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-resourcegraph-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-resourcegraph-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-network
Version:       0.23.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Network Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-network
Microsoft Azure Network Management Client Library for Ruby


%package       -n gem-azure-mgmt-network-doc
Version:       0.23.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-network-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-network-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-serialconsole
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Serialconsole
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-serialconsole
Official Ruby client library to consume Serialconsole


%package       -n gem-azure-mgmt-serialconsole-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-serialconsole-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-serialconsole-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-locks
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Lock Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-locks
Microsoft Azure Resource Lock Management Client Library for Ruby


%package       -n gem-azure-mgmt-locks-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-locks-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-locks-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-service-bus
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Service Bus Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-service-bus
Microsoft Azure Service Bus Management Client Library for Ruby


%package       -n gem-azure-mgmt-service-bus-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-service-bus-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-service-bus-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-migrate
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Migrate
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-migrate
Official Ruby client library to consume Migrate


%package       -n gem-azure-mgmt-migrate-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-migrate-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-migrate-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-hdinsight
Version:       0.17.7
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Hdinsight Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-hdinsight
Microsoft Azure Hdinsight Management Client Library for Ruby


%package       -n gem-azure-mgmt-hdinsight-doc
Version:       0.17.7
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-hdinsight-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-hdinsight-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-import-export
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume ImportExport
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-import-export
Official Ruby client library to consume ImportExport.


%package       -n gem-azure-mgmt-import-export-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-import-export-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-import-export-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-appconfiguration
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Appconfiguration
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-appconfiguration
Official Ruby client library to consume Appconfiguration


%package       -n gem-azure-mgmt-appconfiguration-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-appconfiguration-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-appconfiguration-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-attestation
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Appconfiguration
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-attestation
Official Ruby client library to consume Appconfiguration


%package       -n gem-azure-mgmt-attestation-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-attestation-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-attestation-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-resources
Version:       0.17.8
Release:       alt1.2
Summary:       Official ruby client library to consume Microsoft Azure Resource Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-resources
Microsoft Azure Resource Management Client Library for Ruby


%package       -n gem-azure-mgmt-resources-doc
Version:       0.17.8
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-resources-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-resources-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-mariadb
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure MariaDB services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-mariadb
Microsoft Azure MariaDB Library for Ruby


%package       -n gem-azure-mgmt-mariadb-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-mariadb-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-mariadb-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-cost-management
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume CostManagement
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-cost-management
Official Ruby client library to consume CostManagement


%package       -n gem-azure-mgmt-cost-management-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-cost-management-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-cost-management-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-powerbi-embedded
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Power BI Embedded Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-powerbi-embedded
Microsoft Azure Power BI Embedded Management Client Library for Ruby


%package       -n gem-azure-mgmt-powerbi-embedded-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-powerbi-embedded-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-powerbi-embedded-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-scheduler
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Scheduler Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-scheduler
Microsoft Azure Scheduler Management Client Library for Ruby


%package       -n gem-azure-mgmt-scheduler-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-scheduler-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-scheduler-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-operational-insights
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Operational Insights.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-operational-insights
Microsoft Azure Operational Insights Library for Ruby


%package       -n gem-azure-mgmt-operational-insights-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-operational-insights-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-operational-insights-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-authorization
Version:       0.18.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Role Based Authorization Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-authorization
Microsoft Azure Role Based Authorization Management Client Library for Ruby


%package       -n gem-azure-mgmt-authorization-doc
Version:       0.18.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-authorization-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-authorization-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-policy
Version:       0.17.8
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Policy Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-policy
Microsoft Azure Resource Policy Management Client Library for Ruby


%package       -n gem-azure-mgmt-policy-doc
Version:       0.17.8
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-policy-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-policy-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-portal
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Portal
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-portal
Official Ruby client library to consume Portal.


%package       -n gem-azure-mgmt-portal-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-portal-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-portal-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-logic
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Logic Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-logic
Microsoft Azure Logic Management Client Library for Ruby


%package       -n gem-azure-mgmt-logic-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-logic-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-logic-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-billing
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Billing.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-billing
Microsoft Azure Billing Services Library for Ruby


%package       -n gem-azure-mgmt-billing-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-billing-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-billing-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-dns
Version:       0.17.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Dns Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-dns
Microsoft Azure Dns Management Client Library for Ruby


%package       -n gem-azure-mgmt-dns-doc
Version:       0.17.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-dns-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-dns-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-machine-learning
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Machine Learning Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-machine-learning
Microsoft Azure Machine Learning Management Client Library for Ruby


%package       -n gem-azure-mgmt-machine-learning-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-machine-learning-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-machine-learning-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-recovery-services-backup
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Recovery Services Backup.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services-backup
Microsoft Azure Recovery Services Backup Library for Ruby


%package       -n gem-azure-mgmt-recovery-services-backup-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-recovery-services-backup-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-recovery-services-backup-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-commerce
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Commerce Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-commerce
Microsoft Azure Commerce Management Client Library for Ruby


%package       -n gem-azure-mgmt-commerce-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-commerce-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-commerce-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-datalake-store
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Resource Provider DataLake Store Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-datalake-store
Microsoft Azure Resource Provider DataLake Store Client Library for Ruby


%package       -n gem-azure-mgmt-datalake-store-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-datalake-store-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-datalake-store-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-datashare
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Datashare
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-datashare
Official Ruby client library to consume Datashare.


%package       -n gem-azure-mgmt-datashare-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-datashare-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-datashare-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-deployment-manager
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume DeploymentManager
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-deployment-manager
Official Ruby client library to consume DeploymentManager.


%package       -n gem-azure-mgmt-deployment-manager-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-deployment-manager-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-deployment-manager-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-storagesync
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure StorageSync.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-storagesync
Microsoft Azure StorageSync Library for Ruby


%package       -n gem-azure-mgmt-storagesync-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-storagesync-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-storagesync-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-storagecache
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Storagecache
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-storagecache
Official Ruby client library to consume Storagecache.


%package       -n gem-azure-mgmt-storagecache-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-storagecache-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-storagecache-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-storage
Version:       0.19.3
Release:       alt1.2
Summary:       Official ruby client library to consume Microsoft Azure Storage Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-storage
Microsoft Azure Storage Management Client Library for Ruby


%package       -n gem-azure-mgmt-storage-doc
Version:       0.19.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-storage-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-storage-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-signalr
Version:       0.17.4
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Signalr.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-signalr
Microsoft Azure Signalr Library for Ruby


%package       -n gem-azure-mgmt-signalr-doc
Version:       0.17.4
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-signalr-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-signalr-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-search
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Search Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-search
Microsoft Azure Search Management Client Library for Ruby


%package       -n gem-azure-mgmt-search-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-search-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-search-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-compute
Version:       0.19.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Compute Management services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-compute
Microsoft Azure Compute Management Client Library for Ruby


%package       -n gem-azure-mgmt-compute-doc
Version:       0.19.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-compute-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-compute-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-customer-insights
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Customer Insights.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-customer-insights
Microsoft Azure Customer Insights Services Library for Ruby


%package       -n gem-azure-mgmt-customer-insights-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-customer-insights-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-customer-insights-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-hanaonazure
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Hanaonazure
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-hanaonazure
Official Ruby client library to consume Hanaonazure


%package       -n gem-azure-mgmt-hanaonazure-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-hanaonazure-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-hanaonazure-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-mgmt-mysql
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Mysql
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-mgmt-mysql
Official Ruby client library to consume Mysql


%package       -n gem-azure-mgmt-mysql-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-mgmt-mysql-doc
Documentation files for %gemname gem.

%description   -n gem-azure-mgmt-mysql-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-contentmoderator
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Content Moderator.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-contentmoderator
Microsoft Azure Cognitive Services Content Moderator Client Library for Ruby


%package       -n gem-azure-cognitiveservices-contentmoderator-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-contentmoderator-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-contentmoderator-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-service-fabric
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Service Fabric.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-service-fabric
Microsoft Azure Service Fabric Client Library for Ruby


%package       -n gem-azure-service-fabric-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-service-fabric-doc
Documentation files for %gemname gem.

%description   -n gem-azure-service-fabric-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-customimagesearch
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Custom Image Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customimagesearch
Microsoft Azure Cognitive Services Custom Image Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-customimagesearch-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customimagesearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-customimagesearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-anomalydetector
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Anomaly Detector.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-anomalydetector
Microsoft Azure Cognitive Services Anomaly Detector Client Library for Ruby


%package       -n gem-azure-cognitiveservices-anomalydetector-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-anomalydetector-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-anomalydetector-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-luisruntime
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services LUIS Runtime.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-luisruntime
Microsoft Azure Cognitive Services LUIS Runtime Client Library for Ruby


%package       -n gem-azure-cognitiveservices-luisruntime-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-luisruntime-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-luisruntime-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-videosearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Video Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-videosearch
Microsoft Azure Cognitive Services Video Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-videosearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-videosearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-videosearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-face
Version:       0.19.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Face.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-face
Microsoft Azure Cognitive Services Face Client Library for Ruby


%package       -n gem-azure-cognitiveservices-face-doc
Version:       0.19.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-face-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-face-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-key-vault
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Key Vault.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-key-vault
Microsoft Azure Key Vault Client Library for Ruby


%package       -n gem-azure-key-vault-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-key-vault-doc
Documentation files for %gemname gem.

%description   -n gem-azure-key-vault-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-autosuggest
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Auto Suggest.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-autosuggest
Microsoft Azure Cognitive Services Auto Suggest Client Library for Ruby


%package       -n gem-azure-cognitiveservices-autosuggest-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-autosuggest-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-autosuggest-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-customsearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Custom Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customsearch
Microsoft Azure Cognitive Services Custom Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-customsearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customsearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-customsearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-entitysearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Entity Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-entitysearch
Microsoft Azure Cognitive Services Entity Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-entitysearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-entitysearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-entitysearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-graph-rbac
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Active Directory Graph Rbac services.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-graph-rbac
Microsoft Azure Active Directory Graph Rbac Client Library for Ruby


%package       -n gem-azure-graph-rbac-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-graph-rbac-doc
Documentation files for %gemname gem.

%description   -n gem-azure-graph-rbac-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-localsearch
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Local Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-localsearch
Microsoft Azure Cognitive Services Local Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-localsearch-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-localsearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-localsearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-qnamakerruntime
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume CognitiveservicesQnamakerruntime
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-qnamakerruntime
Official Ruby client library to consume CognitiveservicesQnamakerruntime


%package       -n gem-azure-cognitiveservices-qnamakerruntime-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-qnamakerruntime-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-qnamakerruntime-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-websearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Web Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-websearch
Microsoft Azure Cognitive Services Web Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-websearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-websearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-websearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-customvisiontraining
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Custom Vision Training.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customvisiontraining
Microsoft Azure Cognitive Services Custom Vision Training Client Library for
Ruby


%package       -n gem-azure-cognitiveservices-customvisiontraining-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customvisiontraining-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-customvisiontraining-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-newssearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services News Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-newssearch
Microsoft Azure Cognitive Services News Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-newssearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-newssearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-newssearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-textanalytics
Version:       0.17.3
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Text Analytics.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-textanalytics
Microsoft Azure Cognitive Services Text Analytics Client Library for Ruby


%package       -n gem-azure-cognitiveservices-textanalytics-doc
Version:       0.17.3
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-textanalytics-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-textanalytics-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-spellcheck
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Spell Check.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-spellcheck
Microsoft Azure Cognitive Services Spell Check Client Library for Ruby


%package       -n gem-azure-cognitiveservices-spellcheck-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-spellcheck-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-spellcheck-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-luisauthoring
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services LUIS Runtime.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-luisauthoring
Microsoft Azure Cognitive Services LUIS Runtime Client Library for Ruby


%package       -n gem-azure-cognitiveservices-luisauthoring-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-luisauthoring-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-luisauthoring-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-event-grid
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Event Grid.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-event-grid
Microsoft Azure Event Grid Client Library for Ruby


%package       -n gem-azure-event-grid-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-event-grid-doc
Documentation files for %gemname gem.

%description   -n gem-azure-event-grid-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-computervision
Version:       0.20.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Computer Vision.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-computervision
Microsoft Azure Cognitive Services Computer Vision Client Library for Ruby


%package       -n gem-azure-cognitiveservices-computervision-doc
Version:       0.20.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-computervision-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-computervision-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-qnamaker
Version:       0.18.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services QnAMaker.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-qnamaker
Microsoft Azure Cognitive Services QnAMaker Client Library for Ruby


%package       -n gem-azure-cognitiveservices-qnamaker-doc
Version:       0.18.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-qnamaker-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-qnamaker-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-personalizer
Version:       0.17.0
Release:       alt1.2
Summary:       Official Ruby client library to consume Cognitiveservices Personalizer
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-personalizer
Official Ruby client library to consume Cognitiveservices Personalizer


%package       -n gem-azure-cognitiveservices-personalizer-doc
Version:       0.17.0
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-personalizer-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-personalizer-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-customvisionprediction
Version:       0.17.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Custom Vision Prediction.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customvisionprediction
Microsoft Azure Cognitive Services Custom Vision Prediction Library for Ruby


%package       -n gem-azure-cognitiveservices-customvisionprediction-doc
Version:       0.17.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-customvisionprediction-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-customvisionprediction-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-visualsearch
Version:       0.18.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Visual Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-visualsearch
Microsoft Azure Cognitive Services Visual Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-visualsearch-doc
Version:       0.18.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-visualsearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-visualsearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-formrecognizer
Version:       0.17.1
Release:       alt1.2
Summary:       Official Ruby client library to consume Cognitiveservices Form Recognizer
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-formrecognizer
Official Ruby client library to consume Cognitiveservices Form Recognizer


%package       -n gem-azure-cognitiveservices-formrecognizer-doc
Version:       0.17.1
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-formrecognizer-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-formrecognizer-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-azure-cognitiveservices-imagesearch
Version:       0.18.2
Release:       alt1.2
Summary:       Official Ruby client library to consume Microsoft Azure Cognitive Services Image Search.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-imagesearch
Microsoft Azure Cognitive Services Image Search Client Library for Ruby


%package       -n gem-azure-cognitiveservices-imagesearch-doc
Version:       0.18.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-azure-cognitiveservices-imagesearch-doc
Documentation files for %gemname gem.

%description   -n gem-azure-cognitiveservices-imagesearch-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-ms-rest-azure
Version:       0.11.2
Release:       alt1.2
Summary:       Azure Client Library for Ruby.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-ms-rest-azure
Azure Client Library for Ruby.


%package       -n gem-ms-rest-azure-doc
Version:       0.11.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-ms-rest-azure-doc
Documentation files for %gemname gem.

%description   -n gem-ms-rest-azure-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-ms-rest
Version:       0.7.6
Release:       alt1.2
Summary:       Client Library for Ruby.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-ms-rest
Client Library for Ruby.


%package       -n gem-ms-rest-doc
Version:       0.11.2
Release:       alt1.2
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-ms-rest-doc
Documentation files for %gemname gem.

%description   -n gem-ms-rest-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Version:       0.7.6
Release:       alt1.2
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=gem-azure-sdk-for-ruby,azure-sdk-for-ruby

%install
%ruby_install

%check
%ruby_test

%files
%doc README*

%files         doc

%files         -n gem-azure-sdk
%doc README*
%ruby_gemspecdir/azure_sdk-0.52.1.gemspec
%ruby_gemslibdir/azure_sdk-0.52.1

%files         -n gem-azure-sdk-doc
%ruby_gemsdocdir/azure_sdk-0.52.1

%files         -n gem-azure-mgmt-alerts-management
%doc README*
%ruby_gemspecdir/azure_mgmt_alerts_management-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_alerts_management-0.17.0

%files         -n gem-azure-mgmt-alerts-management-doc
%ruby_gemsdocdir/azure_mgmt_alerts_management-0.17.0

%files         -n gem-azure-mgmt-recovery-services-site-recovery
%doc README*
%ruby_gemspecdir/azure_mgmt_recovery_services_site_recovery-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_recovery_services_site_recovery-0.17.2

%files         -n gem-azure-mgmt-recovery-services-site-recovery-doc
%ruby_gemsdocdir/azure_mgmt_recovery_services_site_recovery-0.17.2

%files         -n gem-azure-mgmt-edgegateway
%doc README*
%ruby_gemspecdir/azure_mgmt_edgegateway-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_edgegateway-0.18.0

%files         -n gem-azure-mgmt-edgegateway-doc
%ruby_gemsdocdir/azure_mgmt_edgegateway-0.18.0

%files         -n gem-azure-mgmt-container-instance
%doc README*
%ruby_gemspecdir/azure_mgmt_container_instance-0.17.4.gemspec
%ruby_gemslibdir/azure_mgmt_container_instance-0.17.4

%files         -n gem-azure-mgmt-container-instance-doc
%ruby_gemsdocdir/azure_mgmt_container_instance-0.17.4

%files         -n gem-azure-mgmt-notification-hubs
%doc README*
%ruby_gemspecdir/azure_mgmt_notification_hubs-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_notification_hubs-0.17.2

%files         -n gem-azure-mgmt-notification-hubs-doc
%ruby_gemsdocdir/azure_mgmt_notification_hubs-0.17.2

%files         -n gem-azure-mgmt-iot-central
%doc README*
%ruby_gemspecdir/azure_mgmt_iot_central-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_iot_central-0.18.0

%files         -n gem-azure-mgmt-iot-central-doc
%ruby_gemsdocdir/azure_mgmt_iot_central-0.18.0

%files         -n gem-azure-mgmt-cognitive-services
%doc README*
%ruby_gemspecdir/azure_mgmt_cognitive_services-0.19.0.gemspec
%ruby_gemslibdir/azure_mgmt_cognitive_services-0.19.0

%files         -n gem-azure-mgmt-cognitive-services-doc
%ruby_gemsdocdir/azure_mgmt_cognitive_services-0.19.0

%files         -n gem-azure-mgmt-relay
%doc README*
%ruby_gemspecdir/azure_mgmt_relay-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_relay-0.17.2

%files         -n gem-azure-mgmt-relay-doc
%ruby_gemsdocdir/azure_mgmt_relay-0.17.2

%files         -n gem-azure-mgmt-redis
%doc README*
%ruby_gemspecdir/azure_mgmt_redis-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_redis-0.17.3

%files         -n gem-azure-mgmt-redis-doc
%ruby_gemsdocdir/azure_mgmt_redis-0.17.3

%files         -n gem-azure-mgmt-reservations
%doc README*
%ruby_gemspecdir/azure_mgmt_reservations-0.19.1.gemspec
%ruby_gemslibdir/azure_mgmt_reservations-0.19.1

%files         -n gem-azure-mgmt-reservations-doc
%ruby_gemsdocdir/azure_mgmt_reservations-0.19.1

%files         -n gem-azure-mgmt-resource-health
%doc README*
%ruby_gemspecdir/azure_mgmt_resource_health-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_resource_health-0.17.0

%files         -n gem-azure-mgmt-resource-health-doc
%ruby_gemsdocdir/azure_mgmt_resource_health-0.17.0

%files         -n gem-azure-mgmt-marketplace-ordering
%doc README*
%ruby_gemspecdir/azure_mgmt_marketplace_ordering-0.17.4.gemspec
%ruby_gemslibdir/azure_mgmt_marketplace_ordering-0.17.4

%files         -n gem-azure-mgmt-marketplace-ordering-doc
%ruby_gemsdocdir/azure_mgmt_marketplace_ordering-0.17.4

%files         -n gem-azure-mgmt-iot-hub
%doc README*
%ruby_gemspecdir/azure_mgmt_iot_hub-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_iot_hub-0.17.3

%files         -n gem-azure-mgmt-iot-hub-doc
%ruby_gemsdocdir/azure_mgmt_iot_hub-0.17.3

%files         -n gem-azure-mgmt-bot-service
%doc README*
%ruby_gemspecdir/azure_mgmt_bot_service-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_bot_service-0.17.0

%files         -n gem-azure-mgmt-bot-service-doc
%ruby_gemsdocdir/azure_mgmt_bot_service-0.17.0

%files         -n gem-azure-mgmt-adhybridhealth-service
%doc README*
%ruby_gemspecdir/azure_mgmt_adhybridhealth_service-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_adhybridhealth_service-0.17.0

%files         -n gem-azure-mgmt-adhybridhealth-service-doc
%ruby_gemsdocdir/azure_mgmt_adhybridhealth_service-0.17.0

%files         -n gem-azure-mgmt-labservices
%doc README*
%ruby_gemspecdir/azure_mgmt_labservices-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_labservices-0.17.1

%files         -n gem-azure-mgmt-labservices-doc
%ruby_gemsdocdir/azure_mgmt_labservices-0.17.1

%files         -n gem-azure-mgmt-sqlvirtualmachine
%doc README*
%ruby_gemspecdir/azure_mgmt_sqlvirtualmachine-0.18.1.gemspec
%ruby_gemslibdir/azure_mgmt_sqlvirtualmachine-0.18.1

%files         -n gem-azure-mgmt-sqlvirtualmachine-doc
%ruby_gemsdocdir/azure_mgmt_sqlvirtualmachine-0.18.1

%files         -n gem-azure-mgmt-stream-analytics
%doc README*
%ruby_gemspecdir/azure_mgmt_stream_analytics-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_stream_analytics-0.17.2

%files         -n gem-azure-mgmt-stream-analytics-doc
%ruby_gemsdocdir/azure_mgmt_stream_analytics-0.17.2

%files         -n gem-azure-mgmt-batch
%doc README*
%ruby_gemspecdir/azure_mgmt_batch-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_batch-0.18.0

%files         -n gem-azure-mgmt-batch-doc
%ruby_gemsdocdir/azure_mgmt_batch-0.18.0

%files         -n gem-azure-mgmt-mixedreality
%doc README*
%ruby_gemspecdir/azure_mgmt_mixedreality-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_mixedreality-0.17.2

%files         -n gem-azure-mgmt-mixedreality-doc
%ruby_gemsdocdir/azure_mgmt_mixedreality-0.17.2

%files         -n gem-azure-mgmt-postgresql
%doc README*
%ruby_gemspecdir/azure_mgmt_postgresql-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_postgresql-0.17.1

%files         -n gem-azure-mgmt-postgresql-doc
%ruby_gemsdocdir/azure_mgmt_postgresql-0.17.1

%files         -n gem-azure-mgmt-media-services
%doc README*
%ruby_gemspecdir/azure_mgmt_media_services-0.20.0.gemspec
%ruby_gemslibdir/azure_mgmt_media_services-0.20.0

%files         -n gem-azure-mgmt-media-services-doc
%ruby_gemsdocdir/azure_mgmt_media_services-0.20.0

%files         -n gem-azure-mgmt-maintenance
%doc README*
%ruby_gemspecdir/azure_mgmt_maintenance-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_maintenance-0.17.0

%files         -n gem-azure-mgmt-maintenance-doc
%ruby_gemsdocdir/azure_mgmt_maintenance-0.17.0

%files         -n gem-azure-mgmt-managed-applications
%doc README*
%ruby_gemspecdir/azure_mgmt_managed_applications-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_managed_applications-0.17.2

%files         -n gem-azure-mgmt-managed-applications-doc
%ruby_gemsdocdir/azure_mgmt_managed_applications-0.17.2

%files         -n gem-azure-mgmt-cdn
%doc README*
%ruby_gemspecdir/azure_mgmt_cdn-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_cdn-0.17.3

%files         -n gem-azure-mgmt-cdn-doc
%ruby_gemsdocdir/azure_mgmt_cdn-0.17.3

%files         -n gem-azure-mgmt-subscriptions
%doc README*
%ruby_gemspecdir/azure_mgmt_subscriptions-0.18.1.gemspec
%ruby_gemslibdir/azure_mgmt_subscriptions-0.18.1

%files         -n gem-azure-mgmt-subscriptions-doc
%ruby_gemsdocdir/azure_mgmt_subscriptions-0.18.1

%files         -n gem-azure-mgmt-time-series-insights
%doc README*
%ruby_gemspecdir/azure_mgmt_time_series_insights-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_time_series_insights-0.17.0

%files         -n gem-azure-mgmt-time-series-insights-doc
%ruby_gemsdocdir/azure_mgmt_time_series_insights-0.17.0

%files         -n gem-azure-mgmt-traffic-manager
%doc README*
%ruby_gemspecdir/azure_mgmt_traffic_manager-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_traffic_manager-0.17.2

%files         -n gem-azure-mgmt-traffic-manager-doc
%ruby_gemsdocdir/azure_mgmt_traffic_manager-0.17.2

%files         -n gem-azure-mgmt-vmware-cloudsimple
%doc README*
%ruby_gemspecdir/azure_mgmt_vmware_cloudsimple-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_vmware_cloudsimple-0.17.0

%files         -n gem-azure-mgmt-vmware-cloudsimple-doc
%ruby_gemsdocdir/azure_mgmt_vmware_cloudsimple-0.17.0

%files         -n gem-azure-mgmt-operations-management
%doc README*
%ruby_gemspecdir/azure_mgmt_operations_management-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_operations_management-0.17.0

%files         -n gem-azure-mgmt-operations-management-doc
%ruby_gemsdocdir/azure_mgmt_operations_management-0.17.0

%files         -n gem-azure-mgmt-peering
%doc README*
%ruby_gemspecdir/azure_mgmt_peering-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_peering-0.17.0

%files         -n gem-azure-mgmt-peering-doc
%ruby_gemsdocdir/azure_mgmt_peering-0.17.0

%files         -n gem-azure-mgmt-web
%doc README*
%ruby_gemspecdir/azure_mgmt_web-0.17.5.gemspec
%ruby_gemslibdir/azure_mgmt_web-0.17.5

%files         -n gem-azure-mgmt-web-doc
%ruby_gemsdocdir/azure_mgmt_web-0.17.5

%files         -n gem-azure-mgmt-stor-simple8000-series
%doc README*
%ruby_gemspecdir/azure_mgmt_stor_simple8000_series-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_stor_simple8000_series-0.17.2

%files         -n gem-azure-mgmt-stor-simple8000-series-doc
%ruby_gemsdocdir/azure_mgmt_stor_simple8000_series-0.17.2

%files         -n gem-azure-mgmt-msi
%doc README*
%ruby_gemspecdir/azure_mgmt_msi-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_msi-0.17.1

%files         -n gem-azure-mgmt-msi-doc
%ruby_gemsdocdir/azure_mgmt_msi-0.17.1

%files         -n gem-azure-mgmt-privatedns
%doc README*
%ruby_gemspecdir/azure_mgmt_privatedns-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_privatedns-0.17.1

%files         -n gem-azure-mgmt-privatedns-doc
%ruby_gemsdocdir/azure_mgmt_privatedns-0.17.1

%files         -n gem-azure-mgmt-monitor
%doc README*
%ruby_gemspecdir/azure_mgmt_monitor-0.17.5.gemspec
%ruby_gemslibdir/azure_mgmt_monitor-0.17.5

%files         -n gem-azure-mgmt-monitor-doc
%ruby_gemsdocdir/azure_mgmt_monitor-0.17.5

%files         -n gem-azure-mgmt-recovery-services
%doc README*
%ruby_gemspecdir/azure_mgmt_recovery_services-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_recovery_services-0.17.3

%files         -n gem-azure-mgmt-recovery-services-doc
%ruby_gemsdocdir/azure_mgmt_recovery_services-0.17.3

%files         -n gem-azure-mgmt-policy-insights
%doc README*
%ruby_gemspecdir/azure_mgmt_policy_insights-0.17.5.gemspec
%ruby_gemslibdir/azure_mgmt_policy_insights-0.17.5

%files         -n gem-azure-mgmt-policy-insights-doc
%ruby_gemsdocdir/azure_mgmt_policy_insights-0.17.5

%files         -n gem-azure-mgmt-data-factory
%doc README*
%ruby_gemspecdir/azure_mgmt_data_factory-0.18.1.gemspec
%ruby_gemslibdir/azure_mgmt_data_factory-0.18.1

%files         -n gem-azure-mgmt-data-factory-doc
%ruby_gemsdocdir/azure_mgmt_data_factory-0.18.1

%files         -n gem-azure-mgmt-links
%doc README*
%ruby_gemspecdir/azure_mgmt_links-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_links-0.17.2

%files         -n gem-azure-mgmt-links-doc
%ruby_gemsdocdir/azure_mgmt_links-0.17.2

%files         -n gem-azure-mgmt-sql
%doc README*
%ruby_gemspecdir/azure_mgmt_sql-0.19.0.gemspec
%ruby_gemslibdir/azure_mgmt_sql-0.19.0

%files         -n gem-azure-mgmt-sql-doc
%ruby_gemsdocdir/azure_mgmt_sql-0.19.0

%files         -n gem-azure-mgmt-event-hub
%doc README*
%ruby_gemspecdir/azure_mgmt_event_hub-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_event_hub-0.18.0

%files         -n gem-azure-mgmt-event-hub-doc
%ruby_gemsdocdir/azure_mgmt_event_hub-0.18.0

%files         -n gem-azure-mgmt-advisor
%doc README*
%ruby_gemspecdir/azure_mgmt_advisor-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_advisor-0.17.0

%files         -n gem-azure-mgmt-advisor-doc
%ruby_gemsdocdir/azure_mgmt_advisor-0.17.0

%files         -n gem-azure-mgmt-kusto
%doc README*
%ruby_gemspecdir/azure_mgmt_kusto-0.19.1.gemspec
%ruby_gemslibdir/azure_mgmt_kusto-0.19.1

%files         -n gem-azure-mgmt-kusto-doc
%ruby_gemsdocdir/azure_mgmt_kusto-0.19.1

%files         -n gem-azure-mgmt-signlr
%doc README*
%ruby_gemspecdir/azure_mgmt_signlr-0.0.1.gemspec
%ruby_gemslibdir/azure_mgmt_signlr-0.0.1

%files         -n gem-azure-mgmt-signlr-doc
%ruby_gemsdocdir/azure_mgmt_signlr-0.0.1

%files         -n gem-azure-mgmt-cosmosdb
%doc README*
%ruby_gemspecdir/azure_mgmt_cosmosdb-0.21.0.gemspec
%ruby_gemslibdir/azure_mgmt_cosmosdb-0.21.0

%files         -n gem-azure-mgmt-cosmosdb-doc
%ruby_gemsdocdir/azure_mgmt_cosmosdb-0.21.0

%files         -n gem-azure-mgmt-key-vault
%doc README*
%ruby_gemspecdir/azure_mgmt_key_vault-0.17.5.gemspec
%ruby_gemslibdir/azure_mgmt_key_vault-0.17.5

%files         -n gem-azure-mgmt-key-vault-doc
%ruby_gemsdocdir/azure_mgmt_key_vault-0.17.5

%files         -n gem-azure-mgmt-automation
%doc README*
%ruby_gemspecdir/azure_mgmt_automation-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_automation-0.17.2

%files         -n gem-azure-mgmt-automation-doc
%ruby_gemsdocdir/azure_mgmt_automation-0.17.2

%files         -n gem-azure-mgmt-powerbi-dedicated
%doc README*
%ruby_gemspecdir/azure_mgmt_powerbi_dedicated-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_powerbi_dedicated-0.17.0

%files         -n gem-azure-mgmt-powerbi-dedicated-doc
%ruby_gemsdocdir/azure_mgmt_powerbi_dedicated-0.17.0

%files         -n gem-azure-mgmt-machine-learning-services
%doc README*
%ruby_gemspecdir/azure_mgmt_machine_learning_services-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_machine_learning_services-0.17.2

%files         -n gem-azure-mgmt-machine-learning-services-doc
%ruby_gemsdocdir/azure_mgmt_machine_learning_services-0.17.2

%files         -n gem-azure-mgmt-service-fabric
%doc README*
%ruby_gemspecdir/azure_mgmt_service_fabric-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_service_fabric-0.17.2

%files         -n gem-azure-mgmt-service-fabric-doc
%ruby_gemsdocdir/azure_mgmt_service_fabric-0.17.2

%files         -n gem-azure-mgmt-azurestack
%doc README*
%ruby_gemspecdir/azure_mgmt_azurestack-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_azurestack-0.17.1

%files         -n gem-azure-mgmt-azurestack-doc
%ruby_gemsdocdir/azure_mgmt_azurestack-0.17.1

%files         -n gem-azure-mgmt-security
%doc README*
%ruby_gemspecdir/azure_mgmt_security-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_security-0.18.0

%files         -n gem-azure-mgmt-security-doc
%ruby_gemsdocdir/azure_mgmt_security-0.18.0

%files         -n gem-azure-mgmt-features
%doc README*
%ruby_gemspecdir/azure_mgmt_features-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_features-0.17.2

%files         -n gem-azure-mgmt-features-doc
%ruby_gemsdocdir/azure_mgmt_features-0.17.2

%files         -n gem-azure-mgmt-batchai
%doc README*
%ruby_gemspecdir/azure_mgmt_batchai-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_batchai-0.17.0

%files         -n gem-azure-mgmt-batchai-doc
%ruby_gemsdocdir/azure_mgmt_batchai-0.17.0

%files         -n gem-azure-mgmt-dev-spaces
%doc README*
%ruby_gemspecdir/azure_mgmt_dev_spaces-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_dev_spaces-0.17.2

%files         -n gem-azure-mgmt-dev-spaces-doc
%ruby_gemsdocdir/azure_mgmt_dev_spaces-0.17.2

%files         -n gem-azure-mgmt-datalake-analytics
%doc README*
%ruby_gemspecdir/azure_mgmt_datalake_analytics-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_datalake_analytics-0.17.2

%files         -n gem-azure-mgmt-datalake-analytics-doc
%ruby_gemsdocdir/azure_mgmt_datalake_analytics-0.17.2

%files         -n gem-azure-mgmt-netapp
%doc README*
%ruby_gemspecdir/azure_mgmt_netapp-0.18.3.gemspec
%ruby_gemslibdir/azure_mgmt_netapp-0.18.3

%files         -n gem-azure-mgmt-netapp-doc
%ruby_gemsdocdir/azure_mgmt_netapp-0.18.3

%files         -n gem-azure-mgmt-event-grid
%doc README*
%ruby_gemspecdir/azure_mgmt_event_grid-0.17.10.gemspec
%ruby_gemslibdir/azure_mgmt_event_grid-0.17.10

%files         -n gem-azure-mgmt-event-grid-doc
%ruby_gemsdocdir/azure_mgmt_event_grid-0.17.10

%files         -n gem-azure-mgmt-data-migration
%doc README*
%ruby_gemspecdir/azure_mgmt_data_migration-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_data_migration-0.18.0

%files         -n gem-azure-mgmt-data-migration-doc
%ruby_gemsdocdir/azure_mgmt_data_migration-0.18.0

%files         -n gem-azure-mgmt-resources-management
%doc README*
%ruby_gemspecdir/azure_mgmt_resources_management-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_resources_management-0.17.1

%files         -n gem-azure-mgmt-resources-management-doc
%ruby_gemsdocdir/azure_mgmt_resources_management-0.17.1

%files         -n gem-azure-mgmt-container-service
%doc README*
%ruby_gemspecdir/azure_mgmt_container_service-0.20.1.gemspec
%ruby_gemslibdir/azure_mgmt_container_service-0.20.1

%files         -n gem-azure-mgmt-container-service-doc
%ruby_gemsdocdir/azure_mgmt_container_service-0.20.1

%files         -n gem-azure-mgmt-databox
%doc README*
%ruby_gemspecdir/azure_mgmt_databox-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_databox-0.17.0

%files         -n gem-azure-mgmt-databox-doc
%ruby_gemsdocdir/azure_mgmt_databox-0.17.0

%files         -n gem-azure-mgmt-analysis-services
%doc README*
%ruby_gemspecdir/azure_mgmt_analysis_services-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_analysis_services-0.17.2

%files         -n gem-azure-mgmt-analysis-services-doc
%ruby_gemsdocdir/azure_mgmt_analysis_services-0.17.2

%files         -n gem-azure-mgmt-api-management
%doc README*
%ruby_gemspecdir/azure_mgmt_api_management-0.18.4.gemspec
%ruby_gemslibdir/azure_mgmt_api_management-0.18.4

%files         -n gem-azure-mgmt-api-management-doc
%ruby_gemsdocdir/azure_mgmt_api_management-0.18.4

%files         -n gem-azure-mgmt-container-registry
%doc README*
%ruby_gemspecdir/azure_mgmt_container_registry-0.18.3.gemspec
%ruby_gemslibdir/azure_mgmt_container_registry-0.18.3

%files         -n gem-azure-mgmt-container-registry-doc
%ruby_gemsdocdir/azure_mgmt_container_registry-0.18.3

%files         -n gem-azure-mgmt-consumption
%doc README*
%ruby_gemspecdir/azure_mgmt_consumption-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_consumption-0.18.0

%files         -n gem-azure-mgmt-consumption-doc
%ruby_gemsdocdir/azure_mgmt_consumption-0.18.0

%files         -n gem-azure-mgmt-devtestlabs
%doc README*
%ruby_gemspecdir/azure_mgmt_devtestlabs-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_devtestlabs-0.18.0

%files         -n gem-azure-mgmt-devtestlabs-doc
%ruby_gemsdocdir/azure_mgmt_devtestlabs-0.18.0

%files         -n gem-azure-mgmt-resourcegraph
%doc README*
%ruby_gemspecdir/azure_mgmt_resourcegraph-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_resourcegraph-0.17.1

%files         -n gem-azure-mgmt-resourcegraph-doc
%ruby_gemsdocdir/azure_mgmt_resourcegraph-0.17.1

%files         -n gem-azure-mgmt-network
%doc README*
%ruby_gemspecdir/azure_mgmt_network-0.23.0.gemspec
%ruby_gemslibdir/azure_mgmt_network-0.23.0

%files         -n gem-azure-mgmt-network-doc
%ruby_gemsdocdir/azure_mgmt_network-0.23.0

%files         -n gem-azure-mgmt-serialconsole
%doc README*
%ruby_gemspecdir/azure_mgmt_serialconsole-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_serialconsole-0.17.0

%files         -n gem-azure-mgmt-serialconsole-doc
%ruby_gemsdocdir/azure_mgmt_serialconsole-0.17.0

%files         -n gem-azure-mgmt-locks
%doc README*
%ruby_gemspecdir/azure_mgmt_locks-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_locks-0.17.3

%files         -n gem-azure-mgmt-locks-doc
%ruby_gemsdocdir/azure_mgmt_locks-0.17.3

%files         -n gem-azure-mgmt-service-bus
%doc README*
%ruby_gemspecdir/azure_mgmt_service_bus-0.17.3.gemspec
%ruby_gemslibdir/azure_mgmt_service_bus-0.17.3

%files         -n gem-azure-mgmt-service-bus-doc
%ruby_gemsdocdir/azure_mgmt_service_bus-0.17.3

%files         -n gem-azure-mgmt-migrate
%doc README*
%ruby_gemspecdir/azure_mgmt_migrate-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_migrate-0.17.0

%files         -n gem-azure-mgmt-migrate-doc
%ruby_gemsdocdir/azure_mgmt_migrate-0.17.0

%files         -n gem-azure-mgmt-hdinsight
%doc README*
%ruby_gemspecdir/azure_mgmt_hdinsight-0.17.7.gemspec
%ruby_gemslibdir/azure_mgmt_hdinsight-0.17.7

%files         -n gem-azure-mgmt-hdinsight-doc
%ruby_gemsdocdir/azure_mgmt_hdinsight-0.17.7

%files         -n gem-azure-mgmt-import-export
%doc README*
%ruby_gemspecdir/azure_mgmt_import_export-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_import_export-0.17.0

%files         -n gem-azure-mgmt-import-export-doc
%ruby_gemsdocdir/azure_mgmt_import_export-0.17.0

%files         -n gem-azure-mgmt-appconfiguration
%doc README*
%ruby_gemspecdir/azure_mgmt_appconfiguration-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_appconfiguration-0.17.1

%files         -n gem-azure-mgmt-appconfiguration-doc
%ruby_gemsdocdir/azure_mgmt_appconfiguration-0.17.1

%files         -n gem-azure-mgmt-attestation
%doc README*
%ruby_gemspecdir/azure_mgmt_attestation-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_attestation-0.17.0

%files         -n gem-azure-mgmt-attestation-doc
%ruby_gemsdocdir/azure_mgmt_attestation-0.17.0

%files         -n gem-azure-mgmt-resources
%doc README*
%ruby_gemspecdir/azure_mgmt_resources-0.17.8.gemspec
%ruby_gemslibdir/azure_mgmt_resources-0.17.8

%files         -n gem-azure-mgmt-resources-doc
%ruby_gemsdocdir/azure_mgmt_resources-0.17.8

%files         -n gem-azure-mgmt-mariadb
%doc README*
%ruby_gemspecdir/azure_mgmt_mariadb-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_mariadb-0.17.1

%files         -n gem-azure-mgmt-mariadb-doc
%ruby_gemsdocdir/azure_mgmt_mariadb-0.17.1

%files         -n gem-azure-mgmt-cost-management
%doc README*
%ruby_gemspecdir/azure_mgmt_cost_management-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_cost_management-0.17.0

%files         -n gem-azure-mgmt-cost-management-doc
%ruby_gemsdocdir/azure_mgmt_cost_management-0.17.0

%files         -n gem-azure-mgmt-powerbi-embedded
%doc README*
%ruby_gemspecdir/azure_mgmt_powerbi_embedded-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_powerbi_embedded-0.17.1

%files         -n gem-azure-mgmt-powerbi-embedded-doc
%ruby_gemsdocdir/azure_mgmt_powerbi_embedded-0.17.1

%files         -n gem-azure-mgmt-scheduler
%doc README*
%ruby_gemspecdir/azure_mgmt_scheduler-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_scheduler-0.17.1

%files         -n gem-azure-mgmt-scheduler-doc
%ruby_gemsdocdir/azure_mgmt_scheduler-0.17.1

%files         -n gem-azure-mgmt-operational-insights
%doc README*
%ruby_gemspecdir/azure_mgmt_operational_insights-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_operational_insights-0.17.2

%files         -n gem-azure-mgmt-operational-insights-doc
%ruby_gemsdocdir/azure_mgmt_operational_insights-0.17.2

%files         -n gem-azure-mgmt-authorization
%doc README*
%ruby_gemspecdir/azure_mgmt_authorization-0.18.4.gemspec
%ruby_gemslibdir/azure_mgmt_authorization-0.18.4

%files         -n gem-azure-mgmt-authorization-doc
%ruby_gemsdocdir/azure_mgmt_authorization-0.18.4

%files         -n gem-azure-mgmt-policy
%doc README*
%ruby_gemspecdir/azure_mgmt_policy-0.17.8.gemspec
%ruby_gemslibdir/azure_mgmt_policy-0.17.8

%files         -n gem-azure-mgmt-policy-doc
%ruby_gemsdocdir/azure_mgmt_policy-0.17.8

%files         -n gem-azure-mgmt-portal
%doc README*
%ruby_gemspecdir/azure_mgmt_portal-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_portal-0.17.0

%files         -n gem-azure-mgmt-portal-doc
%ruby_gemsdocdir/azure_mgmt_portal-0.17.0

%files         -n gem-azure-mgmt-logic
%doc README*
%ruby_gemspecdir/azure_mgmt_logic-0.18.1.gemspec
%ruby_gemslibdir/azure_mgmt_logic-0.18.1

%files         -n gem-azure-mgmt-logic-doc
%ruby_gemsdocdir/azure_mgmt_logic-0.18.1

%files         -n gem-azure-mgmt-billing
%doc README*
%ruby_gemspecdir/azure_mgmt_billing-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_billing-0.17.2

%files         -n gem-azure-mgmt-billing-doc
%ruby_gemsdocdir/azure_mgmt_billing-0.17.2

%files         -n gem-azure-mgmt-dns
%doc README*
%ruby_gemspecdir/azure_mgmt_dns-0.17.4.gemspec
%ruby_gemslibdir/azure_mgmt_dns-0.17.4

%files         -n gem-azure-mgmt-dns-doc
%ruby_gemsdocdir/azure_mgmt_dns-0.17.4

%files         -n gem-azure-mgmt-machine-learning
%doc README*
%ruby_gemspecdir/azure_mgmt_machine_learning-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_machine_learning-0.17.2

%files         -n gem-azure-mgmt-machine-learning-doc
%ruby_gemsdocdir/azure_mgmt_machine_learning-0.17.2

%files         -n gem-azure-mgmt-recovery-services-backup
%doc README*
%ruby_gemspecdir/azure_mgmt_recovery_services_backup-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_recovery_services_backup-0.18.0

%files         -n gem-azure-mgmt-recovery-services-backup-doc
%ruby_gemsdocdir/azure_mgmt_recovery_services_backup-0.18.0

%files         -n gem-azure-mgmt-commerce
%doc README*
%ruby_gemspecdir/azure_mgmt_commerce-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_commerce-0.17.1

%files         -n gem-azure-mgmt-commerce-doc
%ruby_gemsdocdir/azure_mgmt_commerce-0.17.1

%files         -n gem-azure-mgmt-datalake-store
%doc README*
%ruby_gemspecdir/azure_mgmt_datalake_store-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_datalake_store-0.17.2

%files         -n gem-azure-mgmt-datalake-store-doc
%ruby_gemsdocdir/azure_mgmt_datalake_store-0.17.2

%files         -n gem-azure-mgmt-datashare
%doc README*
%ruby_gemspecdir/azure_mgmt_datashare-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_datashare-0.17.0

%files         -n gem-azure-mgmt-datashare-doc
%ruby_gemsdocdir/azure_mgmt_datashare-0.17.0

%files         -n gem-azure-mgmt-deployment-manager
%doc README*
%ruby_gemspecdir/azure_mgmt_deployment_manager-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_deployment_manager-0.17.0

%files         -n gem-azure-mgmt-deployment-manager-doc
%ruby_gemsdocdir/azure_mgmt_deployment_manager-0.17.0

%files         -n gem-azure-mgmt-storagesync
%doc README*
%ruby_gemspecdir/azure_mgmt_storagesync-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_storagesync-0.18.0

%files         -n gem-azure-mgmt-storagesync-doc
%ruby_gemsdocdir/azure_mgmt_storagesync-0.18.0

%files         -n gem-azure-mgmt-storagecache
%doc README*
%ruby_gemspecdir/azure_mgmt_storagecache-0.17.1.gemspec
%ruby_gemslibdir/azure_mgmt_storagecache-0.17.1

%files         -n gem-azure-mgmt-storagecache-doc
%ruby_gemsdocdir/azure_mgmt_storagecache-0.17.1

%files         -n gem-azure-mgmt-storage
%doc README*
%ruby_gemspecdir/azure_mgmt_storage-0.19.3.gemspec
%ruby_gemslibdir/azure_mgmt_storage-0.19.3

%files         -n gem-azure-mgmt-storage-doc
%ruby_gemsdocdir/azure_mgmt_storage-0.19.3

%files         -n gem-azure-mgmt-signalr
%doc README*
%ruby_gemspecdir/azure_mgmt_signalr-0.17.4.gemspec
%ruby_gemslibdir/azure_mgmt_signalr-0.17.4

%files         -n gem-azure-mgmt-signalr-doc
%ruby_gemsdocdir/azure_mgmt_signalr-0.17.4

%files         -n gem-azure-mgmt-search
%doc README*
%ruby_gemspecdir/azure_mgmt_search-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_search-0.17.2

%files         -n gem-azure-mgmt-search-doc
%ruby_gemsdocdir/azure_mgmt_search-0.17.2

%files         -n gem-azure-mgmt-compute
%doc README*
%ruby_gemspecdir/azure_mgmt_compute-0.19.0.gemspec
%ruby_gemslibdir/azure_mgmt_compute-0.19.0

%files         -n gem-azure-mgmt-compute-doc
%ruby_gemsdocdir/azure_mgmt_compute-0.19.0

%files         -n gem-azure-mgmt-customer-insights
%doc README*
%ruby_gemspecdir/azure_mgmt_customer_insights-0.17.2.gemspec
%ruby_gemslibdir/azure_mgmt_customer_insights-0.17.2

%files         -n gem-azure-mgmt-customer-insights-doc
%ruby_gemsdocdir/azure_mgmt_customer_insights-0.17.2

%files         -n gem-azure-mgmt-hanaonazure
%doc README*
%ruby_gemspecdir/azure_mgmt_hanaonazure-0.18.0.gemspec
%ruby_gemslibdir/azure_mgmt_hanaonazure-0.18.0

%files         -n gem-azure-mgmt-hanaonazure-doc
%ruby_gemsdocdir/azure_mgmt_hanaonazure-0.18.0

%files         -n gem-azure-mgmt-mysql
%doc README*
%ruby_gemspecdir/azure_mgmt_mysql-0.17.0.gemspec
%ruby_gemslibdir/azure_mgmt_mysql-0.17.0

%files         -n gem-azure-mgmt-mysql-doc
%ruby_gemsdocdir/azure_mgmt_mysql-0.17.0

%files         -n gem-azure-cognitiveservices-contentmoderator
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_contentmoderator-0.17.2.gemspec
%ruby_gemslibdir/azure_cognitiveservices_contentmoderator-0.17.2

%files         -n gem-azure-cognitiveservices-contentmoderator-doc
%ruby_gemsdocdir/azure_cognitiveservices_contentmoderator-0.17.2

%files         -n gem-azure-service-fabric
%doc README*
%ruby_gemspecdir/azure_service_fabric-0.18.0.gemspec
%ruby_gemslibdir/azure_service_fabric-0.18.0

%files         -n gem-azure-service-fabric-doc
%ruby_gemsdocdir/azure_service_fabric-0.18.0

%files         -n gem-azure-cognitiveservices-customimagesearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_customimagesearch-0.17.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_customimagesearch-0.17.1

%files         -n gem-azure-cognitiveservices-customimagesearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_customimagesearch-0.17.1

%files         -n gem-azure-cognitiveservices-anomalydetector
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_anomalydetector-0.17.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_anomalydetector-0.17.0

%files         -n gem-azure-cognitiveservices-anomalydetector-doc
%ruby_gemsdocdir/azure_cognitiveservices_anomalydetector-0.17.0

%files         -n gem-azure-cognitiveservices-luisruntime
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_luisruntime-0.18.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_luisruntime-0.18.0

%files         -n gem-azure-cognitiveservices-luisruntime-doc
%ruby_gemsdocdir/azure_cognitiveservices_luisruntime-0.18.0

%files         -n gem-azure-cognitiveservices-videosearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_videosearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_videosearch-0.18.1

%files         -n gem-azure-cognitiveservices-videosearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_videosearch-0.18.1

%files         -n gem-azure-cognitiveservices-face
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_face-0.19.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_face-0.19.0

%files         -n gem-azure-cognitiveservices-face-doc
%ruby_gemsdocdir/azure_cognitiveservices_face-0.19.0

%files         -n gem-azure-key-vault
%doc README*
%ruby_gemspecdir/azure_key_vault-0.17.3.gemspec
%ruby_gemslibdir/azure_key_vault-0.17.3

%files         -n gem-azure-key-vault-doc
%ruby_gemsdocdir/azure_key_vault-0.17.3

%files         -n gem-azure-cognitiveservices-autosuggest
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_autosuggest-0.17.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_autosuggest-0.17.1

%files         -n gem-azure-cognitiveservices-autosuggest-doc
%ruby_gemsdocdir/azure_cognitiveservices_autosuggest-0.17.1

%files         -n gem-azure-cognitiveservices-customsearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_customsearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_customsearch-0.18.1

%files         -n gem-azure-cognitiveservices-customsearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_customsearch-0.18.1

%files         -n gem-azure-cognitiveservices-entitysearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_entitysearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_entitysearch-0.18.1

%files         -n gem-azure-cognitiveservices-entitysearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_entitysearch-0.18.1

%files         -n gem-azure-graph-rbac
%doc README*
%ruby_gemspecdir/azure_graph_rbac-0.17.1.gemspec
%ruby_gemslibdir/azure_graph_rbac-0.17.1

%files         -n gem-azure-graph-rbac-doc
%ruby_gemsdocdir/azure_graph_rbac-0.17.1

%files         -n gem-azure-cognitiveservices-localsearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_localsearch-0.17.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_localsearch-0.17.1

%files         -n gem-azure-cognitiveservices-localsearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_localsearch-0.17.1

%files         -n gem-azure-cognitiveservices-qnamakerruntime
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_qnamakerruntime-0.17.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_qnamakerruntime-0.17.1

%files         -n gem-azure-cognitiveservices-qnamakerruntime-doc
%ruby_gemsdocdir/azure_cognitiveservices_qnamakerruntime-0.17.1

%files         -n gem-azure-cognitiveservices-websearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_websearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_websearch-0.18.1

%files         -n gem-azure-cognitiveservices-websearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_websearch-0.18.1

%files         -n gem-azure-cognitiveservices-customvisiontraining
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_customvisiontraining-0.17.2.gemspec
%ruby_gemslibdir/azure_cognitiveservices_customvisiontraining-0.17.2

%files         -n gem-azure-cognitiveservices-customvisiontraining-doc
%ruby_gemsdocdir/azure_cognitiveservices_customvisiontraining-0.17.2

%files         -n gem-azure-cognitiveservices-newssearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_newssearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_newssearch-0.18.1

%files         -n gem-azure-cognitiveservices-newssearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_newssearch-0.18.1

%files         -n gem-azure-cognitiveservices-textanalytics
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_textanalytics-0.17.3.gemspec
%ruby_gemslibdir/azure_cognitiveservices_textanalytics-0.17.3

%files         -n gem-azure-cognitiveservices-textanalytics-doc
%ruby_gemsdocdir/azure_cognitiveservices_textanalytics-0.17.3

%files         -n gem-azure-cognitiveservices-spellcheck
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_spellcheck-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_spellcheck-0.18.1

%files         -n gem-azure-cognitiveservices-spellcheck-doc
%ruby_gemsdocdir/azure_cognitiveservices_spellcheck-0.18.1

%files         -n gem-azure-cognitiveservices-luisauthoring
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_luisauthoring-0.18.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_luisauthoring-0.18.0

%files         -n gem-azure-cognitiveservices-luisauthoring-doc
%ruby_gemsdocdir/azure_cognitiveservices_luisauthoring-0.18.0

%files         -n gem-azure-event-grid
%doc README*
%ruby_gemspecdir/azure_event_grid-0.18.0.gemspec
%ruby_gemslibdir/azure_event_grid-0.18.0

%files         -n gem-azure-event-grid-doc
%ruby_gemsdocdir/azure_event_grid-0.18.0

%files         -n gem-azure-cognitiveservices-computervision
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_computervision-0.20.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_computervision-0.20.1

%files         -n gem-azure-cognitiveservices-computervision-doc
%ruby_gemsdocdir/azure_cognitiveservices_computervision-0.20.1

%files         -n gem-azure-cognitiveservices-qnamaker
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_qnamaker-0.18.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_qnamaker-0.18.0

%files         -n gem-azure-cognitiveservices-qnamaker-doc
%ruby_gemsdocdir/azure_cognitiveservices_qnamaker-0.18.0

%files         -n gem-azure-cognitiveservices-personalizer
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_personalizer-0.17.0.gemspec
%ruby_gemslibdir/azure_cognitiveservices_personalizer-0.17.0

%files         -n gem-azure-cognitiveservices-personalizer-doc
%ruby_gemsdocdir/azure_cognitiveservices_personalizer-0.17.0

%files         -n gem-azure-cognitiveservices-customvisionprediction
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_customvisionprediction-0.17.2.gemspec
%ruby_gemslibdir/azure_cognitiveservices_customvisionprediction-0.17.2

%files         -n gem-azure-cognitiveservices-customvisionprediction-doc
%ruby_gemsdocdir/azure_cognitiveservices_customvisionprediction-0.17.2

%files         -n gem-azure-cognitiveservices-visualsearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_visualsearch-0.18.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_visualsearch-0.18.1

%files         -n gem-azure-cognitiveservices-visualsearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_visualsearch-0.18.1

%files         -n gem-azure-cognitiveservices-formrecognizer
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_formrecognizer-0.17.1.gemspec
%ruby_gemslibdir/azure_cognitiveservices_formrecognizer-0.17.1

%files         -n gem-azure-cognitiveservices-formrecognizer-doc
%ruby_gemsdocdir/azure_cognitiveservices_formrecognizer-0.17.1

%files         -n gem-azure-cognitiveservices-imagesearch
%doc README*
%ruby_gemspecdir/azure_cognitiveservices_imagesearch-0.18.2.gemspec
%ruby_gemslibdir/azure_cognitiveservices_imagesearch-0.18.2

%files         -n gem-azure-cognitiveservices-imagesearch-doc
%ruby_gemsdocdir/azure_cognitiveservices_imagesearch-0.18.2

%files         -n gem-ms-rest-azure
%doc README*
%ruby_gemspecdir/ms_rest_azure-0.11.2.gemspec
%ruby_gemslibdir/ms_rest_azure-0.11.2

%files         -n gem-ms-rest-azure-doc
%ruby_gemsdocdir/ms_rest_azure-0.11.2

%files         -n gem-ms-rest
%doc README*
%ruby_gemspecdir/ms_rest-0.7.6.gemspec
%ruby_gemslibdir/ms_rest-0.7.6

%files         -n gem-ms-rest-doc
%ruby_gemsdocdir/ms_rest-0.7.6

%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 20200316-alt1.2
- ^ 20190809 -> 20200316
- ! spec tags and syntax

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 20190809-alt1.1
- ! spec according to changelog rules

* Tue Aug 13 2019 Pavel Skrylev <majioa@altlinux.org> 20190809-alt1
- + packaged gem with usage Ruby Policy 2.0
