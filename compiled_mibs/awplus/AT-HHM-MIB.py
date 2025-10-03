# SNMP MIB module (AT-HHM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-HHM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:28 2025
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

atHwHealthMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24)
)
if mibBuilder.loadTexts:
    atHwHealthMon.setRevisions(
        ("2013-06-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtHhmNotifications_ObjectIdentity = ObjectIdentity
atHhmNotifications = _AtHhmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0)
)
_AtHhmNotificationVariables_ObjectIdentity = ObjectIdentity
atHhmNotificationVariables = _AtHhmNotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1)
)


class _AtHhmLogMessage_Type(DisplayStringUnsized):
    """Custom type atHhmLogMessage based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AtHhmLogMessage_Type.__name__ = "DisplayStringUnsized"
_AtHhmLogMessage_Object = MibScalar
atHhmLogMessage = _AtHhmLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1, 1),
    _AtHhmLogMessage_Type()
)
atHhmLogMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atHhmLogMessage.setStatus("current")

# Managed Objects groups


# Notification objects

atHhmLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0, 1)
)
atHhmLogNotify.setObjects(
    ("AT-HHM-MIB", "atHhmLogMessage")
)
if mibBuilder.loadTexts:
    atHhmLogNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-HHM-MIB",
    **{"atHwHealthMon": atHwHealthMon,
       "atHhmNotifications": atHhmNotifications,
       "atHhmLogNotify": atHhmLogNotify,
       "atHhmNotificationVariables": atHhmNotificationVariables,
       "atHhmLogMessage": atHhmLogMessage}
)
