# SNMP MIB module (F10-FIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\F10-FIB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:03 2025
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

(chSysCardNumber,) = mibBuilder.importSymbols(
    "F10-CHASSIS-MIB",
    "chSysCardNumber")

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

f10IpForwardMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9)
)
if mibBuilder.loadTexts:
    f10IpForwardMib.setRevisions(
        ("2007-09-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10IpForwardMibObjects_ObjectIdentity = ObjectIdentity
f10IpForwardMibObjects = _F10IpForwardMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1)
)
_F10IpForwardVersionTable_Object = MibTable
f10IpForwardVersionTable = _F10IpForwardVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    f10IpForwardVersionTable.setStatus("current")
_F10IpForwardVersionEntry_Object = MibTableRow
f10IpForwardVersionEntry = _F10IpForwardVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1)
)
f10IpForwardVersionEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
)
if mibBuilder.loadTexts:
    f10IpForwardVersionEntry.setStatus("current")
_F10IpForwardVersion_Type = Counter64
_F10IpForwardVersion_Object = MibTableColumn
f10IpForwardVersion = _F10IpForwardVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 1),
    _F10IpForwardVersion_Type()
)
f10IpForwardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpForwardVersion.setStatus("current")
_F10IpForwardTable_Object = MibTable
f10IpForwardTable = _F10IpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    f10IpForwardTable.setStatus("current")
_F10IpForwardEntry_Object = MibTableRow
f10IpForwardEntry = _F10IpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1)
)
f10IpForwardEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
    (0, "F10-FIB-MIB", "f10IpforwardDest"),
    (0, "F10-FIB-MIB", "f10IpforwardMask"),
    (0, "F10-FIB-MIB", "f10IpforwardNextHop"),
    (0, "F10-FIB-MIB", "f10IpforwardFirstHop"),
)
if mibBuilder.loadTexts:
    f10IpForwardEntry.setStatus("current")
_F10IpforwardDest_Type = IpAddress
_F10IpforwardDest_Object = MibTableColumn
f10IpforwardDest = _F10IpforwardDest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 1),
    _F10IpforwardDest_Type()
)
f10IpforwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardDest.setStatus("current")
_F10IpforwardMask_Type = IpAddress
_F10IpforwardMask_Object = MibTableColumn
f10IpforwardMask = _F10IpforwardMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 2),
    _F10IpforwardMask_Type()
)
f10IpforwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardMask.setStatus("current")
_F10IpforwardNextHop_Type = IpAddress
_F10IpforwardNextHop_Object = MibTableColumn
f10IpforwardNextHop = _F10IpforwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 3),
    _F10IpforwardNextHop_Type()
)
f10IpforwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardNextHop.setStatus("current")
_F10IpforwardFirstHop_Type = IpAddress
_F10IpforwardFirstHop_Object = MibTableColumn
f10IpforwardFirstHop = _F10IpforwardFirstHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 4),
    _F10IpforwardFirstHop_Type()
)
f10IpforwardFirstHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardFirstHop.setStatus("current")
_F10IpforwardIfIndex_Type = Integer32
_F10IpforwardIfIndex_Object = MibTableColumn
f10IpforwardIfIndex = _F10IpforwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 5),
    _F10IpforwardIfIndex_Type()
)
f10IpforwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardIfIndex.setStatus("current")
_F10IpforwardMacAddress_Type = MacAddress
_F10IpforwardMacAddress_Object = MibTableColumn
f10IpforwardMacAddress = _F10IpforwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 6),
    _F10IpforwardMacAddress_Type()
)
f10IpforwardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardMacAddress.setStatus("current")


class _F10IpforwardEgressPort_Type(OctetString):
    """Custom type f10IpforwardEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F10IpforwardEgressPort_Type.__name__ = "OctetString"
_F10IpforwardEgressPort_Object = MibTableColumn
f10IpforwardEgressPort = _F10IpforwardEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 7),
    _F10IpforwardEgressPort_Type()
)
f10IpforwardEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardEgressPort.setStatus("current")
_F10IpforwardCamIndex_Type = Integer32
_F10IpforwardCamIndex_Object = MibTableColumn
f10IpforwardCamIndex = _F10IpforwardCamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 8),
    _F10IpforwardCamIndex_Type()
)
f10IpforwardCamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardCamIndex.setStatus("current")
_F10IpForwardMibConformance_ObjectIdentity = ObjectIdentity
f10IpForwardMibConformance = _F10IpForwardMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2)
)
_F10IpForwardMibCompliances_ObjectIdentity = ObjectIdentity
f10IpForwardMibCompliances = _F10IpForwardMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1)
)
_F10IpForwardMibGroups_ObjectIdentity = ObjectIdentity
f10IpForwardMibGroups = _F10IpForwardMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2)
)

# Managed Objects groups

f10IpForwardObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2, 1)
)
f10IpForwardObjectGroup.setObjects(
      *(("F10-FIB-MIB", "f10IpForwardVersion"),
        ("F10-FIB-MIB", "f10IpforwardDest"),
        ("F10-FIB-MIB", "f10IpforwardMask"),
        ("F10-FIB-MIB", "f10IpforwardNextHop"),
        ("F10-FIB-MIB", "f10IpforwardFirstHop"),
        ("F10-FIB-MIB", "f10IpforwardIfIndex"),
        ("F10-FIB-MIB", "f10IpforwardMacAddress"),
        ("F10-FIB-MIB", "f10IpforwardEgressPort"),
        ("F10-FIB-MIB", "f10IpforwardCamIndex"))
)
if mibBuilder.loadTexts:
    f10IpForwardObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10IpForwardMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1, 1)
)
f10IpForwardMibCompliance.setObjects(
    ("F10-FIB-MIB", "f10IpForwardObjectGroup")
)
if mibBuilder.loadTexts:
    f10IpForwardMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-FIB-MIB",
    **{"f10IpForwardMib": f10IpForwardMib,
       "f10IpForwardMibObjects": f10IpForwardMibObjects,
       "f10IpForwardVersionTable": f10IpForwardVersionTable,
       "f10IpForwardVersionEntry": f10IpForwardVersionEntry,
       "f10IpForwardVersion": f10IpForwardVersion,
       "f10IpForwardTable": f10IpForwardTable,
       "f10IpForwardEntry": f10IpForwardEntry,
       "f10IpforwardDest": f10IpforwardDest,
       "f10IpforwardMask": f10IpforwardMask,
       "f10IpforwardNextHop": f10IpforwardNextHop,
       "f10IpforwardFirstHop": f10IpforwardFirstHop,
       "f10IpforwardIfIndex": f10IpforwardIfIndex,
       "f10IpforwardMacAddress": f10IpforwardMacAddress,
       "f10IpforwardEgressPort": f10IpforwardEgressPort,
       "f10IpforwardCamIndex": f10IpforwardCamIndex,
       "f10IpForwardMibConformance": f10IpForwardMibConformance,
       "f10IpForwardMibCompliances": f10IpForwardMibCompliances,
       "f10IpForwardMibCompliance": f10IpForwardMibCompliance,
       "f10IpForwardMibGroups": f10IpForwardMibGroups,
       "f10IpForwardObjectGroup": f10IpForwardObjectGroup}
)
