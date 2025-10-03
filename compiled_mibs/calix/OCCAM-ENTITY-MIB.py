# SNMP MIB module (OCCAM-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:22 2025
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

(occamGenericHardwareModules,) = mibBuilder.importSymbols(
    "OCCAM-REG-MODULE",
    "occamGenericHardwareModules")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

entityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    entityMIB.setRevisions(
        ("2009-09-10 00:00",
         "2007-10-02 00:00",
         "2007-09-20 00:00",
         "1999-12-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysicalIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_EntityMIBObjects_ObjectIdentity = ObjectIdentity
entityMIBObjects = _EntityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1)
)
_EntityCompanyName_Type = SnmpAdminString
_EntityCompanyName_Object = MibScalar
entityCompanyName = _EntityCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 1),
    _EntityCompanyName_Type()
)
entityCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityCompanyName.setStatus("current")
_EntityMacAddress_Type = MacAddress
_EntityMacAddress_Object = MibScalar
entityMacAddress = _EntityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 2),
    _EntityMacAddress_Type()
)
entityMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityMacAddress.setStatus("current")
_EntityBoardName_Type = SnmpAdminString
_EntityBoardName_Object = MibScalar
entityBoardName = _EntityBoardName_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 3),
    _EntityBoardName_Type()
)
entityBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityBoardName.setStatus("current")
_EntityBoardAssembly_Type = SnmpAdminString
_EntityBoardAssembly_Object = MibScalar
entityBoardAssembly = _EntityBoardAssembly_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 4),
    _EntityBoardAssembly_Type()
)
entityBoardAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityBoardAssembly.setStatus("current")
_EntityBoardType_Type = SnmpAdminString
_EntityBoardType_Object = MibScalar
entityBoardType = _EntityBoardType_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 5),
    _EntityBoardType_Type()
)
entityBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityBoardType.setStatus("current")


