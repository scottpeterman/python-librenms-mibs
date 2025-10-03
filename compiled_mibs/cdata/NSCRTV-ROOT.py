# SNMP MIB module (NSCRTV-ROOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\NSCRTV-ROOT
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:59 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NscrtvRoot_ObjectIdentity = ObjectIdentity
nscrtvRoot = _NscrtvRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409)
)
_NscrtvHFCemsTree_ObjectIdentity = ObjectIdentity
nscrtvHFCemsTree = _NscrtvHFCemsTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1)
)
_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2)
)
_CommonIdent_ObjectIdentity = ObjectIdentity
commonIdent = _CommonIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3)
)
_TvmodIdent_ObjectIdentity = ObjectIdentity
tvmodIdent = _TvmodIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 4)
)
_QammodIdent_ObjectIdentity = ObjectIdentity
qammodIdent = _QammodIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 5)
)
_OtdIdent_ObjectIdentity = ObjectIdentity
otdIdent = _OtdIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6)
)
_OtxIdent_ObjectIdentity = ObjectIdentity
otxIdent = _OtxIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 7)
)
_UporIdent_ObjectIdentity = ObjectIdentity
uporIdent = _UporIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8)
)
_DorIdent_ObjectIdentity = ObjectIdentity
dorIdent = _DorIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 9)
)
_FnIdent_ObjectIdentity = ObjectIdentity
fnIdent = _FnIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 10)
)
_OaIdent_ObjectIdentity = ObjectIdentity
oaIdent = _OaIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11)
)
_AddIdent_ObjectIdentity = ObjectIdentity
addIdent = _AddIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 12)
)
_CacIdent_ObjectIdentity = ObjectIdentity
cacIdent = _CacIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13)
)
_LineIdent_ObjectIdentity = ObjectIdentity
lineIdent = _LineIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-ROOT",
    **{"nscrtvRoot": nscrtvRoot,
       "nscrtvHFCemsTree": nscrtvHFCemsTree,
       "propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "commonIdent": commonIdent,
       "tvmodIdent": tvmodIdent,
       "qammodIdent": qammodIdent,
       "otdIdent": otdIdent,
       "otxIdent": otxIdent,
       "uporIdent": uporIdent,
       "dorIdent": dorIdent,
       "fnIdent": fnIdent,
       "oaIdent": oaIdent,
       "addIdent": addIdent,
       "cacIdent": cacIdent,
       "lineIdent": lineIdent}
)
