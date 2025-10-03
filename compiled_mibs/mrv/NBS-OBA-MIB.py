# SNMP MIB module (NBS-OBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-OBA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:21 2025
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

(NbsTcMHz,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMHz",
    "nbs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nbsObaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 240)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsObaInfoGrp_ObjectIdentity = ObjectIdentity
nbsObaInfoGrp = _NbsObaInfoGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 240, 1)
)
if mibBuilder.loadTexts:
    nbsObaInfoGrp.setStatus("current")
_NbsObaInfoTable_Object = MibTable
nbsObaInfoTable = _NbsObaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1)
)
if mibBuilder.loadTexts:
    nbsObaInfoTable.setStatus("current")
_NbsObaInfoEntry_Object = MibTableRow
nbsObaInfoEntry = _NbsObaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1)
)
nbsObaInfoEntry.setIndexNames(
    (0, "NBS-OBA-MIB", "nbsObaInfoLineIfIndex"),
)
if mibBuilder.loadTexts:
    nbsObaInfoEntry.setStatus("current")
_NbsObaInfoLineIfIndex_Type = InterfaceIndex
_NbsObaInfoLineIfIndex_Object = MibTableColumn
nbsObaInfoLineIfIndex = _NbsObaInfoLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 1),
    _NbsObaInfoLineIfIndex_Type()
)
nbsObaInfoLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaInfoLineIfIndex.setStatus("current")
_NbsObaInfoAvails_Type = DisplayString
_NbsObaInfoAvails_Object = MibTableColumn
nbsObaInfoAvails = _NbsObaInfoAvails_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 2),
    _NbsObaInfoAvails_Type()
)
nbsObaInfoAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaInfoAvails.setStatus("current")
_NbsObaInfoUnitSize_Type = NbsTcMHz
_NbsObaInfoUnitSize_Object = MibTableColumn
nbsObaInfoUnitSize = _NbsObaInfoUnitSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 3),
    _NbsObaInfoUnitSize_Type()
)
nbsObaInfoUnitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaInfoUnitSize.setStatus("current")
_NbsObaInfoMaxUnits_Type = Integer32
_NbsObaInfoMaxUnits_Object = MibTableColumn
nbsObaInfoMaxUnits = _NbsObaInfoMaxUnits_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 4),
    _NbsObaInfoMaxUnits_Type()
)
nbsObaInfoMaxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaInfoMaxUnits.setStatus("current")
_NbsObaInfoMaxUnitsPerClientPort_Type = Integer32
_NbsObaInfoMaxUnitsPerClientPort_Object = MibTableColumn
nbsObaInfoMaxUnitsPerClientPort = _NbsObaInfoMaxUnitsPerClientPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 1, 1, 1, 5),
    _NbsObaInfoMaxUnitsPerClientPort_Type()
)
nbsObaInfoMaxUnitsPerClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaInfoMaxUnitsPerClientPort.setStatus("current")
_NbsObaDefineGrp_ObjectIdentity = ObjectIdentity
nbsObaDefineGrp = _NbsObaDefineGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 240, 2)
)
if mibBuilder.loadTexts:
    nbsObaDefineGrp.setStatus("current")
_NbsObaDefineTableSize_Type = Integer32
_NbsObaDefineTableSize_Object = MibScalar
nbsObaDefineTableSize = _NbsObaDefineTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 1),
    _NbsObaDefineTableSize_Type()
)
nbsObaDefineTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefineTableSize.setStatus("current")
_NbsObaDefineTable_Object = MibTable
nbsObaDefineTable = _NbsObaDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2)
)
if mibBuilder.loadTexts:
    nbsObaDefineTable.setStatus("current")
_NbsObaDefineEntry_Object = MibTableRow
nbsObaDefineEntry = _NbsObaDefineEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1)
)
nbsObaDefineEntry.setIndexNames(
    (0, "NBS-OBA-MIB", "nbsObaDefineLinePort"),
    (0, "NBS-OBA-MIB", "nbsObaDefineOrdinalIndex"),
)
if mibBuilder.loadTexts:
    nbsObaDefineEntry.setStatus("current")
_NbsObaDefineLinePort_Type = InterfaceIndex
_NbsObaDefineLinePort_Object = MibTableColumn
nbsObaDefineLinePort = _NbsObaDefineLinePort_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 1),
    _NbsObaDefineLinePort_Type()
)
nbsObaDefineLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefineLinePort.setStatus("current")
_NbsObaDefineOrdinalIndex_Type = Integer32
_NbsObaDefineOrdinalIndex_Object = MibTableColumn
nbsObaDefineOrdinalIndex = _NbsObaDefineOrdinalIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 2),
    _NbsObaDefineOrdinalIndex_Type()
)
nbsObaDefineOrdinalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefineOrdinalIndex.setStatus("current")


