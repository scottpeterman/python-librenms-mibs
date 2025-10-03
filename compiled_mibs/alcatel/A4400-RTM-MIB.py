# SNMP MIB module (A4400-RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alcatel\A4400-RTM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:10 2025
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

(a4400CPU,) = mibBuilder.importSymbols(
    "A4400-CPU-MIB",
    "a4400CPU")

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

_IpDomainTable_Object = MibTable
ipDomainTable = _IpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3)
)
if mibBuilder.loadTexts:
    ipDomainTable.setStatus("current")
_IpDomainEntry_Object = MibTableRow
ipDomainEntry = _IpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1)
)
ipDomainEntry.setIndexNames(
    (0, "A4400-RTM-MIB", "ipDomain"),
)
if mibBuilder.loadTexts:
    ipDomainEntry.setStatus("current")
_IpDomain_Type = Integer32
_IpDomain_Object = MibTableColumn
ipDomain = _IpDomain_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 1),
    _IpDomain_Type()
)
ipDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDomain.setStatus("current")
_ConfAvailable_Type = Integer32
_ConfAvailable_Object = MibTableColumn
confAvailable = _ConfAvailable_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 2),
    _ConfAvailable_Type()
)
confAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confAvailable.setStatus("current")
_ConfBusy_Type = Integer32
_ConfBusy_Object = MibTableColumn
confBusy = _ConfBusy_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 3),
    _ConfBusy_Type()
)
confBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confBusy.setStatus("current")
_ConfOutOfOrder_Type = Integer32
_ConfOutOfOrder_Object = MibTableColumn
confOutOfOrder = _ConfOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 4),
    _ConfOutOfOrder_Type()
)
confOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confOutOfOrder.setStatus("current")
_DspRessAvailable_Type = Integer32
_DspRessAvailable_Object = MibTableColumn
dspRessAvailable = _DspRessAvailable_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 5),
    _DspRessAvailable_Type()
)
dspRessAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspRessAvailable.setStatus("current")
_DspRessBusy_Type = Integer32
_DspRessBusy_Object = MibTableColumn
dspRessBusy = _DspRessBusy_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 6),
    _DspRessBusy_Type()
)
dspRessBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspRessBusy.setStatus("current")
_DspRessOutOfService_Type = Integer32
_DspRessOutOfService_Object = MibTableColumn
dspRessOutOfService = _DspRessOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 7),
    _DspRessOutOfService_Type()
)
dspRessOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspRessOutOfService.setStatus("current")
_DspRessOverrun_Type = Integer32
_DspRessOverrun_Object = MibTableColumn
dspRessOverrun = _DspRessOverrun_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 8),
    _DspRessOverrun_Type()
)
dspRessOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspRessOverrun.setStatus("current")
_CacAllowed_Type = Integer32
_CacAllowed_Object = MibTableColumn
cacAllowed = _CacAllowed_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 9),
    _CacAllowed_Type()
)
cacAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacAllowed.setStatus("current")
_CacUsed_Type = Integer32
_CacUsed_Object = MibTableColumn
cacUsed = _CacUsed_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 10),
    _CacUsed_Type()
)
cacUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacUsed.setStatus("current")
_CacOverrun_Type = Integer32
_CacOverrun_Object = MibTableColumn
cacOverrun = _CacOverrun_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 11),
    _CacOverrun_Type()
)
cacOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacOverrun.setStatus("current")


