# SNMP MIB module (SL-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-ENTITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:48 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slmEntity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysicalIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PhysicalClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("port", 10),
          ("stack", 11))
    )



class PhysicalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              14,
              15,
              16,
              21,
              100)
        )
    )
    namedValues = NamedValues(
        *(("powerModule", 1),
          ("fanModule", 2),
          ("switchModule", 3),
          ("edfaModule", 14),
          ("ocmModule", 15),
          ("otdrModule", 16),
          ("lc400G", 21),
          ("unknown", 100))
    )



class CleiCode(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



# MIB Managed Objects in the order of their OIDs

_SlEntityPhysical_ObjectIdentity = ObjectIdentity
slEntityPhysical = _SlEntityPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1)
)
_SlEntPhysicalTable_Object = MibTable
slEntPhysicalTable = _SlEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    slEntPhysicalTable.setStatus("current")
_SlEntPhysicalEntry_Object = MibTableRow
slEntPhysicalEntry = _SlEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1)
)
slEntPhysicalEntry.setIndexNames(
    (0, "SL-ENTITY-MIB", "slEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    slEntPhysicalEntry.setStatus("current")
_SlEntPhysicalIndex_Type = InterfaceIndex
_SlEntPhysicalIndex_Object = MibTableColumn
slEntPhysicalIndex = _SlEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 1),
    _SlEntPhysicalIndex_Type()
)
slEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalIndex.setStatus("current")
_SlEntPhysicalDescr_Type = SnmpAdminString
_SlEntPhysicalDescr_Object = MibTableColumn
slEntPhysicalDescr = _SlEntPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 2),
    _SlEntPhysicalDescr_Type()
)
slEntPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalDescr.setStatus("current")
_SlEntPhysicalClass_Type = PhysicalClass
_SlEntPhysicalClass_Object = MibTableColumn
slEntPhysicalClass = _SlEntPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 3),
    _SlEntPhysicalClass_Type()
)
slEntPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalClass.setStatus("current")
_SlEntPhysicalHardwareRev_Type = SnmpAdminString
_SlEntPhysicalHardwareRev_Object = MibTableColumn
slEntPhysicalHardwareRev = _SlEntPhysicalHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 4),
    _SlEntPhysicalHardwareRev_Type()
)
slEntPhysicalHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalHardwareRev.setStatus("current")
_SlEntPhysicalFirmwareRev_Type = SnmpAdminString
_SlEntPhysicalFirmwareRev_Object = MibTableColumn
slEntPhysicalFirmwareRev = _SlEntPhysicalFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 5),
    _SlEntPhysicalFirmwareRev_Type()
)
slEntPhysicalFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalFirmwareRev.setStatus("current")
_SlEntPhysicalSoftwareRev_Type = SnmpAdminString
_SlEntPhysicalSoftwareRev_Object = MibTableColumn
slEntPhysicalSoftwareRev = _SlEntPhysicalSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 6),
    _SlEntPhysicalSoftwareRev_Type()
)
slEntPhysicalSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalSoftwareRev.setStatus("current")


class _SlEntPhysicalSerialNum_Type(SnmpAdminString):
    """Custom type slEntPhysicalSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlEntPhysicalSerialNum_Type.__name__ = "SnmpAdminString"
_SlEntPhysicalSerialNum_Object = MibTableColumn
slEntPhysicalSerialNum = _SlEntPhysicalSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 7),
    _SlEntPhysicalSerialNum_Type()
)
slEntPhysicalSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalSerialNum.setStatus("current")
_SlEntPhysicalProtectionEntity_Type = PhysicalIndex
_SlEntPhysicalProtectionEntity_Object = MibTableColumn
slEntPhysicalProtectionEntity = _SlEntPhysicalProtectionEntity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 8),
    _SlEntPhysicalProtectionEntity_Type()
)
slEntPhysicalProtectionEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalProtectionEntity.setStatus("current")


class _SlEntPhysicalProtectState_Type(Integer32):
    """Custom type slEntPhysicalProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protecting", 2),
          ("noProtection", 3))
    )


