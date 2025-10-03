# SNMP MIB module (HH3C-LPBKDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LPBKDT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:04 2025
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

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cLpbkdt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95)
)
if mibBuilder.loadTexts:
    hh3cLpbkdt.setRevisions(
        ("2014-07-26 15:18",
         "2009-03-30 17:41",
         "2008-09-27 15:04")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cLpbkdtActionType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("block", 2),
          ("nolearning", 3),
          ("shutdown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cLpbkdtNotifications_ObjectIdentity = ObjectIdentity
hh3cLpbkdtNotifications = _Hh3cLpbkdtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1)
)
_Hh3cLpbkdtTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cLpbkdtTrapPrefix = _Hh3cLpbkdtTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0)
)
_Hh3cLpbkdtObjects_ObjectIdentity = ObjectIdentity
hh3cLpbkdtObjects = _Hh3cLpbkdtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2)
)
_Hh3cLpbkdtVlanID_Type = VlanId
_Hh3cLpbkdtVlanID_Object = MibScalar
hh3cLpbkdtVlanID = _Hh3cLpbkdtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 1),
    _Hh3cLpbkdtVlanID_Type()
)
hh3cLpbkdtVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLpbkdtVlanID.setStatus("current")


class _Hh3cLpbkdtVlanEnable_Type(OctetString):
    """Custom type hh3cLpbkdtVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_Hh3cLpbkdtVlanEnable_Type.__name__ = "OctetString"
_Hh3cLpbkdtVlanEnable_Object = MibScalar
hh3cLpbkdtVlanEnable = _Hh3cLpbkdtVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 2),
    _Hh3cLpbkdtVlanEnable_Type()
)
hh3cLpbkdtVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLpbkdtVlanEnable.setStatus("current")


class _Hh3cLpbkdtAction_Type(Hh3cLpbkdtActionType):
    """Custom type hh3cLpbkdtAction based on Hh3cLpbkdtActionType"""
    defaultValue = 1


_Hh3cLpbkdtAction_Type.__name__ = "Hh3cLpbkdtActionType"
_Hh3cLpbkdtAction_Object = MibScalar
hh3cLpbkdtAction = _Hh3cLpbkdtAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 3),
    _Hh3cLpbkdtAction_Type()
)
hh3cLpbkdtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLpbkdtAction.setStatus("current")


class _Hh3cLpbkdtIntervalTime_Type(Integer32):
    """Custom type hh3cLpbkdtIntervalTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Hh3cLpbkdtIntervalTime_Type.__name__ = "Integer32"
_Hh3cLpbkdtIntervalTime_Object = MibScalar
hh3cLpbkdtIntervalTime = _Hh3cLpbkdtIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 4),
    _Hh3cLpbkdtIntervalTime_Type()
)
hh3cLpbkdtIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLpbkdtIntervalTime.setStatus("current")
_Hh3cLpbkdtPortTable_Object = MibTable
hh3cLpbkdtPortTable = _Hh3cLpbkdtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cLpbkdtPortTable.setStatus("current")
_Hh3cLpbkdtPortEntry_Object = MibTableRow
hh3cLpbkdtPortEntry = _Hh3cLpbkdtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5, 1)
)
hh3cLpbkdtPortEntry.setIndexNames(
    (0, "HH3C-LPBKDT-MIB", "hh3cLpbkdtPortIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cLpbkdtPortEntry.setStatus("current")
_Hh3cLpbkdtPortIfIndex_Type = InterfaceIndex
_Hh3cLpbkdtPortIfIndex_Object = MibTableColumn
hh3cLpbkdtPortIfIndex = _Hh3cLpbkdtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5, 1, 1),
    _Hh3cLpbkdtPortIfIndex_Type()
)
hh3cLpbkdtPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLpbkdtPortIfIndex.setStatus("current")


