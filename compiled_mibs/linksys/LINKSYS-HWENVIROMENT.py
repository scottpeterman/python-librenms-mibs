# SNMP MIB module (LINKSYS-HWENVIROMENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-HWENVIROMENT
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:15 2025
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

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rlEnv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83)
)
if mibBuilder.loadTexts:
    rlEnv.setRevisions(
        ("2003-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlEnvMonState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notPresent", 5),
          ("notFunctioning", 6))
    )



class RlEnvMonDirection(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unKnown", 1),
          ("frontToBack", 2),
          ("backToFront", 3),
          ("clockwise", 4),
          ("unClockwise", 5),
          ("insideOut", 6),
          ("outsideIn", 7),
          ("rightToLeft", 8),
          ("leftToRight", 9))
    )



# MIB Managed Objects in the order of their OIDs

_RlEnvPhysicalDescription_ObjectIdentity = ObjectIdentity
rlEnvPhysicalDescription = _RlEnvPhysicalDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1)
)
_RlEnvMonFanStatusTable_Object = MibTable
rlEnvMonFanStatusTable = _RlEnvMonFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 1)
)
if mibBuilder.loadTexts:
    rlEnvMonFanStatusTable.setStatus("current")
_RlEnvMonFanStatusEntry_Object = MibTableRow
rlEnvMonFanStatusEntry = _RlEnvMonFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 1, 1)
)
rlEnvMonFanStatusEntry.setIndexNames(
    (0, "LINKSYS-HWENVIROMENT", "rlEnvMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    rlEnvMonFanStatusEntry.setStatus("current")
_RlEnvMonFanStatusIndex_Type = Integer32
_RlEnvMonFanStatusIndex_Object = MibTableColumn
rlEnvMonFanStatusIndex = _RlEnvMonFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 1, 1, 1),
    _RlEnvMonFanStatusIndex_Type()
)
rlEnvMonFanStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEnvMonFanStatusIndex.setStatus("current")


class _RlEnvMonFanStatusDescr_Type(DisplayString):
    """Custom type rlEnvMonFanStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlEnvMonFanStatusDescr_Type.__name__ = "DisplayString"
_RlEnvMonFanStatusDescr_Object = MibTableColumn
rlEnvMonFanStatusDescr = _RlEnvMonFanStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 1, 1, 2),
    _RlEnvMonFanStatusDescr_Type()
)
rlEnvMonFanStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonFanStatusDescr.setStatus("current")
_RlEnvMonFanState_Type = RlEnvMonState
_RlEnvMonFanState_Object = MibTableColumn
rlEnvMonFanState = _RlEnvMonFanState_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 1, 1, 3),
    _RlEnvMonFanState_Type()
)
rlEnvMonFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonFanState.setStatus("current")
_RlEnvMonSupplyStatusTable_Object = MibTable
rlEnvMonSupplyStatusTable = _RlEnvMonSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2)
)
if mibBuilder.loadTexts:
    rlEnvMonSupplyStatusTable.setStatus("current")
_RlEnvMonSupplyStatusEntry_Object = MibTableRow
rlEnvMonSupplyStatusEntry = _RlEnvMonSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1)
)
rlEnvMonSupplyStatusEntry.setIndexNames(
    (0, "LINKSYS-HWENVIROMENT", "rlEnvMonSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    rlEnvMonSupplyStatusEntry.setStatus("current")


class _RlEnvMonSupplyStatusIndex_Type(Integer32):
    """Custom type rlEnvMonSupplyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlEnvMonSupplyStatusIndex_Type.__name__ = "Integer32"
_RlEnvMonSupplyStatusIndex_Object = MibTableColumn
rlEnvMonSupplyStatusIndex = _RlEnvMonSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1, 1),
    _RlEnvMonSupplyStatusIndex_Type()
)
rlEnvMonSupplyStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEnvMonSupplyStatusIndex.setStatus("current")


class _RlEnvMonSupplyStatusDescr_Type(DisplayString):
    """Custom type rlEnvMonSupplyStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlEnvMonSupplyStatusDescr_Type.__name__ = "DisplayString"
_RlEnvMonSupplyStatusDescr_Object = MibTableColumn
rlEnvMonSupplyStatusDescr = _RlEnvMonSupplyStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1, 2),
    _RlEnvMonSupplyStatusDescr_Type()
)
rlEnvMonSupplyStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonSupplyStatusDescr.setStatus("current")
_RlEnvMonSupplyState_Type = RlEnvMonState
_RlEnvMonSupplyState_Object = MibTableColumn
rlEnvMonSupplyState = _RlEnvMonSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1, 3),
    _RlEnvMonSupplyState_Type()
)
rlEnvMonSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonSupplyState.setStatus("current")


class _RlEnvMonSupplySource_Type(Integer32):
    """Custom type rlEnvMonSupplySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ac", 2),
          ("dc", 3),
          ("externalPowerSupply", 4),
          ("internalRedundant", 5))
    )