_SlEntPhysicalProtectState_Type.__name__ = "Integer32"
_SlEntPhysicalProtectState_Object = MibTableColumn
slEntPhysicalProtectState = _SlEntPhysicalProtectState_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 9),
    _SlEntPhysicalProtectState_Type()
)
slEntPhysicalProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalProtectState.setStatus("current")


class _SlEntPhysicalProtectMode_Type(Integer32):
    """Custom type slEntPhysicalProtectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("force", 2),
          ("automatic", 3))
    )


_SlEntPhysicalProtectMode_Type.__name__ = "Integer32"
_SlEntPhysicalProtectMode_Object = MibTableColumn
slEntPhysicalProtectMode = _SlEntPhysicalProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 14),
    _SlEntPhysicalProtectMode_Type()
)
slEntPhysicalProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEntPhysicalProtectMode.setStatus("current")


class _SlEntPhysicalStatus_Type(Integer32):
    """Custom type slEntPhysicalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_SlEntPhysicalStatus_Type.__name__ = "Integer32"
_SlEntPhysicalStatus_Object = MibTableColumn
slEntPhysicalStatus = _SlEntPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 15),
    _SlEntPhysicalStatus_Type()
)
slEntPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalStatus.setStatus("current")
_SlEntPhysicalFailureDescription_Type = SnmpAdminString
_SlEntPhysicalFailureDescription_Object = MibTableColumn
slEntPhysicalFailureDescription = _SlEntPhysicalFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 16),
    _SlEntPhysicalFailureDescription_Type()
)
slEntPhysicalFailureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalFailureDescription.setStatus("current")


class _SlEntPhysicalAdminStatus_Type(Integer32):
    """Custom type slEntPhysicalAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("warmBoot", 4),
          ("coldBoot", 5),
          ("hotBoot", 7))
    )


_SlEntPhysicalAdminStatus_Type.__name__ = "Integer32"
_SlEntPhysicalAdminStatus_Object = MibTableColumn
slEntPhysicalAdminStatus = _SlEntPhysicalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 17),
    _SlEntPhysicalAdminStatus_Type()
)
slEntPhysicalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEntPhysicalAdminStatus.setStatus("current")


class _SlEntPhysicalOperStatus_Type(Integer32):
    """Custom type slEntPhysicalOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("notPresent", 6))
    )


_SlEntPhysicalOperStatus_Type.__name__ = "Integer32"
_SlEntPhysicalOperStatus_Object = MibTableColumn
slEntPhysicalOperStatus = _SlEntPhysicalOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 18),
    _SlEntPhysicalOperStatus_Type()
)
slEntPhysicalOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalOperStatus.setStatus("current")
_SlEntPhysicalSysUptime_Type = TimeTicks
_SlEntPhysicalSysUptime_Object = MibTableColumn
slEntPhysicalSysUptime = _SlEntPhysicalSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 19),
    _SlEntPhysicalSysUptime_Type()
)
slEntPhysicalSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalSysUptime.setStatus("current")
_SlEntPhysicalType_Type = PhysicalType
_SlEntPhysicalType_Object = MibTableColumn
slEntPhysicalType = _SlEntPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 20),
    _SlEntPhysicalType_Type()
)
slEntPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalType.setStatus("current")
_SlEntPhysicalCleiCode_Type = CleiCode
_SlEntPhysicalCleiCode_Object = MibTableColumn
slEntPhysicalCleiCode = _SlEntPhysicalCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 21),
    _SlEntPhysicalCleiCode_Type()
)
slEntPhysicalCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalCleiCode.setStatus("current")


class _SlEntPhysicalPartNumber_Type(SnmpAdminString):
    """Custom type slEntPhysicalPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SlEntPhysicalPartNumber_Type.__name__ = "SnmpAdminString"
_SlEntPhysicalPartNumber_Object = MibTableColumn
slEntPhysicalPartNumber = _SlEntPhysicalPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 22),
    _SlEntPhysicalPartNumber_Type()
)
slEntPhysicalPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalPartNumber.setStatus("current")


class _SlEntPhysicalOemSerialNum_Type(SnmpAdminString):
    """Custom type slEntPhysicalOemSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlEntPhysicalOemSerialNum_Type.__name__ = "SnmpAdminString"
