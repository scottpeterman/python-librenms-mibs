# SNMP MIB module (ENDACE-HBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-HBA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:56 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hbaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HbaNotifications_ObjectIdentity = ObjectIdentity
hbaNotifications = _HbaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14, 0)
)
if mibBuilder.loadTexts:
    hbaNotifications.setStatus("current")
_HbaObjects_ObjectIdentity = ObjectIdentity
hbaObjects = _HbaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1)
)
if mibBuilder.loadTexts:
    hbaObjects.setStatus("current")
_HbaFcTable_Object = MibTable
hbaFcTable = _HbaFcTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hbaFcTable.setStatus("current")
_HbaFcEntry_Object = MibTableRow
hbaFcEntry = _HbaFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 1, 1)
)
hbaFcEntry.setIndexNames(
    (0, "ENDACE-HBA-MIB", "hbaFcIndex"),
)
if mibBuilder.loadTexts:
    hbaFcEntry.setStatus("current")


class _HbaFcIndex_Type(Integer32):
    """Custom type hbaFcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HbaFcIndex_Type.__name__ = "Integer32"
_HbaFcIndex_Object = MibTableColumn
hbaFcIndex = _HbaFcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 1, 1, 1),
    _HbaFcIndex_Type()
)
hbaFcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbaFcIndex.setStatus("current")


class _HbaFcPort_Type(Integer32):
    """Custom type hbaFcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HbaFcPort_Type.__name__ = "Integer32"
_HbaFcPort_Object = MibTableColumn
hbaFcPort = _HbaFcPort_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 1, 1, 2),
    _HbaFcPort_Type()
)
hbaFcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaFcPort.setStatus("current")


class _HbaFcState_Type(Integer32):
    """Custom type hbaFcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2))
    )


_HbaFcState_Type.__name__ = "Integer32"
_HbaFcState_Object = MibTableColumn
hbaFcState = _HbaFcState_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 1, 1, 3),
    _HbaFcState_Type()
)
hbaFcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaFcState.setStatus("current")
_HbaPathTable_Object = MibTable
hbaPathTable = _HbaPathTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2)
)
if mibBuilder.loadTexts:
    hbaPathTable.setStatus("current")
_HbaPathEntry_Object = MibTableRow
hbaPathEntry = _HbaPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1)
)
hbaPathEntry.setIndexNames(
    (0, "ENDACE-HBA-MIB", "hbaPathLunIndex"),
    (0, "ENDACE-HBA-MIB", "hbaPathIndex"),
)
if mibBuilder.loadTexts:
    hbaPathEntry.setStatus("current")


class _HbaPathLunIndex_Type(Integer32):
    """Custom type hbaPathLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HbaPathLunIndex_Type.__name__ = "Integer32"
_HbaPathLunIndex_Object = MibTableColumn
hbaPathLunIndex = _HbaPathLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 1),
    _HbaPathLunIndex_Type()
)
hbaPathLunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbaPathLunIndex.setStatus("current")


class _HbaPathIndex_Type(Integer32):
    """Custom type hbaPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HbaPathIndex_Type.__name__ = "Integer32"
_HbaPathIndex_Object = MibTableColumn
hbaPathIndex = _HbaPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 2),
    _HbaPathIndex_Type()
)
hbaPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbaPathIndex.setStatus("current")


class _HbaPathLun_Type(Integer32):
    """Custom type hbaPathLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HbaPathLun_Type.__name__ = "Integer32"
_HbaPathLun_Object = MibTableColumn
hbaPathLun = _HbaPathLun_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 3),
    _HbaPathLun_Type()
)
hbaPathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaPathLun.setStatus("current")


class _HbaPathNumber_Type(Integer32):
    """Custom type hbaPathNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HbaPathNumber_Type.__name__ = "Integer32"
_HbaPathNumber_Object = MibTableColumn
hbaPathNumber = _HbaPathNumber_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 4),
    _HbaPathNumber_Type()
)
hbaPathNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaPathNumber.setStatus("current")


class _HbaPathScsiId_Type(DisplayString):
    """Custom type hbaPathScsiId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HbaPathScsiId_Type.__name__ = "DisplayString"
_HbaPathScsiId_Object = MibTableColumn
hbaPathScsiId = _HbaPathScsiId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 5),
    _HbaPathScsiId_Type()
)
hbaPathScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaPathScsiId.setStatus("current")


class _HbaPathState_Type(Integer32):
    """Custom type hbaPathState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2))
    )


_HbaPathState_Type.__name__ = "Integer32"
_HbaPathState_Object = MibTableColumn
hbaPathState = _HbaPathState_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 6),
    _HbaPathState_Type()
)
hbaPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaPathState.setStatus("current")


class _HbaPathWwn_Type(DisplayString):
    """Custom type hbaPathWwn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HbaPathWwn_Type.__name__ = "DisplayString"
