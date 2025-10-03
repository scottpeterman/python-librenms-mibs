# SNMP MIB module (BENU-GENERAL-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\benuos\BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:02 2025
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

benuGeneralNotif = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 4)
)
if mibBuilder.loadTexts:
    benuGeneralNotif.setRevisions(
        ("2014-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BGeneralNotifyMIBTraps_ObjectIdentity = ObjectIdentity
bGeneralNotifyMIBTraps = _BGeneralNotifyMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 4, 0)
)
_BGeneralNotifyMIBObjects_ObjectIdentity = ObjectIdentity
bGeneralNotifyMIBObjects = _BGeneralNotifyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 4, 1)
)

# Managed Objects groups


# Notification objects

bNotifyAgentShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    bNotifyAgentShutDown.setStatus(
        "current"
    )

bNotifyAgentRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 2)
)
if mibBuilder.loadTexts:
    bNotifyAgentRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-GENERAL-NOTIFICATION-MIB",
    **{"benuGeneralNotif": benuGeneralNotif,
       "bGeneralNotifyMIBTraps": bGeneralNotifyMIBTraps,
       "bNotifyAgentShutDown": bNotifyAgentShutDown,
       "bNotifyAgentRestart": bNotifyAgentRestart,
       "bGeneralNotifyMIBObjects": bGeneralNotifyMIBObjects}
)
