# SNMP MIB module (IRT-COMMONVARBINDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\IRT-COMMONVARBINDS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:35 2025
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

(common,) = mibBuilder.importSymbols(
    "IRT-TRANSMITTER-SMI-MIB",
    "common")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

commonVarbinds = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    commonVarbinds.setRevisions(
        ("2007-05-04 14:00",
         "2006-12-20 14:00",
         "2006-09-21 14:00",
         "2006-09-19 14:00",
         "2006-09-07 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventTimeStamp_Type = DateAndTime
_EventTimeStamp_Object = MibScalar
eventTimeStamp = _EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 2),
    _EventTimeStamp_Type()
)
eventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTimeStamp.setStatus("current")
_EventPriority_Type = Unsigned32
_EventPriority_Object = MibScalar
eventPriority = _EventPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 3),
    _EventPriority_Type()
)
eventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventPriority.setStatus("current")
_EventCounter_Type = Counter32
_EventCounter_Object = MibScalar
eventCounter = _EventCounter_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 4),
    _EventCounter_Type()
)
eventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCounter.setStatus("current")
_MibRelease_Type = DateAndTime
_MibRelease_Object = MibScalar
mibRelease = _MibRelease_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 5),
    _MibRelease_Type()
)
mibRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibRelease.setStatus("current")

# Managed Objects groups

objectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 1)
)
objectGroup.setObjects(
      *(("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-COMMONVARBINDS-MIB", "mibRelease"))
)
if mibBuilder.loadTexts:
    objectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

commonVarbindsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 6)
)
commonVarbindsCompliance.setObjects(
    ("IRT-COMMONVARBINDS-MIB", "objectGroup")
)
if mibBuilder.loadTexts:
    commonVarbindsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IRT-COMMONVARBINDS-MIB",
    **{"commonVarbinds": commonVarbinds,
       "objectGroup": objectGroup,
       "eventTimeStamp": eventTimeStamp,
       "eventPriority": eventPriority,
       "eventCounter": eventCounter,
       "mibRelease": mibRelease,
       "commonVarbindsCompliance": commonVarbindsCompliance}
)