class _Hh3cLpbkdtPortVlanEnable_Type(OctetString):
    """Custom type hh3cLpbkdtPortVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_Hh3cLpbkdtPortVlanEnable_Type.__name__ = "OctetString"
_Hh3cLpbkdtPortVlanEnable_Object = MibTableColumn
hh3cLpbkdtPortVlanEnable = _Hh3cLpbkdtPortVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5, 1, 2),
    _Hh3cLpbkdtPortVlanEnable_Type()
)
hh3cLpbkdtPortVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLpbkdtPortVlanEnable.setStatus("current")
_Hh3cLpbkdtPortAction_Type = Hh3cLpbkdtActionType
_Hh3cLpbkdtPortAction_Object = MibTableColumn
hh3cLpbkdtPortAction = _Hh3cLpbkdtPortAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5, 1, 3),
    _Hh3cLpbkdtPortAction_Type()
)
hh3cLpbkdtPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLpbkdtPortAction.setStatus("current")
_Hh3cLpbkdtPortLoopbacked_Type = TruthValue
_Hh3cLpbkdtPortLoopbacked_Object = MibTableColumn
hh3cLpbkdtPortLoopbacked = _Hh3cLpbkdtPortLoopbacked_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 5, 1, 4),
    _Hh3cLpbkdtPortLoopbacked_Type()
)
hh3cLpbkdtPortLoopbacked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLpbkdtPortLoopbacked.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cLpbkdtTrapLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 1)
)
hh3cLpbkdtTrapLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cLpbkdtTrapLoopbacked.setStatus(
        "current"
    )

hh3cLpbkdtTrapRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 2)
)
hh3cLpbkdtTrapRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cLpbkdtTrapRecovered.setStatus(
        "current"
    )

hh3cLpbkdtTrapPerVlanLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 3)
)
hh3cLpbkdtTrapPerVlanLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-LPBKDT-MIB", "hh3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    hh3cLpbkdtTrapPerVlanLoopbacked.setStatus(
        "current"
    )

hh3cLpbkdtTrapPerVlanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 4)
)
hh3cLpbkdtTrapPerVlanRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-LPBKDT-MIB", "hh3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    hh3cLpbkdtTrapPerVlanRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LPBKDT-MIB",
    **{"Hh3cLpbkdtActionType": Hh3cLpbkdtActionType,
       "hh3cLpbkdt": hh3cLpbkdt,
       "hh3cLpbkdtNotifications": hh3cLpbkdtNotifications,
       "hh3cLpbkdtTrapPrefix": hh3cLpbkdtTrapPrefix,
       "hh3cLpbkdtTrapLoopbacked": hh3cLpbkdtTrapLoopbacked,
       "hh3cLpbkdtTrapRecovered": hh3cLpbkdtTrapRecovered,
       "hh3cLpbkdtTrapPerVlanLoopbacked": hh3cLpbkdtTrapPerVlanLoopbacked,
       "hh3cLpbkdtTrapPerVlanRecovered": hh3cLpbkdtTrapPerVlanRecovered,
       "hh3cLpbkdtObjects": hh3cLpbkdtObjects,
       "hh3cLpbkdtVlanID": hh3cLpbkdtVlanID,
       "hh3cLpbkdtVlanEnable": hh3cLpbkdtVlanEnable,
       "hh3cLpbkdtAction": hh3cLpbkdtAction,
       "hh3cLpbkdtIntervalTime": hh3cLpbkdtIntervalTime,
       "hh3cLpbkdtPortTable": hh3cLpbkdtPortTable,
       "hh3cLpbkdtPortEntry": hh3cLpbkdtPortEntry,
       "hh3cLpbkdtPortIfIndex": hh3cLpbkdtPortIfIndex,
       "hh3cLpbkdtPortVlanEnable": hh3cLpbkdtPortVlanEnable,
       "hh3cLpbkdtPortAction": hh3cLpbkdtPortAction,
       "hh3cLpbkdtPortLoopbacked": hh3cLpbkdtPortLoopbacked}
)
