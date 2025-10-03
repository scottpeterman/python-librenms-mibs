# SNMP MIB module (PK-SOFTWARE-APPLIANCE-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\primekey\PK-SOFTWARE-APPLIANCE-V2
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:57 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

primekey = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22408)
)
if mibBuilder.loadTexts:
    primekey.setRevisions(
        ("2022-05-16 00:00",
         "2021-07-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrimeKeyProducts_ObjectIdentity = ObjectIdentity
primeKeyProducts = _PrimeKeyProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1)
)
_PrimeKeySoftwareApplianceSubTree_ObjectIdentity = ObjectIdentity
primeKeySoftwareApplianceSubTree = _PrimeKeySoftwareApplianceSubTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4)
)
_Pk_Software_Appliance_V2_ObjectIdentity = ObjectIdentity
pk_Software_Appliance_V2 = _Pk_Software_Appliance_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1)
)
_Pk_SAV2_component_readyness_ObjectIdentity = ObjectIdentity
pk_SAV2_component_readyness = _Pk_SAV2_component_readyness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1)
)
_Pk_SAV2_authentication_service_status_Type = Integer32
_Pk_SAV2_authentication_service_status_Object = MibScalar
pk_SAV2_authentication_service_status = _Pk_SAV2_authentication_service_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 1),
    _Pk_SAV2_authentication_service_status_Type()
)
pk_SAV2_authentication_service_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_authentication_service_status.setStatus("current")
_Pk_SAV2_crs_status_Type = Integer32
_Pk_SAV2_crs_status_Object = MibScalar
pk_SAV2_crs_status = _Pk_SAV2_crs_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 2),
    _Pk_SAV2_crs_status_Type()
)
pk_SAV2_crs_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_crs_status.setStatus("current")
_Pk_SAV2_documentation_status_Type = Integer32
_Pk_SAV2_documentation_status_Object = MibScalar
pk_SAV2_documentation_status = _Pk_SAV2_documentation_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 3),
    _Pk_SAV2_documentation_status_Type()
)
pk_SAV2_documentation_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_documentation_status.setStatus("current")
_Pk_SAV2_monitoring_status_Type = Integer32
_Pk_SAV2_monitoring_status_Object = MibScalar
pk_SAV2_monitoring_status = _Pk_SAV2_monitoring_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 4),
    _Pk_SAV2_monitoring_status_Type()
)
pk_SAV2_monitoring_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_monitoring_status.setStatus("current")
_Pk_SAV2_persistence_status_Type = Integer32
_Pk_SAV2_persistence_status_Object = MibScalar
pk_SAV2_persistence_status = _Pk_SAV2_persistence_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 5),
    _Pk_SAV2_persistence_status_Type()
)
pk_SAV2_persistence_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_persistence_status.setStatus("current")
_Pk_SAV2_snmp_status_Type = Integer32
_Pk_SAV2_snmp_status_Object = MibScalar
pk_SAV2_snmp_status = _Pk_SAV2_snmp_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 6),
    _Pk_SAV2_snmp_status_Type()
)
pk_SAV2_snmp_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_snmp_status.setStatus("current")
_Pk_SAV2_spc_status_Type = Integer32
_Pk_SAV2_spc_status_Object = MibScalar
pk_SAV2_spc_status = _Pk_SAV2_spc_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 7),
    _Pk_SAV2_spc_status_Type()
)
pk_SAV2_spc_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_spc_status.setStatus("current")
_Pk_SAV2_vs_status_Type = Integer32
_Pk_SAV2_vs_status_Object = MibScalar
pk_SAV2_vs_status = _Pk_SAV2_vs_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 8),
    _Pk_SAV2_vs_status_Type()
)
pk_SAV2_vs_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_vs_status.setStatus("current")
_Pk_SAV2_vsapi_status_Type = Integer32
_Pk_SAV2_vsapi_status_Object = MibScalar
pk_SAV2_vsapi_status = _Pk_SAV2_vsapi_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 9),
    _Pk_SAV2_vsapi_status_Type()
)
pk_SAV2_vsapi_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_vsapi_status.setStatus("current")
_Pk_SAV2_webconf_status_Type = Integer32
_Pk_SAV2_webconf_status_Object = MibScalar
pk_SAV2_webconf_status = _Pk_SAV2_webconf_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 10),
    _Pk_SAV2_webconf_status_Type()
)
pk_SAV2_webconf_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_webconf_status.setStatus("current")
_Pk_SAV2_vault_status_Type = Integer32
_Pk_SAV2_vault_status_Object = MibScalar
pk_SAV2_vault_status = _Pk_SAV2_vault_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 1, 11),
    _Pk_SAV2_vault_status_Type()
)
pk_SAV2_vault_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_vault_status.setStatus("current")
_Pk_SAV2_network_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_network_subtree = _Pk_SAV2_network_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2)
)
_Pk_SAV2_networkLink_status_Type = Integer32
_Pk_SAV2_networkLink_status_Object = MibScalar
pk_SAV2_networkLink_status = _Pk_SAV2_networkLink_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 1),
    _Pk_SAV2_networkLink_status_Type()
)
pk_SAV2_networkLink_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_networkLink_status.setStatus("current")
_Pk_SAV2_networkIpv4_Type = OctetString
_Pk_SAV2_networkIpv4_Object = MibScalar
pk_SAV2_networkIpv4 = _Pk_SAV2_networkIpv4_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 2),
    _Pk_SAV2_networkIpv4_Type()
)
pk_SAV2_networkIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_networkIpv4.setStatus("current")
_Pk_SAV2_networkIpv4Prefix_Type = Integer32
_Pk_SAV2_networkIpv4Prefix_Object = MibScalar
pk_SAV2_networkIpv4Prefix = _Pk_SAV2_networkIpv4Prefix_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 3),
    _Pk_SAV2_networkIpv4Prefix_Type()
)
pk_SAV2_networkIpv4Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_networkIpv4Prefix.setStatus("current")
_Pk_SAV2_networkIpv6_Type = OctetString
_Pk_SAV2_networkIpv6_Object = MibScalar
pk_SAV2_networkIpv6 = _Pk_SAV2_networkIpv6_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 4),
    _Pk_SAV2_networkIpv6_Type()
)
pk_SAV2_networkIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_networkIpv6.setStatus("current")
_Pk_SAV2_networkIpv6Prefix_Type = Integer32
_Pk_SAV2_networkIpv6Prefix_Object = MibScalar
pk_SAV2_networkIpv6Prefix = _Pk_SAV2_networkIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 5),
    _Pk_SAV2_networkIpv6Prefix_Type()
)
pk_SAV2_networkIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_networkIpv6Prefix.setStatus("current")
_Pk_SAV2_systemHostname_Type = OctetString
_Pk_SAV2_systemHostname_Object = MibScalar
pk_SAV2_systemHostname = _Pk_SAV2_systemHostname_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 2, 6),
    _Pk_SAV2_systemHostname_Type()
)
pk_SAV2_systemHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_systemHostname.setStatus("current")
_Pk_SAV2_database_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_database_subtree = _Pk_SAV2_database_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3)
)
_Pk_SAV2_internal_database_ObjectIdentity = ObjectIdentity
pk_SAV2_internal_database = _Pk_SAV2_internal_database_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3, 1)
)
_Pk_SAV2_internal_database_status_Type = Integer32
_Pk_SAV2_internal_database_status_Object = MibScalar
pk_SAV2_internal_database_status = _Pk_SAV2_internal_database_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3, 1, 1),
    _Pk_SAV2_internal_database_status_Type()
)
pk_SAV2_internal_database_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_internal_database_status.setStatus("current")
_Pk_SAV2_internal_databaseAvailableStorage_Type = Integer32
_Pk_SAV2_internal_databaseAvailableStorage_Object = MibScalar
pk_SAV2_internal_databaseAvailableStorage = _Pk_SAV2_internal_databaseAvailableStorage_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3, 1, 2),
    _Pk_SAV2_internal_databaseAvailableStorage_Type()
)
pk_SAV2_internal_databaseAvailableStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_internal_databaseAvailableStorage.setStatus("current")
_Pk_SAV2_internal_databaseTotalStorage_Type = Integer32
_Pk_SAV2_internal_databaseTotalStorage_Object = MibScalar
pk_SAV2_internal_databaseTotalStorage = _Pk_SAV2_internal_databaseTotalStorage_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3, 1, 3),
    _Pk_SAV2_internal_databaseTotalStorage_Type()
)
pk_SAV2_internal_databaseTotalStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_internal_databaseTotalStorage.setStatus("current")
_Pk_SAV2_internal_databaseUsage_Type = Integer32
_Pk_SAV2_internal_databaseUsage_Object = MibScalar
pk_SAV2_internal_databaseUsage = _Pk_SAV2_internal_databaseUsage_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 3, 1, 4),
    _Pk_SAV2_internal_databaseUsage_Type()
)
pk_SAV2_internal_databaseUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_internal_databaseUsage.setStatus("current")
_Pk_SAV2_version_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_version_subtree = _Pk_SAV2_version_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 4)
)
_Pk_SAV2_systemVersion_Type = OctetString
_Pk_SAV2_systemVersion_Object = MibScalar
pk_SAV2_systemVersion = _Pk_SAV2_systemVersion_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 4, 1),
    _Pk_SAV2_systemVersion_Type()
)
pk_SAV2_systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_systemVersion.setStatus("current")
_Pk_SAV2_application_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_application_subtree = _Pk_SAV2_application_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5)
)
_Pk_SAV2_ejbca_ObjectIdentity = ObjectIdentity
pk_SAV2_ejbca = _Pk_SAV2_ejbca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 1)
)
_Pk_SAV2_ejbca_status_Type = Integer32
_Pk_SAV2_ejbca_status_Object = MibScalar
pk_SAV2_ejbca_status = _Pk_SAV2_ejbca_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 1, 1),
    _Pk_SAV2_ejbca_status_Type()
)
pk_SAV2_ejbca_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_ejbca_status.setStatus("current")
_Pk_SAV2_ejbcaVersion_Type = OctetString
_Pk_SAV2_ejbcaVersion_Object = MibScalar
pk_SAV2_ejbcaVersion = _Pk_SAV2_ejbcaVersion_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 1, 2),
    _Pk_SAV2_ejbcaVersion_Type()
)
pk_SAV2_ejbcaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_ejbcaVersion.setStatus("current")
_Pk_SAV2_ejbcaHealthCheck_Type = Integer32
_Pk_SAV2_ejbcaHealthCheck_Object = MibScalar
pk_SAV2_ejbcaHealthCheck = _Pk_SAV2_ejbcaHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 1, 3),
    _Pk_SAV2_ejbcaHealthCheck_Type()
)
pk_SAV2_ejbcaHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_ejbcaHealthCheck.setStatus("current")
_Pk_SAV2_signserver_ObjectIdentity = ObjectIdentity
pk_SAV2_signserver = _Pk_SAV2_signserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 2)
)
_Pk_SAV2_signserver_status_Type = Integer32
_Pk_SAV2_signserver_status_Object = MibScalar
pk_SAV2_signserver_status = _Pk_SAV2_signserver_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 2, 1),
    _Pk_SAV2_signserver_status_Type()
)
pk_SAV2_signserver_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_signserver_status.setStatus("current")
_Pk_SAV2_signserverVersion_Type = OctetString
_Pk_SAV2_signserverVersion_Object = MibScalar
pk_SAV2_signserverVersion = _Pk_SAV2_signserverVersion_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 2, 2),
    _Pk_SAV2_signserverVersion_Type()
)
pk_SAV2_signserverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_signserverVersion.setStatus("current")
_Pk_SAV2_signserverHealthCheck_Type = Integer32
_Pk_SAV2_signserverHealthCheck_Object = MibScalar
pk_SAV2_signserverHealthCheck = _Pk_SAV2_signserverHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 5, 2, 3),
    _Pk_SAV2_signserverHealthCheck_Type()
)
pk_SAV2_signserverHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_signserverHealthCheck.setStatus("current")
_Pk_SAV2_hsm_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_hsm_subtree = _Pk_SAV2_hsm_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6)
)
_Pk_SAV2_hsm_driver_softhsm_status_Type = Integer32
_Pk_SAV2_hsm_driver_softhsm_status_Object = MibScalar
pk_SAV2_hsm_driver_softhsm_status = _Pk_SAV2_hsm_driver_softhsm_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 1),
    _Pk_SAV2_hsm_driver_softhsm_status_Type()
)
pk_SAV2_hsm_driver_softhsm_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_softhsm_status.setStatus("current")
_Pk_SAV2_hsm_driver_luna7_status_Type = Integer32
_Pk_SAV2_hsm_driver_luna7_status_Object = MibScalar
pk_SAV2_hsm_driver_luna7_status = _Pk_SAV2_hsm_driver_luna7_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 2),
    _Pk_SAV2_hsm_driver_luna7_status_Type()
)
pk_SAV2_hsm_driver_luna7_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_luna7_status.setStatus("current")
_Pk_SAV2_hsm_utimaco_subtree_ObjectIdentity = ObjectIdentity
pk_SAV2_hsm_utimaco_subtree = _Pk_SAV2_hsm_utimaco_subtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3)
)
_Pk_SAV2_hsm_driver_utimaco_status_Type = Integer32
_Pk_SAV2_hsm_driver_utimaco_status_Object = MibScalar
pk_SAV2_hsm_driver_utimaco_status = _Pk_SAV2_hsm_driver_utimaco_status_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3, 1),
    _Pk_SAV2_hsm_driver_utimaco_status_Type()
)
pk_SAV2_hsm_driver_utimaco_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_utimaco_status.setStatus("current")
_Pk_SAV2_hsm_driver_utimaco_serialNumber_Type = OctetString
_Pk_SAV2_hsm_driver_utimaco_serialNumber_Object = MibScalar
pk_SAV2_hsm_driver_utimaco_serialNumber = _Pk_SAV2_hsm_driver_utimaco_serialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3, 2),
    _Pk_SAV2_hsm_driver_utimaco_serialNumber_Type()
)
pk_SAV2_hsm_driver_utimaco_serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_utimaco_serialNumber.setStatus("current")
_Pk_SAV2_hsm_driver_utimaco_model_Type = OctetString
_Pk_SAV2_hsm_driver_utimaco_model_Object = MibScalar
pk_SAV2_hsm_driver_utimaco_model = _Pk_SAV2_hsm_driver_utimaco_model_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3, 3),
    _Pk_SAV2_hsm_driver_utimaco_model_Type()
)
pk_SAV2_hsm_driver_utimaco_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_utimaco_model.setStatus("current")
_Pk_SAV2_hsm_driver_utimaco_state_Type = OctetString
_Pk_SAV2_hsm_driver_utimaco_state_Object = MibScalar
pk_SAV2_hsm_driver_utimaco_state = _Pk_SAV2_hsm_driver_utimaco_state_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3, 4),
    _Pk_SAV2_hsm_driver_utimaco_state_Type()
)
pk_SAV2_hsm_driver_utimaco_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_utimaco_state.setStatus("current")
_Pk_SAV2_hsm_driver_utimaco_mode_Type = OctetString
_Pk_SAV2_hsm_driver_utimaco_mode_Object = MibScalar
pk_SAV2_hsm_driver_utimaco_mode = _Pk_SAV2_hsm_driver_utimaco_mode_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 3, 5),
    _Pk_SAV2_hsm_driver_utimaco_mode_Type()
)
pk_SAV2_hsm_driver_utimaco_mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_utimaco_mode.setStatus("current")
_Pk_SAV2_hsm_driver_ncipher_Type = Integer32
_Pk_SAV2_hsm_driver_ncipher_Object = MibScalar
pk_SAV2_hsm_driver_ncipher = _Pk_SAV2_hsm_driver_ncipher_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 4, 1, 6, 4),
    _Pk_SAV2_hsm_driver_ncipher_Type()
)
pk_SAV2_hsm_driver_ncipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pk_SAV2_hsm_driver_ncipher.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PK-SOFTWARE-APPLIANCE-V2",
    **{"primekey": primekey,
       "primeKeyProducts": primeKeyProducts,
       "primeKeySoftwareApplianceSubTree": primeKeySoftwareApplianceSubTree,
       "pk-Software-Appliance-V2": pk_Software_Appliance_V2,
       "pk-SAV2-component-readyness": pk_SAV2_component_readyness,
       "pk-SAV2-authentication-service-status": pk_SAV2_authentication_service_status,
       "pk-SAV2-crs-status": pk_SAV2_crs_status,
       "pk-SAV2-documentation-status": pk_SAV2_documentation_status,
       "pk-SAV2-monitoring-status": pk_SAV2_monitoring_status,
       "pk-SAV2-persistence-status": pk_SAV2_persistence_status,
       "pk-SAV2-snmp-status": pk_SAV2_snmp_status,
       "pk-SAV2-spc-status": pk_SAV2_spc_status,
       "pk-SAV2-vs-status": pk_SAV2_vs_status,
       "pk-SAV2-vsapi-status": pk_SAV2_vsapi_status,
       "pk-SAV2-webconf-status": pk_SAV2_webconf_status,
       "pk-SAV2-vault-status": pk_SAV2_vault_status,
       "pk-SAV2-network-subtree": pk_SAV2_network_subtree,
       "pk-SAV2-networkLink-status": pk_SAV2_networkLink_status,
       "pk-SAV2-networkIpv4": pk_SAV2_networkIpv4,
       "pk-SAV2-networkIpv4Prefix": pk_SAV2_networkIpv4Prefix,
       "pk-SAV2-networkIpv6": pk_SAV2_networkIpv6,
       "pk-SAV2-networkIpv6Prefix": pk_SAV2_networkIpv6Prefix,
       "pk-SAV2-systemHostname": pk_SAV2_systemHostname,
       "pk-SAV2-database-subtree": pk_SAV2_database_subtree,
       "pk-SAV2-internal-database": pk_SAV2_internal_database,
       "pk-SAV2-internal-database-status": pk_SAV2_internal_database_status,
       "pk-SAV2-internal-databaseAvailableStorage": pk_SAV2_internal_databaseAvailableStorage,
       "pk-SAV2-internal-databaseTotalStorage": pk_SAV2_internal_databaseTotalStorage,
       "pk-SAV2-internal-databaseUsage": pk_SAV2_internal_databaseUsage,
       "pk-SAV2-version-subtree": pk_SAV2_version_subtree,
       "pk-SAV2-systemVersion": pk_SAV2_systemVersion,
       "pk-SAV2-application-subtree": pk_SAV2_application_subtree,
       "pk-SAV2-ejbca": pk_SAV2_ejbca,
       "pk-SAV2-ejbca-status": pk_SAV2_ejbca_status,
       "pk-SAV2-ejbcaVersion": pk_SAV2_ejbcaVersion,
       "pk-SAV2-ejbcaHealthCheck": pk_SAV2_ejbcaHealthCheck,
       "pk-SAV2-signserver": pk_SAV2_signserver,
       "pk-SAV2-signserver-status": pk_SAV2_signserver_status,
       "pk-SAV2-signserverVersion": pk_SAV2_signserverVersion,
       "pk-SAV2-signserverHealthCheck": pk_SAV2_signserverHealthCheck,
       "pk-SAV2-hsm-subtree": pk_SAV2_hsm_subtree,
       "pk-SAV2-hsm-driver-softhsm-status": pk_SAV2_hsm_driver_softhsm_status,
       "pk-SAV2-hsm-driver-luna7-status": pk_SAV2_hsm_driver_luna7_status,
       "pk-SAV2-hsm-utimaco-subtree": pk_SAV2_hsm_utimaco_subtree,
       "pk-SAV2-hsm-driver-utimaco-status": pk_SAV2_hsm_driver_utimaco_status,
       "pk-SAV2-hsm-driver-utimaco-serialNumber": pk_SAV2_hsm_driver_utimaco_serialNumber,
       "pk-SAV2-hsm-driver-utimaco-model": pk_SAV2_hsm_driver_utimaco_model,
       "pk-SAV2-hsm-driver-utimaco-state": pk_SAV2_hsm_driver_utimaco_state,
       "pk-SAV2-hsm-driver-utimaco-mode": pk_SAV2_hsm_driver_utimaco_mode,
       "pk-SAV2-hsm-driver-ncipher": pk_SAV2_hsm_driver_ncipher}
)