_RlEnvMonSupplySource_Type.__name__ = "Integer32"
_RlEnvMonSupplySource_Object = MibTableColumn
rlEnvMonSupplySource = _RlEnvMonSupplySource_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1, 4),
    _RlEnvMonSupplySource_Type()
)
rlEnvMonSupplySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonSupplySource.setStatus("current")
_RlEnvMonSupplyFanDirection_Type = RlEnvMonDirection
_RlEnvMonSupplyFanDirection_Object = MibTableColumn
rlEnvMonSupplyFanDirection = _RlEnvMonSupplyFanDirection_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 1, 2, 1, 5),
    _RlEnvMonSupplyFanDirection_Type()
)
rlEnvMonSupplyFanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvMonSupplyFanDirection.setStatus("current")
_RlEnvFanData_ObjectIdentity = ObjectIdentity
rlEnvFanData = _RlEnvFanData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5)
)
_RlEnvFanDataTable_Object = MibTable
rlEnvFanDataTable = _RlEnvFanDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1)
)
if mibBuilder.loadTexts:
    rlEnvFanDataTable.setStatus("current")
_RlEnvFanDataEntry_Object = MibTableRow
rlEnvFanDataEntry = _RlEnvFanDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1)
)
rlEnvFanDataEntry.setIndexNames(
    (0, "LINKSYS-HWENVIROMENT", "rlEnvFanDataStackUnit"),
)
if mibBuilder.loadTexts:
    rlEnvFanDataEntry.setStatus("current")
_RlEnvFanDataStackUnit_Type = Integer32
_RlEnvFanDataStackUnit_Object = MibTableColumn
rlEnvFanDataStackUnit = _RlEnvFanDataStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 1),
    _RlEnvFanDataStackUnit_Type()
)
rlEnvFanDataStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvFanDataStackUnit.setStatus("current")
_RlEnvFanDataTemp_Type = Integer32
_RlEnvFanDataTemp_Object = MibTableColumn
rlEnvFanDataTemp = _RlEnvFanDataTemp_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 2),
    _RlEnvFanDataTemp_Type()
)
rlEnvFanDataTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvFanDataTemp.setStatus("current")
_RlEnvFanDataSpeed_Type = Integer32
_RlEnvFanDataSpeed_Object = MibTableColumn
rlEnvFanDataSpeed = _RlEnvFanDataSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 3),
    _RlEnvFanDataSpeed_Type()
)
rlEnvFanDataSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvFanDataSpeed.setStatus("current")
_RlEnvFanDataOperLevel_Type = Integer32
_RlEnvFanDataOperLevel_Object = MibTableColumn
rlEnvFanDataOperLevel = _RlEnvFanDataOperLevel_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 4),
    _RlEnvFanDataOperLevel_Type()
)
rlEnvFanDataOperLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvFanDataOperLevel.setStatus("current")
_RlEnvFanDataAdminLevel_Type = Integer32
_RlEnvFanDataAdminLevel_Object = MibTableColumn
rlEnvFanDataAdminLevel = _RlEnvFanDataAdminLevel_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 5),
    _RlEnvFanDataAdminLevel_Type()
)
rlEnvFanDataAdminLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEnvFanDataAdminLevel.setStatus("current")
_RlEnvFanDataDirection_Type = RlEnvMonDirection
_RlEnvFanDataDirection_Object = MibTableColumn
rlEnvFanDataDirection = _RlEnvFanDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 83, 5, 1, 1, 6),
    _RlEnvFanDataDirection_Type()
)
rlEnvFanDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvFanDataDirection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-HWENVIROMENT",
    **{"RlEnvMonState": RlEnvMonState,
       "RlEnvMonDirection": RlEnvMonDirection,
       "rlEnv": rlEnv,
       "rlEnvPhysicalDescription": rlEnvPhysicalDescription,
       "rlEnvMonFanStatusTable": rlEnvMonFanStatusTable,
       "rlEnvMonFanStatusEntry": rlEnvMonFanStatusEntry,
       "rlEnvMonFanStatusIndex": rlEnvMonFanStatusIndex,
       "rlEnvMonFanStatusDescr": rlEnvMonFanStatusDescr,
       "rlEnvMonFanState": rlEnvMonFanState,
       "rlEnvMonSupplyStatusTable": rlEnvMonSupplyStatusTable,
       "rlEnvMonSupplyStatusEntry": rlEnvMonSupplyStatusEntry,
       "rlEnvMonSupplyStatusIndex": rlEnvMonSupplyStatusIndex,
       "rlEnvMonSupplyStatusDescr": rlEnvMonSupplyStatusDescr,
       "rlEnvMonSupplyState": rlEnvMonSupplyState,
       "rlEnvMonSupplySource": rlEnvMonSupplySource,
       "rlEnvMonSupplyFanDirection": rlEnvMonSupplyFanDirection,
       "rlEnvFanData": rlEnvFanData,
       "rlEnvFanDataTable": rlEnvFanDataTable,
       "rlEnvFanDataEntry": rlEnvFanDataEntry,
       "rlEnvFanDataStackUnit": rlEnvFanDataStackUnit,
       "rlEnvFanDataTemp": rlEnvFanDataTemp,
       "rlEnvFanDataSpeed": rlEnvFanDataSpeed,
       "rlEnvFanDataOperLevel": rlEnvFanDataOperLevel,
       "rlEnvFanDataAdminLevel": rlEnvFanDataAdminLevel,
       "rlEnvFanDataDirection": rlEnvFanDataDirection}
)
