# SNMP MIB module (Brocade-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\Brocade-REG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:11 2025
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

bcsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588)
)
if mibBuilder.loadTexts:
    bcsi.setRevisions(
        ("2012-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommDev_ObjectIdentity = ObjectIdentity
commDev = _CommDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2)
)
if mibBuilder.loadTexts:
    commDev.setStatus("current")
_Fibrechannel_ObjectIdentity = ObjectIdentity
fibrechannel = _Fibrechannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1)
)
if mibBuilder.loadTexts:
    fibrechannel.setStatus("current")
_FcSwitch_ObjectIdentity = ObjectIdentity
fcSwitch = _FcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcSwitch.setStatus("current")
_Nos_ObjectIdentity = ObjectIdentity
nos = _Nos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2)
)
if mibBuilder.loadTexts:
    nos.setStatus("current")
_BcsiReg_ObjectIdentity = ObjectIdentity
bcsiReg = _BcsiReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3)
)
if mibBuilder.loadTexts:
    bcsiReg.setStatus("current")
_BcsiModules_ObjectIdentity = ObjectIdentity
bcsiModules = _BcsiModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1)
)
if mibBuilder.loadTexts:
    bcsiModules.setStatus("current")
_BrocadeAgentCapability_ObjectIdentity = ObjectIdentity
brocadeAgentCapability = _BrocadeAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 2)
)
if mibBuilder.loadTexts:
    brocadeAgentCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Brocade-REG-MIB",
    **{"bcsi": bcsi,
       "commDev": commDev,
       "fibrechannel": fibrechannel,
       "fcSwitch": fcSwitch,
       "nos": nos,
       "bcsiReg": bcsiReg,
       "bcsiModules": bcsiModules,
       "brocadeAgentCapability": brocadeAgentCapability}
)
