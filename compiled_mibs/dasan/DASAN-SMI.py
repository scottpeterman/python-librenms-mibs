# SNMP MIB module (DASAN-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:53 2025
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

dasan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296)
)
if mibBuilder.loadTexts:
    dasan.setRevisions(
        ("1901-04-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanEvents_ObjectIdentity = ObjectIdentity
dasanEvents = _DasanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 0)
)
if mibBuilder.loadTexts:
    dasanEvents.setStatus("current")
_DasanProducts_ObjectIdentity = ObjectIdentity
dasanProducts = _DasanProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1)
)
if mibBuilder.loadTexts:
    dasanProducts.setStatus("current")
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 2)
)
if mibBuilder.loadTexts:
    local.setStatus("current")
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 3)
)
if mibBuilder.loadTexts:
    temporary.setStatus("current")
_Pakmon_ObjectIdentity = ObjectIdentity
pakmon = _Pakmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 4)
)
if mibBuilder.loadTexts:
    pakmon.setStatus("current")
_Workgroup_ObjectIdentity = ObjectIdentity
workgroup = _Workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 5)
)
if mibBuilder.loadTexts:
    workgroup.setStatus("current")
_OtherEnterprises_ObjectIdentity = ObjectIdentity
otherEnterprises = _OtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 6)
)
if mibBuilder.loadTexts:
    otherEnterprises.setStatus("current")
_DsShe_ObjectIdentity = ObjectIdentity
dsShe = _DsShe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 6, 2)
)
_DasanAgentCapability_ObjectIdentity = ObjectIdentity
dasanAgentCapability = _DasanAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 7)
)
if mibBuilder.loadTexts:
    dasanAgentCapability.setStatus("current")
_DasanConfig_ObjectIdentity = ObjectIdentity
dasanConfig = _DasanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 8)
)
if mibBuilder.loadTexts:
    dasanConfig.setStatus("current")
_DasanMgmt_ObjectIdentity = ObjectIdentity
dasanMgmt = _DasanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9)
)
if mibBuilder.loadTexts:
    dasanMgmt.setStatus("current")
_DasanExperiment_ObjectIdentity = ObjectIdentity
dasanExperiment = _DasanExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 10)
)
if mibBuilder.loadTexts:
    dasanExperiment.setStatus("current")
_DasanAdmin_ObjectIdentity = ObjectIdentity
dasanAdmin = _DasanAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 11)
)
if mibBuilder.loadTexts:
    dasanAdmin.setStatus("current")
_DasanModules_ObjectIdentity = ObjectIdentity
dasanModules = _DasanModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 12)
)
if mibBuilder.loadTexts:
    dasanModules.setStatus("current")
_Lightstream_ObjectIdentity = ObjectIdentity
lightstream = _Lightstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 13)
)
if mibBuilder.loadTexts:
    lightstream.setStatus("current")
_Dasanworks_ObjectIdentity = ObjectIdentity
dasanworks = _Dasanworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 14)
)
if mibBuilder.loadTexts:
    dasanworks.setStatus("current")
_Newport_ObjectIdentity = ObjectIdentity
newport = _Newport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 15)
)
if mibBuilder.loadTexts:
    newport.setStatus("current")
_DasanPartnerProducts_ObjectIdentity = ObjectIdentity
dasanPartnerProducts = _DasanPartnerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 16)
)
if mibBuilder.loadTexts:
    dasanPartnerProducts.setStatus("current")
_DasanPolicy_ObjectIdentity = ObjectIdentity
dasanPolicy = _DasanPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 17)
)
if mibBuilder.loadTexts:
    dasanPolicy.setStatus("current")
_SleMgmt_ObjectIdentity = ObjectIdentity
sleMgmt = _SleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101)
)
if mibBuilder.loadTexts:
    sleMgmt.setStatus("current")
_SleV2Mgmt_ObjectIdentity = ObjectIdentity
sleV2Mgmt = _SleV2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102)
)
if mibBuilder.loadTexts:
    sleV2Mgmt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-SMI",
    **{"dasan": dasan,
       "dasanEvents": dasanEvents,
       "dasanProducts": dasanProducts,
       "local": local,
       "temporary": temporary,
       "pakmon": pakmon,
       "workgroup": workgroup,
       "otherEnterprises": otherEnterprises,
       "dsShe": dsShe,
       "dasanAgentCapability": dasanAgentCapability,
       "dasanConfig": dasanConfig,
       "dasanMgmt": dasanMgmt,
       "dasanExperiment": dasanExperiment,
       "dasanAdmin": dasanAdmin,
       "dasanModules": dasanModules,
       "lightstream": lightstream,
       "dasanworks": dasanworks,
       "newport": newport,
       "dasanPartnerProducts": dasanPartnerProducts,
       "dasanPolicy": dasanPolicy,
       "sleMgmt": sleMgmt,
       "sleV2Mgmt": sleV2Mgmt}
)
