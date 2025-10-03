# SNMP MIB module (AT-ALMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-ALMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:20 2025
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

(DisplayStringUnsized,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized")

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

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

atAlmMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26)
)
if mibBuilder.loadTexts:
    atAlmMon.setRevisions(
        ("2017-02-08 00:00",
         "2014-05-12 00:15",
         "2013-12-13 11:46")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtAlmMonAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("alarmTypeInvalid", 0),
          ("externalPSU", 1),
          ("epsr", 2),
          ("contactInput", 3),
          ("portLinkDown", 4),
          ("loopDetect", 5),
          ("mainPse", 6),
          ("portPoeFailure", 7),
          ("temperature", 8),
          ("g8032", 9))
    )



class AtAlmMonActionUseOutput(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("used", 2))
    )



class AtAlmMonAbnormalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



class AtAlmMonActionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtAlmMonActionTable_Object = MibTable
atAlmMonActionTable = _AtAlmMonActionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1)
)
if mibBuilder.loadTexts:
    atAlmMonActionTable.setStatus("current")
_AtAlmMonActionEntry_Object = MibTableRow
atAlmMonActionEntry = _AtAlmMonActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1)
)
atAlmMonActionEntry.setIndexNames(
    (0, "AT-ALMMON-MIB", "atAlmMonActionStackMemberId"),
    (0, "AT-ALMMON-MIB", "atAlmMonActionIndex"),
)
if mibBuilder.loadTexts:
    atAlmMonActionEntry.setStatus("current")
_AtAlmMonActionStackMemberId_Type = Unsigned32
_AtAlmMonActionStackMemberId_Object = MibTableColumn
atAlmMonActionStackMemberId = _AtAlmMonActionStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 1),
    _AtAlmMonActionStackMemberId_Type()
)
atAlmMonActionStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionStackMemberId.setStatus("current")
_AtAlmMonActionIndex_Type = Unsigned32
_AtAlmMonActionIndex_Object = MibTableColumn
atAlmMonActionIndex = _AtAlmMonActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 2),
    _AtAlmMonActionIndex_Type()
)
atAlmMonActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionIndex.setStatus("current")
_AtAlmMonAlarmType_Type = AtAlmMonAlarmType
_AtAlmMonAlarmType_Object = MibTableColumn
atAlmMonAlarmType = _AtAlmMonAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 3),
    _AtAlmMonAlarmType_Type()
)
atAlmMonAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAlarmType.setStatus("current")
_AtAlmMonAlarmTypeSelection_Type = Unsigned32
_AtAlmMonAlarmTypeSelection_Object = MibTableColumn
atAlmMonAlarmTypeSelection = _AtAlmMonAlarmTypeSelection_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 4),
    _AtAlmMonAlarmTypeSelection_Type()
)
atAlmMonAlarmTypeSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonAlarmTypeSelection.setStatus("current")


class _AtAlmMonActionDescription_Type(DisplayStringUnsized):
    """Custom type atAlmMonActionDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtAlmMonActionDescription_Type.__name__ = "DisplayStringUnsized"
_AtAlmMonActionDescription_Object = MibTableColumn
atAlmMonActionDescription = _AtAlmMonActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 5),
    _AtAlmMonActionDescription_Type()
)
atAlmMonActionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionDescription.setStatus("current")
_AtAlmMonActionUseRelay1_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay1_Object = MibTableColumn
atAlmMonActionUseRelay1 = _AtAlmMonActionUseRelay1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 6),
    _AtAlmMonActionUseRelay1_Type()
)
atAlmMonActionUseRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay1.setStatus("current")
_AtAlmMonActionUseRelay2_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay2_Object = MibTableColumn
atAlmMonActionUseRelay2 = _AtAlmMonActionUseRelay2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 7),
    _AtAlmMonActionUseRelay2_Type()
)
atAlmMonActionUseRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay2.setStatus("current")
_AtAlmMonActionUseRelay3_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay3_Object = MibTableColumn
atAlmMonActionUseRelay3 = _AtAlmMonActionUseRelay3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 8),
    _AtAlmMonActionUseRelay3_Type()
)
atAlmMonActionUseRelay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseRelay3.setStatus("current")
_AtAlmMonActionUseFaultLed_Type = AtAlmMonActionUseOutput
_AtAlmMonActionUseFaultLed_Object = MibTableColumn
atAlmMonActionUseFaultLed = _AtAlmMonActionUseFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 9),
    _AtAlmMonActionUseFaultLed_Type()
)
atAlmMonActionUseFaultLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonActionUseFaultLed.setStatus("current")
_AtAlmMonAbnormalState_Type = AtAlmMonAbnormalState
_AtAlmMonAbnormalState_Object = MibTableColumn
atAlmMonAbnormalState = _AtAlmMonAbnormalState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 10),
    _AtAlmMonAbnormalState_Type()
)
atAlmMonAbnormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atAlmMonAbnormalState.setStatus("current")
_AtAlmMonActionState_Type = AtAlmMonActionState
_AtAlmMonActionState_Object = MibTableColumn
atAlmMonActionState = _AtAlmMonActionState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 11),
    _AtAlmMonActionState_Type()
)
atAlmMonActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAlmMonActionState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ALMMON-MIB",
    **{"AtAlmMonAlarmType": AtAlmMonAlarmType,
       "AtAlmMonActionUseOutput": AtAlmMonActionUseOutput,
       "AtAlmMonAbnormalState": AtAlmMonAbnormalState,
       "AtAlmMonActionState": AtAlmMonActionState,
       "atAlmMon": atAlmMon,
       "atAlmMonActionTable": atAlmMonActionTable,
       "atAlmMonActionEntry": atAlmMonActionEntry,
       "atAlmMonActionStackMemberId": atAlmMonActionStackMemberId,
       "atAlmMonActionIndex": atAlmMonActionIndex,
       "atAlmMonAlarmType": atAlmMonAlarmType,
       "atAlmMonAlarmTypeSelection": atAlmMonAlarmTypeSelection,
       "atAlmMonActionDescription": atAlmMonActionDescription,
       "atAlmMonActionUseRelay1": atAlmMonActionUseRelay1,
       "atAlmMonActionUseRelay2": atAlmMonActionUseRelay2,
       "atAlmMonActionUseRelay3": atAlmMonActionUseRelay3,
       "atAlmMonActionUseFaultLed": atAlmMonActionUseFaultLed,
       "atAlmMonAbnormalState": atAlmMonAbnormalState,
       "atAlmMonActionState": atAlmMonActionState}
)