_SlEntPhysicalOemSerialNum_Object = MibTableColumn
slEntPhysicalOemSerialNum = _SlEntPhysicalOemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 23),
    _SlEntPhysicalOemSerialNum_Type()
)
slEntPhysicalOemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalOemSerialNum.setStatus("current")
_SlEntPhysicalProductionDate_Type = SnmpAdminString
_SlEntPhysicalProductionDate_Object = MibTableColumn
slEntPhysicalProductionDate = _SlEntPhysicalProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 24),
    _SlEntPhysicalProductionDate_Type()
)
slEntPhysicalProductionDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEntPhysicalProductionDate.setStatus("current")
_SlEntPhysicalSysTemp_Type = Integer32
_SlEntPhysicalSysTemp_Object = MibTableColumn
slEntPhysicalSysTemp = _SlEntPhysicalSysTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 25),
    _SlEntPhysicalSysTemp_Type()
)
slEntPhysicalSysTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalSysTemp.setStatus("current")
_SlEntPhysicalSysAlias_Type = SnmpAdminString
_SlEntPhysicalSysAlias_Object = MibTableColumn
slEntPhysicalSysAlias = _SlEntPhysicalSysAlias_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 26),
    _SlEntPhysicalSysAlias_Type()
)
slEntPhysicalSysAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEntPhysicalSysAlias.setStatus("current")
_SlEntPhysicalSysSubType_Type = Integer32
_SlEntPhysicalSysSubType_Object = MibTableColumn
slEntPhysicalSysSubType = _SlEntPhysicalSysSubType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 27),
    _SlEntPhysicalSysSubType_Type()
)
slEntPhysicalSysSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEntPhysicalSysSubType.setStatus("current")
_SlEntityNotification_ObjectIdentity = ObjectIdentity
slEntityNotification = _SlEntityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ENTITY-MIB",
    **{"PhysicalIndex": PhysicalIndex,
       "PhysicalClass": PhysicalClass,
       "PhysicalType": PhysicalType,
       "CleiCode": CleiCode,
       "slmEntity": slmEntity,
       "slEntityPhysical": slEntityPhysical,
       "slEntPhysicalTable": slEntPhysicalTable,
       "slEntPhysicalEntry": slEntPhysicalEntry,
       "slEntPhysicalIndex": slEntPhysicalIndex,
       "slEntPhysicalDescr": slEntPhysicalDescr,
       "slEntPhysicalClass": slEntPhysicalClass,
       "slEntPhysicalHardwareRev": slEntPhysicalHardwareRev,
       "slEntPhysicalFirmwareRev": slEntPhysicalFirmwareRev,
       "slEntPhysicalSoftwareRev": slEntPhysicalSoftwareRev,
       "slEntPhysicalSerialNum": slEntPhysicalSerialNum,
       "slEntPhysicalProtectionEntity": slEntPhysicalProtectionEntity,
       "slEntPhysicalProtectState": slEntPhysicalProtectState,
       "slEntPhysicalProtectMode": slEntPhysicalProtectMode,
       "slEntPhysicalStatus": slEntPhysicalStatus,
       "slEntPhysicalFailureDescription": slEntPhysicalFailureDescription,
       "slEntPhysicalAdminStatus": slEntPhysicalAdminStatus,
       "slEntPhysicalOperStatus": slEntPhysicalOperStatus,
       "slEntPhysicalSysUptime": slEntPhysicalSysUptime,
       "slEntPhysicalType": slEntPhysicalType,
       "slEntPhysicalCleiCode": slEntPhysicalCleiCode,
       "slEntPhysicalPartNumber": slEntPhysicalPartNumber,
       "slEntPhysicalOemSerialNum": slEntPhysicalOemSerialNum,
       "slEntPhysicalProductionDate": slEntPhysicalProductionDate,
       "slEntPhysicalSysTemp": slEntPhysicalSysTemp,
       "slEntPhysicalSysAlias": slEntPhysicalSysAlias,
       "slEntPhysicalSysSubType": slEntPhysicalSysSubType,
       "slEntityNotification": slEntityNotification}
)