class _NbsObaDefineLabel_Type(DisplayString):
    """Custom type nbsObaDefineLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsObaDefineLabel_Type.__name__ = "DisplayString"
_NbsObaDefineLabel_Object = MibTableColumn
nbsObaDefineLabel = _NbsObaDefineLabel_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 10),
    _NbsObaDefineLabel_Type()
)
nbsObaDefineLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineLabel.setStatus("current")


class _NbsObaDefineOduType_Type(Integer32):
    """Custom type nbsObaDefineOduType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 1),
          ("odu0", 2))
    )


_NbsObaDefineOduType_Type.__name__ = "Integer32"
_NbsObaDefineOduType_Object = MibTableColumn
nbsObaDefineOduType = _NbsObaDefineOduType_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 11),
    _NbsObaDefineOduType_Type()
)
nbsObaDefineOduType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineOduType.setStatus("current")


class _NbsObaDefineOduList_Type(DisplayString):
    """Custom type nbsObaDefineOduList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsObaDefineOduList_Type.__name__ = "DisplayString"
_NbsObaDefineOduList_Object = MibTableColumn
nbsObaDefineOduList = _NbsObaDefineOduList_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 12),
    _NbsObaDefineOduList_Type()
)
nbsObaDefineOduList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineOduList.setStatus("current")
_NbsObaDefineOduCount_Type = Integer32
_NbsObaDefineOduCount_Object = MibTableColumn
nbsObaDefineOduCount = _NbsObaDefineOduCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 13),
    _NbsObaDefineOduCount_Type()
)
nbsObaDefineOduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefineOduCount.setStatus("current")


class _NbsObaDefineMapType_Type(Integer32):
    """Custom type nbsObaDefineMapType based on Integer32"""
    defaultValue = 1

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
        *(("unconfigured", 1),
          ("express", 2),
          ("standAlone", 3),
          ("primary", 4),
          ("secondary", 5))
    )


_NbsObaDefineMapType_Type.__name__ = "Integer32"
_NbsObaDefineMapType_Object = MibTableColumn
nbsObaDefineMapType = _NbsObaDefineMapType_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 20),
    _NbsObaDefineMapType_Type()
)
nbsObaDefineMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineMapType.setStatus("current")
_NbsObaDefineClientPort_Type = InterfaceIndex
_NbsObaDefineClientPort_Object = MibTableColumn
nbsObaDefineClientPort = _NbsObaDefineClientPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 21),
    _NbsObaDefineClientPort_Type()
)
nbsObaDefineClientPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineClientPort.setStatus("current")


class _NbsObaDefineCoupledWith_Type(DisplayString):
    """Custom type nbsObaDefineCoupledWith based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsObaDefineCoupledWith_Type.__name__ = "DisplayString"
_NbsObaDefineCoupledWith_Object = MibTableColumn
nbsObaDefineCoupledWith = _NbsObaDefineCoupledWith_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 22),
    _NbsObaDefineCoupledWith_Type()
)
nbsObaDefineCoupledWith.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineCoupledWith.setStatus("current")


class _NbsObaDefinePresentState_Type(Integer32):
    """Custom type nbsObaDefinePresentState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_NbsObaDefinePresentState_Type.__name__ = "Integer32"
_NbsObaDefinePresentState_Object = MibTableColumn
nbsObaDefinePresentState = _NbsObaDefinePresentState_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 29),
    _NbsObaDefinePresentState_Type()
)
nbsObaDefinePresentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefinePresentState.setStatus("current")


class _NbsObaDefineAllocationInfo_Type(Integer32):
    """Custom type nbsObaDefineAllocationInfo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("unitsExceedProtocolSpec", 2),
          ("additionalUnitsNeededForProtocol", 3),
          ("unitsMatchProtocolSpec", 4),
          ("unitsExceedExpress", 5),
          ("additionalUnitsNeededForExpress", 6),
          ("unitsMatchExpress", 7))
    )


_NbsObaDefineAllocationInfo_Type.__name__ = "Integer32"
_NbsObaDefineAllocationInfo_Object = MibTableColumn
nbsObaDefineAllocationInfo = _NbsObaDefineAllocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 30),
    _NbsObaDefineAllocationInfo_Type()
)
nbsObaDefineAllocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaDefineAllocationInfo.setStatus("current")


