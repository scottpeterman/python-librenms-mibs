# SNMP MIB module (HH3C-E1T1VI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-E1T1VI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:17 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

hh3cE1T1VI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76)
)
if mibBuilder.loadTexts:
    hh3cE1T1VI.setRevisions(
        ("2015-08-19 18:00",
         "2010-04-08 18:55",
         "2009-06-08 17:41",
         "2007-04-05 15:42")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cE1T1VITable_Object = MibTable
hh3cE1T1VITable = _Hh3cE1T1VITable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1)
)
if mibBuilder.loadTexts:
    hh3cE1T1VITable.setStatus("current")
_Hh3cE1T1VIEntry_Object = MibTableRow
hh3cE1T1VIEntry = _Hh3cE1T1VIEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1)
)
hh3cE1T1VIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cE1T1VIEntry.setStatus("current")
_Hh3cE1T1VIUsingTimeslots_Type = Integer32
_Hh3cE1T1VIUsingTimeslots_Object = MibTableColumn
hh3cE1T1VIUsingTimeslots = _Hh3cE1T1VIUsingTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 1),
    _Hh3cE1T1VIUsingTimeslots_Type()
)
hh3cE1T1VIUsingTimeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cE1T1VIUsingTimeslots.setStatus("current")
_Hh3cE1T1VIUsingTimeslotsRatio_Type = Integer32
_Hh3cE1T1VIUsingTimeslotsRatio_Object = MibTableColumn
hh3cE1T1VIUsingTimeslotsRatio = _Hh3cE1T1VIUsingTimeslotsRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 2),
    _Hh3cE1T1VIUsingTimeslotsRatio_Type()
)
hh3cE1T1VIUsingTimeslotsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cE1T1VIUsingTimeslotsRatio.setStatus("current")
_Hh3cE1T1VITimeslotsUsedUpCount_Type = Unsigned32
_Hh3cE1T1VITimeslotsUsedUpCount_Object = MibTableColumn
hh3cE1T1VITimeslotsUsedUpCount = _Hh3cE1T1VITimeslotsUsedUpCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 3),
    _Hh3cE1T1VITimeslotsUsedUpCount_Type()
)
hh3cE1T1VITimeslotsUsedUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cE1T1VITimeslotsUsedUpCount.setStatus("current")
_Hh3cE1T1VITimeslotSampleInterval_Type = Integer32
_Hh3cE1T1VITimeslotSampleInterval_Object = MibTableColumn
hh3cE1T1VITimeslotSampleInterval = _Hh3cE1T1VITimeslotSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 4),
    _Hh3cE1T1VITimeslotSampleInterval_Type()
)
hh3cE1T1VITimeslotSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cE1T1VITimeslotSampleInterval.setStatus("current")
_Hh3cE1T1VIUsingTimeslotsPeak_Type = Integer32
_Hh3cE1T1VIUsingTimeslotsPeak_Object = MibTableColumn
hh3cE1T1VIUsingTimeslotsPeak = _Hh3cE1T1VIUsingTimeslotsPeak_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 5),
    _Hh3cE1T1VIUsingTimeslotsPeak_Type()
)
hh3cE1T1VIUsingTimeslotsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cE1T1VIUsingTimeslotsPeak.setStatus("current")
_Hh3cE1T1VITrapTimeSlotsThreshold_Type = Integer32
_Hh3cE1T1VITrapTimeSlotsThreshold_Object = MibTableColumn
hh3cE1T1VITrapTimeSlotsThreshold = _Hh3cE1T1VITrapTimeSlotsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 1, 1, 6),
    _Hh3cE1T1VITrapTimeSlotsThreshold_Type()
)
hh3cE1T1VITrapTimeSlotsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cE1T1VITrapTimeSlotsThreshold.setStatus("current")
_Hh3cE1T1VINotifications_ObjectIdentity = ObjectIdentity
hh3cE1T1VINotifications = _Hh3cE1T1VINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 2)
)
_Hh3cE1T1VITrapPrefix_ObjectIdentity = ObjectIdentity
hh3cE1T1VITrapPrefix = _Hh3cE1T1VITrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 2, 0)
)
_Hh3cE1T1VIGeneral_ObjectIdentity = ObjectIdentity
hh3cE1T1VIGeneral = _Hh3cE1T1VIGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 3)
)


class _Hh3cE1T1VITrapTimeSlotEnable_Type(Integer32):
    """Custom type hh3cE1T1VITrapTimeSlotEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Hh3cE1T1VITrapTimeSlotEnable_Type.__name__ = "Integer32"
_Hh3cE1T1VITrapTimeSlotEnable_Object = MibScalar
hh3cE1T1VITrapTimeSlotEnable = _Hh3cE1T1VITrapTimeSlotEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 3, 1),
    _Hh3cE1T1VITrapTimeSlotEnable_Type()
)
hh3cE1T1VITrapTimeSlotEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cE1T1VITrapTimeSlotEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cE1T1VITrapTimeSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76, 2, 0, 1)
)
hh3cE1T1VITrapTimeSlot.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cE1T1VITrapTimeSlot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-E1T1VI-MIB",
    **{"hh3cE1T1VI": hh3cE1T1VI,
       "hh3cE1T1VITable": hh3cE1T1VITable,
       "hh3cE1T1VIEntry": hh3cE1T1VIEntry,
       "hh3cE1T1VIUsingTimeslots": hh3cE1T1VIUsingTimeslots,
       "hh3cE1T1VIUsingTimeslotsRatio": hh3cE1T1VIUsingTimeslotsRatio,
       "hh3cE1T1VITimeslotsUsedUpCount": hh3cE1T1VITimeslotsUsedUpCount,
       "hh3cE1T1VITimeslotSampleInterval": hh3cE1T1VITimeslotSampleInterval,
       "hh3cE1T1VIUsingTimeslotsPeak": hh3cE1T1VIUsingTimeslotsPeak,
       "hh3cE1T1VITrapTimeSlotsThreshold": hh3cE1T1VITrapTimeSlotsThreshold,
       "hh3cE1T1VINotifications": hh3cE1T1VINotifications,
       "hh3cE1T1VITrapPrefix": hh3cE1T1VITrapPrefix,
       "hh3cE1T1VITrapTimeSlot": hh3cE1T1VITrapTimeSlot,
       "hh3cE1T1VIGeneral": hh3cE1T1VIGeneral,
       "hh3cE1T1VITrapTimeSlotEnable": hh3cE1T1VITrapTimeSlotEnable}
)