_HbaPathWwn_Object = MibTableColumn
hbaPathWwn = _HbaPathWwn_Object(
    (1, 3, 6, 1, 4, 1, 18418, 14, 1, 2, 1, 7),
    _HbaPathWwn_Type()
)
hbaPathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaPathWwn.setStatus("current")
_HbaConformance_ObjectIdentity = ObjectIdentity
hbaConformance = _HbaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2)
)
_HbaCompliances_ObjectIdentity = ObjectIdentity
hbaCompliances = _HbaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2, 1)
)
_HbaGroups_ObjectIdentity = ObjectIdentity
hbaGroups = _HbaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2, 2)
)

# Managed Objects groups

hbaObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2, 2, 1)
)
hbaObjectGroup.setObjects(
      *(("ENDACE-HBA-MIB", "hbaFcPort"),
        ("ENDACE-HBA-MIB", "hbaFcState"),
        ("ENDACE-HBA-MIB", "hbaPathLun"),
        ("ENDACE-HBA-MIB", "hbaPathNumber"),
        ("ENDACE-HBA-MIB", "hbaPathScsiId"),
        ("ENDACE-HBA-MIB", "hbaPathState"),
        ("ENDACE-HBA-MIB", "hbaPathWwn"))
)
if mibBuilder.loadTexts:
    hbaObjectGroup.setStatus("current")


# Notification objects

hbaFcStateLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 14, 0, 1)
)
hbaFcStateLinkUp.setObjects(
    ("ENDACE-HBA-MIB", "hbaFcPort")
)
if mibBuilder.loadTexts:
    hbaFcStateLinkUp.setStatus(
        "current"
    )

hbaFcStateLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 14, 0, 2)
)
hbaFcStateLinkDown.setObjects(
    ("ENDACE-HBA-MIB", "hbaFcPort")
)
if mibBuilder.loadTexts:
    hbaFcStateLinkDown.setStatus(
        "current"
    )

hbaPathStateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 14, 0, 3)
)
hbaPathStateOk.setObjects(
      *(("ENDACE-HBA-MIB", "hbaPathScsiId"),
        ("ENDACE-HBA-MIB", "hbaPathWwn"))
)
if mibBuilder.loadTexts:
    hbaPathStateOk.setStatus(
        "current"
    )

hbaPathStateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 14, 0, 4)
)
hbaPathStateError.setObjects(
      *(("ENDACE-HBA-MIB", "hbaPathScsiId"),
        ("ENDACE-HBA-MIB", "hbaPathWwn"))
)
if mibBuilder.loadTexts:
    hbaPathStateError.setStatus(
        "current"
    )


# Notifications groups

hbaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2, 2, 2)
)
hbaNotificationGroup.setObjects(
      *(("ENDACE-HBA-MIB", "hbaFcStateLinkDown"),
        ("ENDACE-HBA-MIB", "hbaFcStateLinkUp"),
        ("ENDACE-HBA-MIB", "hbaPathStateError"),
        ("ENDACE-HBA-MIB", "hbaPathStateOk"))
)
if mibBuilder.loadTexts:
    hbaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hbaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 14, 2, 1, 1)
)
hbaCompliance.setObjects(
      *(("ENDACE-HBA-MIB", "hbaObjectGroup"),
        ("ENDACE-HBA-MIB", "hbaNotificationGroup"))
)
if mibBuilder.loadTexts:
    hbaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-HBA-MIB",
    **{"hbaMIB": hbaMIB,
       "hbaNotifications": hbaNotifications,
       "hbaFcStateLinkUp": hbaFcStateLinkUp,
       "hbaFcStateLinkDown": hbaFcStateLinkDown,
       "hbaPathStateOk": hbaPathStateOk,
       "hbaPathStateError": hbaPathStateError,
       "hbaObjects": hbaObjects,
       "hbaFcTable": hbaFcTable,
       "hbaFcEntry": hbaFcEntry,
       "hbaFcIndex": hbaFcIndex,
       "hbaFcPort": hbaFcPort,
       "hbaFcState": hbaFcState,
       "hbaPathTable": hbaPathTable,
       "hbaPathEntry": hbaPathEntry,
       "hbaPathLunIndex": hbaPathLunIndex,
       "hbaPathIndex": hbaPathIndex,
       "hbaPathLun": hbaPathLun,
       "hbaPathNumber": hbaPathNumber,
       "hbaPathScsiId": hbaPathScsiId,
       "hbaPathState": hbaPathState,
       "hbaPathWwn": hbaPathWwn,
       "hbaConformance": hbaConformance,
       "hbaCompliances": hbaCompliances,
       "hbaCompliance": hbaCompliance,
       "hbaGroups": hbaGroups,
       "hbaObjectGroup": hbaObjectGroup,
       "hbaNotificationGroup": hbaNotificationGroup}
)
