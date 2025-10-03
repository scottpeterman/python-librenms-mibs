# SNMP MIB module (STORMSHIELD-IPSEC-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:09 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsIPSECStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13)
)
if mibBuilder.loadTexts:
    snsIPSECStats.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsIPSECStatsSPD_ObjectIdentity = ObjectIdentity
snsIPSECStatsSPD = _SnsIPSECStatsSPD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 1)
)
_SnsIPSECStatsSPDIn_Type = Counter64
_SnsIPSECStatsSPDIn_Object = MibScalar
snsIPSECStatsSPDIn = _SnsIPSECStatsSPDIn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 1),
    _SnsIPSECStatsSPDIn_Type()
)
snsIPSECStatsSPDIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSPDIn.setStatus("current")
_SnsIPSECStatsSPDOut_Type = Counter64
_SnsIPSECStatsSPDOut_Object = MibScalar
snsIPSECStatsSPDOut = _SnsIPSECStatsSPDOut_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 2),
    _SnsIPSECStatsSPDOut_Type()
)
snsIPSECStatsSPDOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSPDOut.setStatus("current")
_SnsIPSECStatsSAD_ObjectIdentity = ObjectIdentity
snsIPSECStatsSAD = _SnsIPSECStatsSAD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 2)
)
_SnsIPSECStatsSADLarval_Type = Counter64
_SnsIPSECStatsSADLarval_Object = MibScalar
snsIPSECStatsSADLarval = _SnsIPSECStatsSADLarval_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 1),
    _SnsIPSECStatsSADLarval_Type()
)
snsIPSECStatsSADLarval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSADLarval.setStatus("current")
_SnsIPSECStatsSADMature_Type = Counter64
_SnsIPSECStatsSADMature_Object = MibScalar
snsIPSECStatsSADMature = _SnsIPSECStatsSADMature_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 2),
    _SnsIPSECStatsSADMature_Type()
)
snsIPSECStatsSADMature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSADMature.setStatus("current")
_SnsIPSECStatsSADDying_Type = Counter64
_SnsIPSECStatsSADDying_Object = MibScalar
snsIPSECStatsSADDying = _SnsIPSECStatsSADDying_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 3),
    _SnsIPSECStatsSADDying_Type()
)
snsIPSECStatsSADDying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSADDying.setStatus("current")
_SnsIPSECStatsSADDead_Type = Counter64
_SnsIPSECStatsSADDead_Object = MibScalar
snsIPSECStatsSADDead = _SnsIPSECStatsSADDead_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 4),
    _SnsIPSECStatsSADDead_Type()
)
snsIPSECStatsSADDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsIPSECStatsSADDead.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-IPSEC-STATS-MIB",
    **{"snsIPSECStats": snsIPSECStats,
       "snsIPSECStatsSPD": snsIPSECStatsSPD,
       "snsIPSECStatsSPDIn": snsIPSECStatsSPDIn,
       "snsIPSECStatsSPDOut": snsIPSECStatsSPDOut,
       "snsIPSECStatsSAD": snsIPSECStatsSAD,
       "snsIPSECStatsSADLarval": snsIPSECStatsSADLarval,
       "snsIPSECStatsSADMature": snsIPSECStatsSADMature,
       "snsIPSECStatsSADDying": snsIPSECStatsSADDying,
       "snsIPSECStatsSADDead": snsIPSECStatsSADDead}
)