class _PbxRole_Type(Integer32):
    """Custom type pbxRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("INDETERMINATE", 0),
          ("MAIN", 1),
          ("STAND-BY", 2),
          ("ACTIVE-PCS", 3),
          ("INACTIVE-PCS", 4))
    )


_PbxRole_Type.__name__ = "Integer32"
_PbxRole_Object = MibScalar
pbxRole = _PbxRole_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 4),
    _PbxRole_Type()
)
pbxRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxRole.setStatus("current")
_SipRegSets_Type = Integer32
_SipRegSets_Object = MibScalar
sipRegSets = _SipRegSets_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 5),
    _SipRegSets_Type()
)
sipRegSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegSets.setStatus("current")
_SipUnregSets_Type = Integer32
_SipUnregSets_Object = MibScalar
sipUnregSets = _SipUnregSets_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 6),
    _SipUnregSets_Type()
)
sipUnregSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUnregSets.setStatus("current")
_SetsInService_Type = Integer32
_SetsInService_Object = MibScalar
setsInService = _SetsInService_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 7),
    _SetsInService_Type()
)
setsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setsInService.setStatus("current")
_SetsOutOfService_Type = Integer32
_SetsOutOfService_Object = MibScalar
setsOutOfService = _SetsOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 8),
    _SetsOutOfService_Type()
)
setsOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setsOutOfService.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1)
)
trunkEntry.setIndexNames(
    (0, "A4400-RTM-MIB", "trunkid"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_Trunkid_Type = Integer32
_Trunkid_Object = MibTableColumn
trunkid = _Trunkid_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 1),
    _Trunkid_Type()
)
trunkid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkid.setStatus("current")
_Trunkname_Type = DisplayString
_Trunkname_Object = MibTableColumn
trunkname = _Trunkname_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 2),
    _Trunkname_Type()
)
trunkname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkname.setStatus("current")
_Crystalno_Type = Integer32
_Crystalno_Object = MibTableColumn
crystalno = _Crystalno_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 3),
    _Crystalno_Type()
)
crystalno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crystalno.setStatus("current")
_Couplerno_Type = Integer32
_Couplerno_Object = MibTableColumn
couplerno = _Couplerno_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 4),
    _Couplerno_Type()
)
couplerno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplerno.setStatus("current")


class _Trunktype_Type(Integer32):
    """Custom type trunktype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("BCA", 0),
          ("T2COMP", 2),
          ("T2IP", 3),
          ("T2ATM", 4),
          ("T2BBC2", 5),
          ("T2SIP", 6),
          ("T2IPPR", 7),
          ("T2", 8),
          ("MIXTE", 9),
          ("T0", 10),
          ("DPNSS", 11),
          ("DASS2", 12),
          ("BCAADDON", 13),
          ("T2HYBRID", 14),
          ("LIALDE", 15),
          ("T1", 16))
    )


_Trunktype_Type.__name__ = "Integer32"
_Trunktype_Object = MibTableColumn
trunktype = _Trunktype_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 5),
    _Trunktype_Type()
)
trunktype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunktype.setStatus("current")
_Nodepbx_Type = Integer32
_Nodepbx_Object = MibTableColumn
nodepbx = _Nodepbx_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 6),
    _Nodepbx_Type()
)
nodepbx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodepbx.setStatus("current")
_Freechan_Type = Integer32
_Freechan_Object = MibTableColumn
freechan = _Freechan_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 7),
    _Freechan_Type()
)
freechan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freechan.setStatus("current")
_Busychan_Type = Integer32
_Busychan_Object = MibTableColumn
busychan = _Busychan_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 8),
    _Busychan_Type()
)
busychan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busychan.setStatus("current")
_Ooschan_Type = Integer32
_Ooschan_Object = MibTableColumn
ooschan = _Ooschan_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 9),
    _Ooschan_Type()
)
ooschan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ooschan.setStatus("current")


class _Trunkstatus_Type(Integer32):
    """Custom type trunkstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OOS", 0),
          ("INS", 1))
    )


_Trunkstatus_Type.__name__ = "Integer32"
_Trunkstatus_Object = MibTableColumn
trunkstatus = _Trunkstatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 10),
    _Trunkstatus_Type()
)
trunkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkstatus.setStatus("current")
_Cumuloos_Type = Integer32
_Cumuloos_Object = MibTableColumn
cumuloos = _Cumuloos_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 11),
    _Cumuloos_Type()
)
cumuloos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumuloos.setStatus("current")
_Cumuloverrun_Type = Integer32
_Cumuloverrun_Object = MibTableColumn
cumuloverrun = _Cumuloverrun_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 12),
    _Cumuloverrun_Type()
)
cumuloverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumuloverrun.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A4400-RTM-MIB",
    **{"ipDomainTable": ipDomainTable,
       "ipDomainEntry": ipDomainEntry,
       "ipDomain": ipDomain,
       "confAvailable": confAvailable,
       "confBusy": confBusy,
       "confOutOfOrder": confOutOfOrder,
       "dspRessAvailable": dspRessAvailable,
       "dspRessBusy": dspRessBusy,
       "dspRessOutOfService": dspRessOutOfService,
       "dspRessOverrun": dspRessOverrun,
       "cacAllowed": cacAllowed,
       "cacUsed": cacUsed,
       "cacOverrun": cacOverrun,
       "pbxRole": pbxRole,
       "sipRegSets": sipRegSets,
       "sipUnregSets": sipUnregSets,
       "setsInService": setsInService,
       "setsOutOfService": setsOutOfService,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkid": trunkid,
       "trunkname": trunkname,
       "crystalno": crystalno,
       "couplerno": couplerno,
       "trunktype": trunktype,
       "nodepbx": nodepbx,
       "freechan": freechan,
       "busychan": busychan,
       "ooschan": ooschan,
       "trunkstatus": trunkstatus,
       "cumuloos": cumuloos,
       "cumuloverrun": cumuloverrun}
)
