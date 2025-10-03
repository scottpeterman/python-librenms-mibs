# SNMP MIB module (SONICWALL-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sonicwall\SONICWALL-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:44 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sonicwall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741)
)
if mibBuilder.loadTexts:
    sonicwall.setRevisions(
        ("2017-01-06 00:00",
         "2007-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonicwallFw_ObjectIdentity = ObjectIdentity
sonicwallFw = _SonicwallFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1)
)
if mibBuilder.loadTexts:
    sonicwallFw.setStatus("current")
_SonicwallCommon_ObjectIdentity = ObjectIdentity
sonicwallCommon = _SonicwallCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 2)
)
if mibBuilder.loadTexts:
    sonicwallCommon.setStatus("current")
_SonicwallGMS_ObjectIdentity = ObjectIdentity
sonicwallGMS = _SonicwallGMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 3)
)
if mibBuilder.loadTexts:
    sonicwallGMS.setStatus("current")
_SonicwallEmailSec_ObjectIdentity = ObjectIdentity
sonicwallEmailSec = _SonicwallEmailSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 4)
)
if mibBuilder.loadTexts:
    sonicwallEmailSec.setStatus("current")
_SonicwallDataCenter_ObjectIdentity = ObjectIdentity
sonicwallDataCenter = _SonicwallDataCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 5)
)
if mibBuilder.loadTexts:
    sonicwallDataCenter.setStatus("current")
_SonicwallSSLVPN_ObjectIdentity = ObjectIdentity
sonicwallSSLVPN = _SonicwallSSLVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 6)
)
if mibBuilder.loadTexts:
    sonicwallSSLVPN.setStatus("current")
_SonicwallCDP_ObjectIdentity = ObjectIdentity
sonicwallCDP = _SonicwallCDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 7)
)
if mibBuilder.loadTexts:
    sonicwallCDP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SMI",
    **{"sonicwall": sonicwall,
       "sonicwallFw": sonicwallFw,
       "sonicwallCommon": sonicwallCommon,
       "sonicwallGMS": sonicwallGMS,
       "sonicwallEmailSec": sonicwallEmailSec,
       "sonicwallDataCenter": sonicwallDataCenter,
       "sonicwallSSLVPN": sonicwallSSLVPN,
       "sonicwallCDP": sonicwallCDP}
)
