# SNMP MIB module (DELL-NETWORKING-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-NETWORKING-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:49 2025
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetSyslogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 30)
)
if mibBuilder.loadTexts:
    dellNetSyslogMib.setRevisions(
        ("2014-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetSyslogNotifications_ObjectIdentity = ObjectIdentity
dellNetSyslogNotifications = _DellNetSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 30, 1)
)
_DellNetSyslogTraps_ObjectIdentity = ObjectIdentity
dellNetSyslogTraps = _DellNetSyslogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1)
)

# Managed Objects groups


# Notification objects

dellNetSyslogServerNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetSyslogServerNotReachableTrap.setStatus(
        "current"
    )

dellNetSyslogServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 30, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetSyslogServerReachableTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-SYSLOG-MIB",
    **{"dellNetSyslogMib": dellNetSyslogMib,
       "dellNetSyslogNotifications": dellNetSyslogNotifications,
       "dellNetSyslogTraps": dellNetSyslogTraps,
       "dellNetSyslogServerNotReachableTrap": dellNetSyslogServerNotReachableTrap,
       "dellNetSyslogServerReachableTrap": dellNetSyslogServerReachableTrap}
)
