# SNMP MIB module (HH3C-PVST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PVST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:34 2025
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

hh3cPvst = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131)
)
if mibBuilder.loadTexts:
    hh3cPvst.setRevisions(
        ("2014-05-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPvstObjects_ObjectIdentity = ObjectIdentity
hh3cPvstObjects = _Hh3cPvstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1)
)
_Hh3cPvstVlanConfigTable_Object = MibTable
hh3cPvstVlanConfigTable = _Hh3cPvstVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cPvstVlanConfigTable.setStatus("current")
_Hh3cPvstVlanConfigEntry_Object = MibTableRow
hh3cPvstVlanConfigEntry = _Hh3cPvstVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1, 1)
)
hh3cPvstVlanConfigEntry.setIndexNames(
    (0, "HH3C-PVST-MIB", "hh3cPvstVlanID"),
)
if mibBuilder.loadTexts:
    hh3cPvstVlanConfigEntry.setStatus("current")


class _Hh3cPvstVlanID_Type(Integer32):
    """Custom type hh3cPvstVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cPvstVlanID_Type.__name__ = "Integer32"
_Hh3cPvstVlanID_Object = MibTableColumn
hh3cPvstVlanID = _Hh3cPvstVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1, 1, 1),
    _Hh3cPvstVlanID_Type()
)
hh3cPvstVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPvstVlanID.setStatus("current")
_Hh3cPvstVlanPortConfigTable_Object = MibTable
hh3cPvstVlanPortConfigTable = _Hh3cPvstVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cPvstVlanPortConfigTable.setStatus("current")
_Hh3cPvstVlanPortConfigEntry_Object = MibTableRow
hh3cPvstVlanPortConfigEntry = _Hh3cPvstVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1)
)
hh3cPvstVlanPortConfigEntry.setIndexNames(
    (0, "HH3C-PVST-MIB", "hh3cPvstPortVlanID"),
    (0, "HH3C-PVST-MIB", "hh3cPvstPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cPvstVlanPortConfigEntry.setStatus("current")


class _Hh3cPvstPortVlanID_Type(Integer32):
    """Custom type hh3cPvstPortVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cPvstPortVlanID_Type.__name__ = "Integer32"
_Hh3cPvstPortVlanID_Object = MibTableColumn
hh3cPvstPortVlanID = _Hh3cPvstPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1, 1),
    _Hh3cPvstPortVlanID_Type()
)
hh3cPvstPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPvstPortVlanID.setStatus("current")


class _Hh3cPvstPortIndex_Type(Integer32):
    """Custom type hh3cPvstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPvstPortIndex_Type.__name__ = "Integer32"
_Hh3cPvstPortIndex_Object = MibTableColumn
hh3cPvstPortIndex = _Hh3cPvstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1, 2),
    _Hh3cPvstPortIndex_Type()
)
hh3cPvstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPvstPortIndex.setStatus("current")
_Hh3cPvstNotifications_ObjectIdentity = ObjectIdentity
hh3cPvstNotifications = _Hh3cPvstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 2)
)
_Hh3cPvstEvents_ObjectIdentity = ObjectIdentity
hh3cPvstEvents = _Hh3cPvstEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cPvstVlanPortDetectedTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0, 1)
)
hh3cPvstVlanPortDetectedTc.setObjects(
      *(("HH3C-PVST-MIB", "hh3cPvstPortVlanID"),
        ("HH3C-PVST-MIB", "hh3cPvstPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPvstVlanPortDetectedTc.setStatus(
        "current"
    )

hh3cPvstVlanPortRcvdTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0, 2)
)
hh3cPvstVlanPortRcvdTc.setObjects(
      *(("HH3C-PVST-MIB", "hh3cPvstPortVlanID"),
        ("HH3C-PVST-MIB", "hh3cPvstPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPvstVlanPortRcvdTc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PVST-MIB",
    **{"hh3cPvst": hh3cPvst,
       "hh3cPvstObjects": hh3cPvstObjects,
       "hh3cPvstVlanConfigTable": hh3cPvstVlanConfigTable,
       "hh3cPvstVlanConfigEntry": hh3cPvstVlanConfigEntry,
       "hh3cPvstVlanID": hh3cPvstVlanID,
       "hh3cPvstVlanPortConfigTable": hh3cPvstVlanPortConfigTable,
       "hh3cPvstVlanPortConfigEntry": hh3cPvstVlanPortConfigEntry,
       "hh3cPvstPortVlanID": hh3cPvstPortVlanID,
       "hh3cPvstPortIndex": hh3cPvstPortIndex,
       "hh3cPvstNotifications": hh3cPvstNotifications,
       "hh3cPvstEvents": hh3cPvstEvents,
       "hh3cPvstVlanPortDetectedTc": hh3cPvstVlanPortDetectedTc,
       "hh3cPvstVlanPortRcvdTc": hh3cPvstVlanPortRcvdTc}
)
