# SNMP MIB module (AT-TTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-TTY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:40 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tty = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36)
)
if mibBuilder.loadTexts:
    tty.setRevisions(
        ("2006-06-28 12:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TtyTraps_ObjectIdentity = ObjectIdentity
ttyTraps = _TtyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100)
)
_LoginFailureUser_Type = DisplayString
_LoginFailureUser_Object = MibScalar
loginFailureUser = _LoginFailureUser_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 1),
    _LoginFailureUser_Type()
)
loginFailureUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureUser.setStatus("current")
_LoginFailureIPAddress_Type = IpAddress
_LoginFailureIPAddress_Object = MibScalar
loginFailureIPAddress = _LoginFailureIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 2),
    _LoginFailureIPAddress_Type()
)
loginFailureIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureIPAddress.setStatus("current")
_LoginFailureAttempts_Type = Integer32
_LoginFailureAttempts_Object = MibScalar
loginFailureAttempts = _LoginFailureAttempts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 3),
    _LoginFailureAttempts_Type()
)
loginFailureAttempts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureAttempts.setStatus("current")

# Managed Objects groups


# Notification objects

loginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 11)
)
loginFailureTrap.setObjects(
      *(("AT-TTY-MIB", "loginFailureUser"),
        ("AT-TTY-MIB", "loginFailureIPAddress"),
        ("AT-TTY-MIB", "loginFailureAttempts"))
)
if mibBuilder.loadTexts:
    loginFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-TTY-MIB",
    **{"tty": tty,
       "ttyTraps": ttyTraps,
       "loginFailureUser": loginFailureUser,
       "loginFailureIPAddress": loginFailureIPAddress,
       "loginFailureAttempts": loginFailureAttempts,
       "loginFailureTrap": loginFailureTrap}
)
