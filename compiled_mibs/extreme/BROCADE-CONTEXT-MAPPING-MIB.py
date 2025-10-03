# SNMP MIB module (BROCADE-CONTEXT-MAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-CONTEXT-MAPPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:10 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

brocadeContextMappingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7)
)
if mibBuilder.loadTexts:
    brocadeContextMappingMIB.setRevisions(
        ("2018-05-29 12:00",
         "2015-06-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BContextMapMIBNotifs_ObjectIdentity = ObjectIdentity
bContextMapMIBNotifs = _BContextMapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 0)
)
_BContextMapMIBObjects_ObjectIdentity = ObjectIdentity
bContextMapMIBObjects = _BContextMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1)
)
_BcmContexMapConfig_ObjectIdentity = ObjectIdentity
bcmContexMapConfig = _BcmContexMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1)
)
_BcmContextMappingTable_Object = MibTable
bcmContextMappingTable = _BcmContextMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bcmContextMappingTable.setStatus("current")
_BcmContextMappingEntry_Object = MibTableRow
bcmContextMappingEntry = _BcmContextMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1)
)
bcmContextMappingEntry.setIndexNames(
    (0, "BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingVacmContextName"),
)
if mibBuilder.loadTexts:
    bcmContextMappingEntry.setStatus("current")


class _BcmContextMappingVacmContextName_Type(SnmpAdminString):
    """Custom type bcmContextMappingVacmContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcmContextMappingVacmContextName_Type.__name__ = "SnmpAdminString"
_BcmContextMappingVacmContextName_Object = MibTableColumn
bcmContextMappingVacmContextName = _BcmContextMappingVacmContextName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 1),
    _BcmContextMappingVacmContextName_Type()
)
bcmContextMappingVacmContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcmContextMappingVacmContextName.setStatus("current")


class _BcmContextMappingVrfName_Type(SnmpAdminString):
    """Custom type bcmContextMappingVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcmContextMappingVrfName_Type.__name__ = "SnmpAdminString"
_BcmContextMappingVrfName_Object = MibTableColumn
bcmContextMappingVrfName = _BcmContextMappingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 2),
    _BcmContextMappingVrfName_Type()
)
bcmContextMappingVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmContextMappingVrfName.setStatus("current")


class _BcmContextMappingStorageType_Type(StorageType):
    """Custom type bcmContextMappingStorageType based on StorageType"""
    defaultValue = 3


_BcmContextMappingStorageType_Type.__name__ = "StorageType"
_BcmContextMappingStorageType_Object = MibTableColumn
bcmContextMappingStorageType = _BcmContextMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 3),
    _BcmContextMappingStorageType_Type()
)
bcmContextMappingStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmContextMappingStorageType.setStatus("current")
_BcmContextMappingRowStatus_Type = RowStatus
_BcmContextMappingRowStatus_Object = MibTableColumn
bcmContextMappingRowStatus = _BcmContextMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 4),
    _BcmContextMappingRowStatus_Type()
)
bcmContextMappingRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmContextMappingRowStatus.setStatus("current")
_BContextMapMIBConform_ObjectIdentity = ObjectIdentity
bContextMapMIBConform = _BContextMapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2)
)
_BrocadeContextMapMIBCompliances_ObjectIdentity = ObjectIdentity
brocadeContextMapMIBCompliances = _BrocadeContextMapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 1)
)
_BrocadeContextMapMIBGroups_ObjectIdentity = ObjectIdentity
brocadeContextMapMIBGroups = _BrocadeContextMapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 2)
)

# Managed Objects groups

brocadeContextMapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 2, 1)
)
brocadeContextMapConfigGroup.setObjects(
      *(("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingVrfName"),
        ("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingStorageType"),
        ("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingRowStatus"))
)
if mibBuilder.loadTexts:
    brocadeContextMapConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

brocadeContextMapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 1, 1)
)
brocadeContextMapMIBCompliance.setObjects(
    ("BROCADE-CONTEXT-MAPPING-MIB", "brocadeContextMapConfigGroup")
)
if mibBuilder.loadTexts:
    brocadeContextMapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-CONTEXT-MAPPING-MIB",
    **{"brocadeContextMappingMIB": brocadeContextMappingMIB,
       "bContextMapMIBNotifs": bContextMapMIBNotifs,
       "bContextMapMIBObjects": bContextMapMIBObjects,
       "bcmContexMapConfig": bcmContexMapConfig,
       "bcmContextMappingTable": bcmContextMappingTable,
       "bcmContextMappingEntry": bcmContextMappingEntry,
       "bcmContextMappingVacmContextName": bcmContextMappingVacmContextName,
       "bcmContextMappingVrfName": bcmContextMappingVrfName,
       "bcmContextMappingStorageType": bcmContextMappingStorageType,
       "bcmContextMappingRowStatus": bcmContextMappingRowStatus,
       "bContextMapMIBConform": bContextMapMIBConform,
       "brocadeContextMapMIBCompliances": brocadeContextMapMIBCompliances,
       "brocadeContextMapMIBCompliance": brocadeContextMapMIBCompliance,
       "brocadeContextMapMIBGroups": brocadeContextMapMIBGroups,
       "brocadeContextMapConfigGroup": brocadeContextMapConfigGroup}
)