class _NbsObaDefineRowStatus_Type(RowStatus):
    """Custom type nbsObaDefineRowStatus based on RowStatus"""
    defaultValue = 2


_NbsObaDefineRowStatus_Type.__name__ = "RowStatus"
_NbsObaDefineRowStatus_Object = MibTableColumn
nbsObaDefineRowStatus = _NbsObaDefineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 2, 2, 1, 99),
    _NbsObaDefineRowStatus_Type()
)
nbsObaDefineRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsObaDefineRowStatus.setStatus("current")
_NbsObaAlsGrp_ObjectIdentity = ObjectIdentity
nbsObaAlsGrp = _NbsObaAlsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 240, 3)
)
if mibBuilder.loadTexts:
    nbsObaAlsGrp.setStatus("current")
_NbsObaAlsTable_Object = MibTable
nbsObaAlsTable = _NbsObaAlsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 3, 1)
)
if mibBuilder.loadTexts:
    nbsObaAlsTable.setStatus("current")
_NbsObaAlsEntry_Object = MibTableRow
nbsObaAlsEntry = _NbsObaAlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1)
)
nbsObaAlsEntry.setIndexNames(
    (0, "NBS-OBA-MIB", "nbsObaAlsIfIndex"),
)
if mibBuilder.loadTexts:
    nbsObaAlsEntry.setStatus("current")
_NbsObaAlsIfIndex_Type = InterfaceIndex
_NbsObaAlsIfIndex_Object = MibTableColumn
nbsObaAlsIfIndex = _NbsObaAlsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 1),
    _NbsObaAlsIfIndex_Type()
)
nbsObaAlsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsObaAlsIfIndex.setStatus("current")


class _NbsObaAlsState_Type(Integer32):
    """Custom type nbsObaAlsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("enable", 2),
          ("disable", 3))
    )


_NbsObaAlsState_Type.__name__ = "Integer32"
_NbsObaAlsState_Object = MibTableColumn
nbsObaAlsState = _NbsObaAlsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 240, 3, 1, 1, 10),
    _NbsObaAlsState_Type()
)
nbsObaAlsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsObaAlsState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-OBA-MIB",
    **{"nbsObaMib": nbsObaMib,
       "nbsObaInfoGrp": nbsObaInfoGrp,
       "nbsObaInfoTable": nbsObaInfoTable,
       "nbsObaInfoEntry": nbsObaInfoEntry,
       "nbsObaInfoLineIfIndex": nbsObaInfoLineIfIndex,
       "nbsObaInfoAvails": nbsObaInfoAvails,
       "nbsObaInfoUnitSize": nbsObaInfoUnitSize,
       "nbsObaInfoMaxUnits": nbsObaInfoMaxUnits,
       "nbsObaInfoMaxUnitsPerClientPort": nbsObaInfoMaxUnitsPerClientPort,
       "nbsObaDefineGrp": nbsObaDefineGrp,
       "nbsObaDefineTableSize": nbsObaDefineTableSize,
       "nbsObaDefineTable": nbsObaDefineTable,
       "nbsObaDefineEntry": nbsObaDefineEntry,
       "nbsObaDefineLinePort": nbsObaDefineLinePort,
       "nbsObaDefineOrdinalIndex": nbsObaDefineOrdinalIndex,
       "nbsObaDefineLabel": nbsObaDefineLabel,
       "nbsObaDefineOduType": nbsObaDefineOduType,
       "nbsObaDefineOduList": nbsObaDefineOduList,
       "nbsObaDefineOduCount": nbsObaDefineOduCount,
       "nbsObaDefineMapType": nbsObaDefineMapType,
       "nbsObaDefineClientPort": nbsObaDefineClientPort,
       "nbsObaDefineCoupledWith": nbsObaDefineCoupledWith,
       "nbsObaDefinePresentState": nbsObaDefinePresentState,
       "nbsObaDefineAllocationInfo": nbsObaDefineAllocationInfo,
       "nbsObaDefineRowStatus": nbsObaDefineRowStatus,
       "nbsObaAlsGrp": nbsObaAlsGrp,
       "nbsObaAlsTable": nbsObaAlsTable,
       "nbsObaAlsEntry": nbsObaAlsEntry,
       "nbsObaAlsIfIndex": nbsObaAlsIfIndex,
       "nbsObaAlsState": nbsObaAlsState}
)