class _EntitySerialNum_Type(SnmpAdminString):
    """Custom type entitySerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EntitySerialNum_Type.__name__ = "SnmpAdminString"
_EntitySerialNum_Object = MibScalar
entitySerialNum = _EntitySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 6),
    _EntitySerialNum_Type()
)
entitySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entitySerialNum.setStatus("current")
_EntityHardwareRev_Type = SnmpAdminString
_EntityHardwareRev_Object = MibScalar
entityHardwareRev = _EntityHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 7),
    _EntityHardwareRev_Type()
)
entityHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityHardwareRev.setStatus("current")
_EntityFirmwareRev_Type = SnmpAdminString
_EntityFirmwareRev_Object = MibScalar
entityFirmwareRev = _EntityFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 8),
    _EntityFirmwareRev_Type()
)
entityFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityFirmwareRev.setStatus("current")
_EntitySoftwareRev_Type = SnmpAdminString
_EntitySoftwareRev_Object = MibScalar
entitySoftwareRev = _EntitySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 9),
    _EntitySoftwareRev_Type()
)
entitySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entitySoftwareRev.setStatus("current")
_EntityMfgDate_Type = SnmpAdminString
_EntityMfgDate_Object = MibScalar
entityMfgDate = _EntityMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 10),
    _EntityMfgDate_Type()
)
entityMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityMfgDate.setStatus("current")
_EntityPortTable_Object = MibTable
entityPortTable = _EntityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    entityPortTable.setStatus("current")
_EntityPortEntry_Object = MibTableRow
entityPortEntry = _EntityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11, 1)
)
entityPortEntry.setIndexNames(
    (0, "OCCAM-ENTITY-MIB", "entityPortShelfIndex"),
    (0, "OCCAM-ENTITY-MIB", "entityPortSlotIndex"),
    (0, "OCCAM-ENTITY-MIB", "entityPortIndex"),
)
if mibBuilder.loadTexts:
    entityPortEntry.setStatus("current")
_EntityPortShelfIndex_Type = PhysicalIndex
_EntityPortShelfIndex_Object = MibTableColumn
entityPortShelfIndex = _EntityPortShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11, 1, 1),
    _EntityPortShelfIndex_Type()
)
entityPortShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortShelfIndex.setStatus("current")
_EntityPortSlotIndex_Type = PhysicalIndex
_EntityPortSlotIndex_Object = MibTableColumn
entityPortSlotIndex = _EntityPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11, 1, 2),
    _EntityPortSlotIndex_Type()
)
entityPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortSlotIndex.setStatus("current")
_EntityPortIndex_Type = PhysicalIndex
_EntityPortIndex_Object = MibTableColumn
entityPortIndex = _EntityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11, 1, 3),
    _EntityPortIndex_Type()
)
entityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortIndex.setStatus("current")
_EntityPortName_Type = SnmpAdminString
_EntityPortName_Object = MibTableColumn
entityPortName = _EntityPortName_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 11, 1, 4),
    _EntityPortName_Type()
)
entityPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortName.setStatus("current")
_EntitySoftwareRevExt_Type = SnmpAdminString
_EntitySoftwareRevExt_Object = MibScalar
entitySoftwareRevExt = _EntitySoftwareRevExt_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 13),
    _EntitySoftwareRevExt_Type()
)
entitySoftwareRevExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entitySoftwareRevExt.setStatus("current")
_EntityOntSlotId_Type = SnmpAdminString
_EntityOntSlotId_Object = MibScalar
entityOntSlotId = _EntityOntSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 1, 14),
    _EntityOntSlotId_Type()
)
entityOntSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityOntSlotId.setStatus("current")
_EntityMIBTraps_ObjectIdentity = ObjectIdentity
entityMIBTraps = _EntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 2)
)
_EntityMIBConformance_ObjectIdentity = ObjectIdentity
entityMIBConformance = _EntityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3)
)
_EntityMIBGroups_ObjectIdentity = ObjectIdentity
entityMIBGroups = _EntityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 1)
)
_EntityMIBObjGroups_ObjectIdentity = ObjectIdentity
entityMIBObjGroups = _EntityMIBObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 1, 1)
)
_EntityMIBEventGroups_ObjectIdentity = ObjectIdentity
entityMIBEventGroups = _EntityMIBEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 1, 2)
)
_EntityMIBCompliances_ObjectIdentity = ObjectIdentity
entityMIBCompliances = _EntityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 2)
)

# Managed Objects groups

entityPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 1, 1, 1)
)
entityPhysicalGroup.setObjects(
      *(("OCCAM-ENTITY-MIB", "entityCompanyName"),
        ("OCCAM-ENTITY-MIB", "entityMacAddress"),
        ("OCCAM-ENTITY-MIB", "entityBoardName"),
        ("OCCAM-ENTITY-MIB", "entityBoardAssembly"),
        ("OCCAM-ENTITY-MIB", "entityBoardType"),
        ("OCCAM-ENTITY-MIB", "entitySerialNum"),
        ("OCCAM-ENTITY-MIB", "entityHardwareRev"),
        ("OCCAM-ENTITY-MIB", "entityFirmwareRev"),
        ("OCCAM-ENTITY-MIB", "entitySoftwareRev"),
        ("OCCAM-ENTITY-MIB", "entityMfgDate"))
)
if mibBuilder.loadTexts:
    entityPhysicalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 1, 3, 2, 1)
)
entityCompliance.setObjects(
    ("OCCAM-ENTITY-MIB", "entityPhysicalGroup")
)
if mibBuilder.loadTexts:
    entityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-ENTITY-MIB",
    **{"PhysicalIndex": PhysicalIndex,
       "org": org,
       "dod": dod,
       "internet": internet,
       "mgmt": mgmt,
       "entityMIB": entityMIB,
       "entityMIBObjects": entityMIBObjects,
       "entityCompanyName": entityCompanyName,
       "entityMacAddress": entityMacAddress,
       "entityBoardName": entityBoardName,
       "entityBoardAssembly": entityBoardAssembly,
       "entityBoardType": entityBoardType,
       "entitySerialNum": entitySerialNum,
       "entityHardwareRev": entityHardwareRev,
       "entityFirmwareRev": entityFirmwareRev,
       "entitySoftwareRev": entitySoftwareRev,
       "entityMfgDate": entityMfgDate,
       "entityPortTable": entityPortTable,
       "entityPortEntry": entityPortEntry,
       "entityPortShelfIndex": entityPortShelfIndex,
       "entityPortSlotIndex": entityPortSlotIndex,
       "entityPortIndex": entityPortIndex,
       "entityPortName": entityPortName,
       "entitySoftwareRevExt": entitySoftwareRevExt,
       "entityOntSlotId": entityOntSlotId,
       "entityMIBTraps": entityMIBTraps,
       "entityMIBConformance": entityMIBConformance,
       "entityMIBGroups": entityMIBGroups,
       "entityMIBObjGroups": entityMIBObjGroups,
       "entityPhysicalGroup": entityPhysicalGroup,
       "entityMIBEventGroups": entityMIBEventGroups,
       "entityMIBCompliances": entityMIBCompliances,
       "entityCompliance": entityCompliance}
)
