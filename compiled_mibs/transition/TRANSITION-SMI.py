# SNMP MIB module (TRANSITION-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TRANSITION-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:43 2025
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

transition = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868)
)
if mibBuilder.loadTexts:
    transition.setRevisions(
        ("2013-07-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProductId_ObjectIdentity = ObjectIdentity
productId = _ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1)
)
_TnModules_ObjectIdentity = ObjectIdentity
tnModules = _TnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5)
)
if mibBuilder.loadTexts:
    tnModules.setStatus("current")
_TnIONPlatform_ObjectIdentity = ObjectIdentity
tnIONPlatform = _TnIONPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 1)
)
_TnCESwitches_ObjectIdentity = ObjectIdentity
tnCESwitches = _TnCESwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2)
)
_TnCES3280_ObjectIdentity = ObjectIdentity
tnCES3280 = _TnCES3280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 1)
)
_TnCES3280TST_ObjectIdentity = ObjectIdentity
tnCES3280TST = _TnCES3280TST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 2)
)
_TnCES3280S_ObjectIdentity = ObjectIdentity
tnCES3280S = _TnCES3280S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 3)
)
_TnCES3280STST_ObjectIdentity = ObjectIdentity
tnCES3280STST = _TnCES3280STST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 4)
)
_TnCES3290_24_ObjectIdentity = ObjectIdentity
tnCES3290_24 = _TnCES3290_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 5)
)
_TnCES3290_42_ObjectIdentity = ObjectIdentity
tnCES3290_42 = _TnCES3290_42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 6)
)
_TnCES4140_ObjectIdentity = ObjectIdentity
tnCES4140 = _TnCES4140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 20)
)
_TnCES4212_ObjectIdentity = ObjectIdentity
tnCES4212 = _TnCES4212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 21)
)
_TnCES4224_ObjectIdentity = ObjectIdentity
tnCES4224 = _TnCES4224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 2, 22)
)
_TnIndSwitches_ObjectIdentity = ObjectIdentity
tnIndSwitches = _TnIndSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 3)
)
_TnInd3280L_ObjectIdentity = ObjectIdentity
tnInd3280L = _TnInd3280L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 3, 1)
)
_TnInd3284L_ObjectIdentity = ObjectIdentity
tnInd3284L = _TnInd3284L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 3, 2)
)
_TnInd3280H_ObjectIdentity = ObjectIdentity
tnInd3280H = _TnInd3280H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 3, 3)
)
_TnInd3284H_ObjectIdentity = ObjectIdentity
tnInd3284H = _TnInd3284H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 3, 4)
)
_TnPBSwitches_ObjectIdentity = ObjectIdentity
tnPBSwitches = _TnPBSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4)
)
_TnPBPLUSTDM4AC_ObjectIdentity = ObjectIdentity
tnPBPLUSTDM4AC = _TnPBPLUSTDM4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 1)
)
_TnPBPLUSTDM4DC_ObjectIdentity = ObjectIdentity
tnPBPLUSTDM4DC = _TnPBPLUSTDM4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 2)
)
_TnPBPLUSTDM1VXAC_ObjectIdentity = ObjectIdentity
tnPBPLUSTDM1VXAC = _TnPBPLUSTDM1VXAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 3)
)
_TnPBPLUSTDM1VXDC_ObjectIdentity = ObjectIdentity
tnPBPLUSTDM1VXDC = _TnPBPLUSTDM1VXDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 4)
)
_TnPBOAMTDM16_ObjectIdentity = ObjectIdentity
tnPBOAMTDM16 = _TnPBOAMTDM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 5)
)
_TnPBTDMCONTRAAC_ObjectIdentity = ObjectIdentity
tnPBTDMCONTRAAC = _TnPBTDMCONTRAAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 6)
)
_TnPBTDMCONTRADC_ObjectIdentity = ObjectIdentity
tnPBTDMCONTRADC = _TnPBTDMCONTRADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 4, 7)
)
_TnLIBSwitches_ObjectIdentity = ObjectIdentity
tnLIBSwitches = _TnLIBSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 5)
)
_TnLIBUnoAC_ObjectIdentity = ObjectIdentity
tnLIBUnoAC = _TnLIBUnoAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 5, 1)
)
_TnLIBUnoDC_ObjectIdentity = ObjectIdentity
tnLIBUnoDC = _TnLIBUnoDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 5, 2)
)
_TnLIBMidi_ObjectIdentity = ObjectIdentity
tnLIBMidi = _TnLIBMidi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 5, 3)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2)
)
_TnProducts_ObjectIdentity = ObjectIdentity
tnProducts = _TnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5)
)
if mibBuilder.loadTexts:
    tnProducts.setStatus("current")
_TnExperimental_ObjectIdentity = ObjectIdentity
tnExperimental = _TnExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 3)
)
if mibBuilder.loadTexts:
    tnExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANSITION-SMI",
    **{"transition": transition,
       "productId": productId,
       "tnModules": tnModules,
       "tnIONPlatform": tnIONPlatform,
       "tnCESwitches": tnCESwitches,
       "tnCES3280": tnCES3280,
       "tnCES3280TST": tnCES3280TST,
       "tnCES3280S": tnCES3280S,
       "tnCES3280STST": tnCES3280STST,
       "tnCES3290-24": tnCES3290_24,
       "tnCES3290-42": tnCES3290_42,
       "tnCES4140": tnCES4140,
       "tnCES4212": tnCES4212,
       "tnCES4224": tnCES4224,
       "tnIndSwitches": tnIndSwitches,
       "tnInd3280L": tnInd3280L,
       "tnInd3284L": tnInd3284L,
       "tnInd3280H": tnInd3280H,
       "tnInd3284H": tnInd3284H,
       "tnPBSwitches": tnPBSwitches,
       "tnPBPLUSTDM4AC": tnPBPLUSTDM4AC,
       "tnPBPLUSTDM4DC": tnPBPLUSTDM4DC,
       "tnPBPLUSTDM1VXAC": tnPBPLUSTDM1VXAC,
       "tnPBPLUSTDM1VXDC": tnPBPLUSTDM1VXDC,
       "tnPBOAMTDM16": tnPBOAMTDM16,
       "tnPBTDMCONTRAAC": tnPBTDMCONTRAAC,
       "tnPBTDMCONTRADC": tnPBTDMCONTRADC,
       "tnLIBSwitches": tnLIBSwitches,
       "tnLIBUnoAC": tnLIBUnoAC,
       "tnLIBUnoDC": tnLIBUnoDC,
       "tnLIBMidi": tnLIBMidi,
       "products": products,
       "tnProducts": tnProducts,
       "tnExperimental": tnExperimental}
)
