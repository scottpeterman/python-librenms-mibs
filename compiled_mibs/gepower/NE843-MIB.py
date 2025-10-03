# SNMP MIB module (NE843-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gepower\NE843-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:40 2025
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

ne843 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ne843.setRevisions(
        ("2016-01-12 16:48",
         "2015-10-30 19:50",
         "2015-03-27 21:38",
         "2014-12-15 23:01",
         "2014-10-22 20:33",
         "2014-06-10 14:41",
         "2014-05-21 18:44",
         "2014-03-18 19:52",
         "2012-10-03 21:43",
         "2010-06-28 14:08",
         "2009-06-18 18:32",
         "2009-05-14 16:24",
         "2007-04-03 16:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Teps_ObjectIdentity = ObjectIdentity
teps = _Teps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520)
)
_Controllermibs_ObjectIdentity = ObjectIdentity
controllermibs = _Controllermibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2)
)
_Release_ObjectIdentity = ObjectIdentity
release = _Release_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1)
)
_Ne843Dc1_ObjectIdentity = ObjectIdentity
ne843Dc1 = _Ne843Dc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1)
)
_Ne843Dc1Ide_Type = DisplayString
_Ne843Dc1Ide_Object = MibScalar
ne843Dc1Ide = _Ne843Dc1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 1),
    _Ne843Dc1Ide_Type()
)
ne843Dc1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ide.setStatus("current")
_Ne843Dc1Des_Type = DisplayString
_Ne843Dc1Des_Object = MibScalar
ne843Dc1Des = _Ne843Dc1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 2),
    _Ne843Dc1Des_Type()
)
ne843Dc1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Des.setStatus("current")
_Ne843Dc1Typ_Type = DisplayString
_Ne843Dc1Typ_Object = MibScalar
ne843Dc1Typ = _Ne843Dc1Typ_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 3),
    _Ne843Dc1Typ_Type()
)
ne843Dc1Typ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Typ.setStatus("current")
_Ne843Dc1Vdc_Type = Integer32
_Ne843Dc1Vdc_Object = MibScalar
ne843Dc1Vdc = _Ne843Dc1Vdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 4),
    _Ne843Dc1Vdc_Type()
)
ne843Dc1Vdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Vdc.setUnits("mV")
_Ne843Dc1Adc_Type = Integer32
_Ne843Dc1Adc_Object = MibScalar
ne843Dc1Adc = _Ne843Dc1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 5),
    _Ne843Dc1Adc_Type()
)
ne843Dc1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Adc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Adc.setUnits("Amps")
_Ne843Dc1Cap_Type = Integer32
_Ne843Dc1Cap_Object = MibScalar
ne843Dc1Cap = _Ne843Dc1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 6),
    _Ne843Dc1Cap_Type()
)
ne843Dc1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Cap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Cap.setUnits("Amps")
_Ne843Dc1Olcap_Type = Integer32
_Ne843Dc1Olcap_Object = MibScalar
ne843Dc1Olcap = _Ne843Dc1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 7),
    _Ne843Dc1Olcap_Type()
)
ne843Dc1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Olcap.setUnits("Amps")
_Ne843Dc1Trd_Type = Integer32
_Ne843Dc1Trd_Object = MibScalar
ne843Dc1Trd = _Ne843Dc1Trd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 8),
    _Ne843Dc1Trd_Type()
)
ne843Dc1Trd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Trd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Trd.setUnits("Amps")
_Ne843Dc1Sht_Type = DisplayString
_Ne843Dc1Sht_Object = MibScalar
ne843Dc1Sht = _Ne843Dc1Sht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 9),
    _Ne843Dc1Sht_Type()
)
ne843Dc1Sht.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Sht.setStatus("current")
_Ne843Dc1Sha_Type = Integer32
_Ne843Dc1Sha_Object = MibScalar
ne843Dc1Sha = _Ne843Dc1Sha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 10),
    _Ne843Dc1Sha_Type()
)
ne843Dc1Sha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Sha.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Sha.setUnits("Amps")
_Ne843Dc1Stt_Type = DisplayString
_Ne843Dc1Stt_Object = MibScalar
ne843Dc1Stt = _Ne843Dc1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 11),
    _Ne843Dc1Stt_Type()
)
ne843Dc1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Stt.setStatus("current")
_Ne843Dc1Bod_Type = DisplayString
_Ne843Dc1Bod_Object = MibScalar
ne843Dc1Bod = _Ne843Dc1Bod_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 12),
    _Ne843Dc1Bod_Type()
)
ne843Dc1Bod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bod.setStatus("current")


class _Ne843Dc1Rss_Type(Integer32):
    """Custom type ne843Dc1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843Dc1Rss_Type.__name__ = "Integer32"
_Ne843Dc1Rss_Object = MibScalar
ne843Dc1Rss = _Ne843Dc1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 13),
    _Ne843Dc1Rss_Type()
)
ne843Dc1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Rss.setStatus("current")


class _Ne843Dc1Rsq_Type(Integer32):
    """Custom type ne843Dc1Rsq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Rsq_Type.__name__ = "Integer32"
_Ne843Dc1Rsq_Object = MibScalar
ne843Dc1Rsq = _Ne843Dc1Rsq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 14),
    _Ne843Dc1Rsq_Type()
)
ne843Dc1Rsq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Rsq.setStatus("current")
_Ne843Dc1Ron_Type = Integer32
_Ne843Dc1Ron_Object = MibScalar
ne843Dc1Ron = _Ne843Dc1Ron_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 15),
    _Ne843Dc1Ron_Type()
)
ne843Dc1Ron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Ron.setStatus("current")


class _Ne843Dc1Rot_Type(Integer32):
    """Custom type ne843Dc1Rot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 25000),
        ValueRangeConstraint(40000, 50000),
    )


_Ne843Dc1Rot_Type.__name__ = "Integer32"
_Ne843Dc1Rot_Object = MibScalar
ne843Dc1Rot = _Ne843Dc1Rot_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 16),
    _Ne843Dc1Rot_Type()
)
ne843Dc1Rot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Rot.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Rot.setUnits("mV")
_Ne843Dc1Nst_Type = Integer32
_Ne843Dc1Nst_Object = MibScalar
ne843Dc1Nst = _Ne843Dc1Nst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 17),
    _Ne843Dc1Nst_Type()
)
ne843Dc1Nst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Nst.setStatus("current")
_Ne843Dc1Cps_Type = Integer32
_Ne843Dc1Cps_Object = MibScalar
ne843Dc1Cps = _Ne843Dc1Cps_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 18),
    _Ne843Dc1Cps_Type()
)
ne843Dc1Cps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Cps.setStatus("current")
_Ne843Dc1Bty_Type = DisplayString
_Ne843Dc1Bty_Object = MibScalar
ne843Dc1Bty = _Ne843Dc1Bty_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 19),
    _Ne843Dc1Bty_Type()
)
ne843Dc1Bty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bty.setStatus("current")


class _Ne843Dc1Isd_Type(Integer32):
    """Custom type ne843Dc1Isd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Isd_Type.__name__ = "Integer32"
_Ne843Dc1Isd_Object = MibScalar
ne843Dc1Isd = _Ne843Dc1Isd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 20),
    _Ne843Dc1Isd_Type()
)
ne843Dc1Isd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Isd.setStatus("current")
_Ne843Dc1Rtm_Type = DisplayString
_Ne843Dc1Rtm_Object = MibScalar
ne843Dc1Rtm = _Ne843Dc1Rtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 21),
    _Ne843Dc1Rtm_Type()
)
ne843Dc1Rtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rtm.setStatus("current")
_Ne843Dc1Scap_Type = Integer32
_Ne843Dc1Scap_Object = MibScalar
ne843Dc1Scap = _Ne843Dc1Scap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 22),
    _Ne843Dc1Scap_Type()
)
ne843Dc1Scap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Scap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Scap.setUnits("Amps")


class _Ne843Dc1Mls_Type(Integer32):
    """Custom type ne843Dc1Mls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Mls_Type.__name__ = "Integer32"
_Ne843Dc1Mls_Object = MibScalar
ne843Dc1Mls = _Ne843Dc1Mls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 23),
    _Ne843Dc1Mls_Type()
)
ne843Dc1Mls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Mls.setStatus("current")
_Ne843Dc1Amj_Type = DisplayString
_Ne843Dc1Amj_Object = MibScalar
ne843Dc1Amj = _Ne843Dc1Amj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 24),
    _Ne843Dc1Amj_Type()
)
ne843Dc1Amj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Amj.setStatus("current")
_Ne843Dc1Vsf_Type = DisplayString
_Ne843Dc1Vsf_Object = MibScalar
ne843Dc1Vsf = _Ne843Dc1Vsf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 25),
    _Ne843Dc1Vsf_Type()
)
ne843Dc1Vsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vsf.setStatus("current")
_Ne843Dc1Osa_Type = DisplayString
_Ne843Dc1Osa_Object = MibScalar
ne843Dc1Osa = _Ne843Dc1Osa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 26),
    _Ne843Dc1Osa_Type()
)
ne843Dc1Osa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Osa.setStatus("current")
_Ne843Dc1Zid_Type = DisplayString
_Ne843Dc1Zid_Object = MibScalar
ne843Dc1Zid = _Ne843Dc1Zid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 27),
    _Ne843Dc1Zid_Type()
)
ne843Dc1Zid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Zid.setStatus("current")
_Ne843Dc1Tpa_Type = DisplayString
_Ne843Dc1Tpa_Object = MibScalar
ne843Dc1Tpa = _Ne843Dc1Tpa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 28),
    _Ne843Dc1Tpa_Type()
)
ne843Dc1Tpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Tpa.setStatus("current")
_Ne843Dc1Vmf_Type = DisplayString
_Ne843Dc1Vmf_Object = MibScalar
ne843Dc1Vmf = _Ne843Dc1Vmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 29),
    _Ne843Dc1Vmf_Type()
)
ne843Dc1Vmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vmf.setStatus("current")
_Ne843Dc1Cma_Type = DisplayString
_Ne843Dc1Cma_Object = MibScalar
ne843Dc1Cma = _Ne843Dc1Cma_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 30),
    _Ne843Dc1Cma_Type()
)
ne843Dc1Cma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Cma.setStatus("current")
_Ne843Dc1Mcm_Type = DisplayString
_Ne843Dc1Mcm_Object = MibScalar
ne843Dc1Mcm = _Ne843Dc1Mcm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 31),
    _Ne843Dc1Mcm_Type()
)
ne843Dc1Mcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Mcm.setStatus("current")
_Ne843Dc1Epo_Type = DisplayString
_Ne843Dc1Epo_Object = MibScalar
ne843Dc1Epo = _Ne843Dc1Epo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 32),
    _Ne843Dc1Epo_Type()
)
ne843Dc1Epo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Epo.setStatus("current")
_Ne843Dc1Icr_Type = DisplayString
_Ne843Dc1Icr_Object = MibScalar
ne843Dc1Icr = _Ne843Dc1Icr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 33),
    _Ne843Dc1Icr_Type()
)
ne843Dc1Icr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Icr.setStatus("current")
_Ne843Dc1Rfa_Type = DisplayString
_Ne843Dc1Rfa_Object = MibScalar
ne843Dc1Rfa = _Ne843Dc1Rfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 34),
    _Ne843Dc1Rfa_Type()
)
ne843Dc1Rfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rfa.setStatus("current")
_Ne843Dc1Acf_Type = DisplayString
_Ne843Dc1Acf_Object = MibScalar
ne843Dc1Acf = _Ne843Dc1Acf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 35),
    _Ne843Dc1Acf_Type()
)
ne843Dc1Acf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Acf.setStatus("current")
_Ne843Dc1Man_Type = DisplayString
_Ne843Dc1Man_Object = MibScalar
ne843Dc1Man = _Ne843Dc1Man_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 36),
    _Ne843Dc1Man_Type()
)
ne843Dc1Man.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Man.setStatus("current")
_Ne843Dc1Did_Type = DisplayString
_Ne843Dc1Did_Object = MibScalar
ne843Dc1Did = _Ne843Dc1Did_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 37),
    _Ne843Dc1Did_Type()
)
ne843Dc1Did.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Did.setStatus("current")
_Ne843Dc1Clm_Type = DisplayString
_Ne843Dc1Clm_Object = MibScalar
ne843Dc1Clm = _Ne843Dc1Clm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 38),
    _Ne843Dc1Clm_Type()
)
ne843Dc1Clm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Clm.setStatus("current")
_Ne843Dc1Rfn_Type = DisplayString
_Ne843Dc1Rfn_Object = MibScalar
ne843Dc1Rfn = _Ne843Dc1Rfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 39),
    _Ne843Dc1Rfn_Type()
)
ne843Dc1Rfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rfn.setStatus("current")
_Ne843Dc1Vla_Type = DisplayString
_Ne843Dc1Vla_Object = MibScalar
ne843Dc1Vla = _Ne843Dc1Vla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 40),
    _Ne843Dc1Vla_Type()
)
ne843Dc1Vla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vla.setStatus("current")
_Ne843Dc1Mfa_Type = DisplayString
_Ne843Dc1Mfa_Object = MibScalar
ne843Dc1Mfa = _Ne843Dc1Mfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 41),
    _Ne843Dc1Mfa_Type()
)
ne843Dc1Mfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Mfa.setStatus("current")
_Ne843Dc1Rtl_Type = DisplayString
_Ne843Dc1Rtl_Object = MibScalar
ne843Dc1Rtl = _Ne843Dc1Rtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 42),
    _Ne843Dc1Rtl_Type()
)
ne843Dc1Rtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rtl.setStatus("current")
_Ne843Dc1Rrtl_Type = DisplayString
_Ne843Dc1Rrtl_Object = MibScalar
ne843Dc1Rrtl = _Ne843Dc1Rrtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 43),
    _Ne843Dc1Rrtl_Type()
)
ne843Dc1Rrtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rrtl.setStatus("current")
_Ne843Dc1Rls_Type = DisplayString
_Ne843Dc1Rls_Object = MibScalar
ne843Dc1Rls = _Ne843Dc1Rls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 44),
    _Ne843Dc1Rls_Type()
)
ne843Dc1Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rls.setStatus("current")
_Ne843Dc1Mman_Type = DisplayString
_Ne843Dc1Mman_Object = MibScalar
ne843Dc1Mman = _Ne843Dc1Mman_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 45),
    _Ne843Dc1Mman_Type()
)
ne843Dc1Mman.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Mman.setStatus("current")
_Ne843Dc1Macf_Type = DisplayString
_Ne843Dc1Macf_Object = MibScalar
ne843Dc1Macf = _Ne843Dc1Macf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 46),
    _Ne843Dc1Macf_Type()
)
ne843Dc1Macf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Macf.setStatus("current")
_Ne843Dc1Bda_Type = DisplayString
_Ne843Dc1Bda_Object = MibScalar
ne843Dc1Bda = _Ne843Dc1Bda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 47),
    _Ne843Dc1Bda_Type()
)
ne843Dc1Bda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bda.setStatus("current")
_Ne843Dc1Hva_Type = DisplayString
_Ne843Dc1Hva_Object = MibScalar
ne843Dc1Hva = _Ne843Dc1Hva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 48),
    _Ne843Dc1Hva_Type()
)
ne843Dc1Hva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Hva.setStatus("current")
_Ne843Dc1Hfv_Type = DisplayString
_Ne843Dc1Hfv_Object = MibScalar
ne843Dc1Hfv = _Ne843Dc1Hfv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 49),
    _Ne843Dc1Hfv_Type()
)
ne843Dc1Hfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Hfv.setStatus("current")
_Ne843Dc1Bdt_Type = DisplayString
_Ne843Dc1Bdt_Object = MibScalar
ne843Dc1Bdt = _Ne843Dc1Bdt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 50),
    _Ne843Dc1Bdt_Type()
)
ne843Dc1Bdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bdt.setStatus("current")
_Ne843Dc1Ems_Type = DisplayString
_Ne843Dc1Ems_Object = MibScalar
ne843Dc1Ems = _Ne843Dc1Ems_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 51),
    _Ne843Dc1Ems_Type()
)
ne843Dc1Ems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ems.setStatus("current")


class _Ne843Dc1Eme_Type(Integer32):
    """Custom type ne843Dc1Eme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Eme_Type.__name__ = "Integer32"
_Ne843Dc1Eme_Object = MibScalar
ne843Dc1Eme = _Ne843Dc1Eme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 52),
    _Ne843Dc1Eme_Type()
)
ne843Dc1Eme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Eme.setStatus("current")


class _Ne843Dc1Emt_Type(Integer32):
    """Custom type ne843Dc1Emt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 95),
    )


_Ne843Dc1Emt_Type.__name__ = "Integer32"
_Ne843Dc1Emt_Object = MibScalar
ne843Dc1Emt = _Ne843Dc1Emt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 53),
    _Ne843Dc1Emt_Type()
)
ne843Dc1Emt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Emt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Emt.setUnits("%")


class _Ne843Dc1Emo_Type(Integer32):
    """Custom type ne843Dc1Emo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_Ne843Dc1Emo_Type.__name__ = "Integer32"
_Ne843Dc1Emo_Object = MibScalar
ne843Dc1Emo = _Ne843Dc1Emo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 54),
    _Ne843Dc1Emo_Type()
)
ne843Dc1Emo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Emo.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Emo.setUnits("%")
_Ne843Dc1Poc_Type = DisplayString
_Ne843Dc1Poc_Object = MibScalar
ne843Dc1Poc = _Ne843Dc1Poc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 55),
    _Ne843Dc1Poc_Type()
)
ne843Dc1Poc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Poc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Poc.setUnits("%")
_Ne843Dc1Emd_Type = DisplayString
_Ne843Dc1Emd_Object = MibScalar
ne843Dc1Emd = _Ne843Dc1Emd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 56),
    _Ne843Dc1Emd_Type()
)
ne843Dc1Emd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Emd.setStatus("current")
_Ne843Dc1Pfs_Type = DisplayString
_Ne843Dc1Pfs_Object = MibScalar
ne843Dc1Pfs = _Ne843Dc1Pfs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 57),
    _Ne843Dc1Pfs_Type()
)
ne843Dc1Pfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Pfs.setStatus("current")
_Ne843Dc1Rif_Type = DisplayString
_Ne843Dc1Rif_Object = MibScalar
ne843Dc1Rif = _Ne843Dc1Rif_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 58),
    _Ne843Dc1Rif_Type()
)
ne843Dc1Rif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Rif.setStatus("current")
_Ne843Dc1Lsf_Type = DisplayString
_Ne843Dc1Lsf_Object = MibScalar
ne843Dc1Lsf = _Ne843Dc1Lsf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 59),
    _Ne843Dc1Lsf_Type()
)
ne843Dc1Lsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Lsf.setStatus("current")


class _Ne843Dc1Emi_Type(Integer32):
    """Custom type ne843Dc1Emi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Ne843Dc1Emi_Type.__name__ = "Integer32"
_Ne843Dc1Emi_Object = MibScalar
ne843Dc1Emi = _Ne843Dc1Emi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 60),
    _Ne843Dc1Emi_Type()
)
ne843Dc1Emi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Emi.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Emi.setUnits("Minutes")


class _Ne843Dc1Emw_Type(Integer32):
    """Custom type ne843Dc1Emw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Ne843Dc1Emw_Type.__name__ = "Integer32"
_Ne843Dc1Emw_Object = MibScalar
ne843Dc1Emw = _Ne843Dc1Emw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 61),
    _Ne843Dc1Emw_Type()
)
ne843Dc1Emw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Emw.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Emw.setUnits("Minutes")


class _Ne843Dc1Aseq_Type(Integer32):
    """Custom type ne843Dc1Aseq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Aseq_Type.__name__ = "Integer32"
_Ne843Dc1Aseq_Object = MibScalar
ne843Dc1Aseq = _Ne843Dc1Aseq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 62),
    _Ne843Dc1Aseq_Type()
)
ne843Dc1Aseq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Aseq.setStatus("current")


class _Ne843Dc1Isy_Type(Integer32):
    """Custom type ne843Dc1Isy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_Ne843Dc1Isy_Type.__name__ = "Integer32"
_Ne843Dc1Isy_Object = MibScalar
ne843Dc1Isy = _Ne843Dc1Isy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 63),
    _Ne843Dc1Isy_Type()
)
ne843Dc1Isy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Isy.setStatus("current")


class _Ne843Dc1Bofe_Type(Integer32):
    """Custom type ne843Dc1Bofe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Dc1Bofe_Type.__name__ = "Integer32"
_Ne843Dc1Bofe_Object = MibScalar
ne843Dc1Bofe = _Ne843Dc1Bofe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 64),
    _Ne843Dc1Bofe_Type()
)
ne843Dc1Bofe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Dc1Bofe.setStatus("current")
_Ne843Dc1Bof_Type = DisplayString
_Ne843Dc1Bof_Object = MibScalar
ne843Dc1Bof = _Ne843Dc1Bof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 65),
    _Ne843Dc1Bof_Type()
)
ne843Dc1Bof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bof.setStatus("current")
_Ne843Dc1Sof_Type = DisplayString
_Ne843Dc1Sof_Object = MibScalar
ne843Dc1Sof = _Ne843Dc1Sof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 66),
    _Ne843Dc1Sof_Type()
)
ne843Dc1Sof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Sof.setStatus("current")
_Ne843Dc1Der_Type = DisplayString
_Ne843Dc1Der_Object = MibScalar
ne843Dc1Der = _Ne843Dc1Der_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 67),
    _Ne843Dc1Der_Type()
)
ne843Dc1Der.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Der.setStatus("current")
_Ne843Dc1Pmf_Type = DisplayString
_Ne843Dc1Pmf_Object = MibScalar
ne843Dc1Pmf = _Ne843Dc1Pmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 68),
    _Ne843Dc1Pmf_Type()
)
ne843Dc1Pmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Pmf.setStatus("current")
_Ne843Dc1Faja_Type = DisplayString
_Ne843Dc1Faja_Object = MibScalar
ne843Dc1Faja = _Ne843Dc1Faja_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 69),
    _Ne843Dc1Faja_Type()
)
ne843Dc1Faja.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Faja.setStatus("current")
_Ne843Dc1Buht_Type = DisplayString
_Ne843Dc1Buht_Object = MibScalar
ne843Dc1Buht = _Ne843Dc1Buht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 70),
    _Ne843Dc1Buht_Type()
)
ne843Dc1Buht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Buht.setStatus("current")
_Ne843Dc1Buvht_Type = DisplayString
_Ne843Dc1Buvht_Object = MibScalar
ne843Dc1Buvht = _Ne843Dc1Buvht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 71),
    _Ne843Dc1Buvht_Type()
)
ne843Dc1Buvht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Buvht.setStatus("current")
_Ne843Dc1Btha_Type = DisplayString
_Ne843Dc1Btha_Object = MibScalar
ne843Dc1Btha = _Ne843Dc1Btha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 72),
    _Ne843Dc1Btha_Type()
)
ne843Dc1Btha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Btha.setStatus("current")
_Ne843Dc1Btvh_Type = DisplayString
_Ne843Dc1Btvh_Object = MibScalar
ne843Dc1Btvh = _Ne843Dc1Btvh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 73),
    _Ne843Dc1Btvh_Type()
)
ne843Dc1Btvh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Btvh.setStatus("current")
_Ne843Dc1Btla_Type = DisplayString
_Ne843Dc1Btla_Object = MibScalar
ne843Dc1Btla = _Ne843Dc1Btla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 74),
    _Ne843Dc1Btla_Type()
)
ne843Dc1Btla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Btla.setStatus("current")
_Ne843Dc1Btvl_Type = DisplayString
_Ne843Dc1Btvl_Object = MibScalar
ne843Dc1Btvl = _Ne843Dc1Btvl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 75),
    _Ne843Dc1Btvl_Type()
)
ne843Dc1Btvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Btvl.setStatus("current")
_Ne843Dc1Laht_Type = DisplayString
_Ne843Dc1Laht_Object = MibScalar
ne843Dc1Laht = _Ne843Dc1Laht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 76),
    _Ne843Dc1Laht_Type()
)
ne843Dc1Laht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Laht.setStatus("current")
_Ne843Dc1Lalt_Type = DisplayString
_Ne843Dc1Lalt_Object = MibScalar
ne843Dc1Lalt = _Ne843Dc1Lalt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 77),
    _Ne843Dc1Lalt_Type()
)
ne843Dc1Lalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Lalt.setStatus("current")
_Ne843Dc1Raht_Type = DisplayString
_Ne843Dc1Raht_Object = MibScalar
ne843Dc1Raht = _Ne843Dc1Raht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 78),
    _Ne843Dc1Raht_Type()
)
ne843Dc1Raht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Raht.setStatus("current")
_Ne843Dc1Ravht_Type = DisplayString
_Ne843Dc1Ravht_Object = MibScalar
ne843Dc1Ravht = _Ne843Dc1Ravht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 79),
    _Ne843Dc1Ravht_Type()
)
ne843Dc1Ravht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ravht.setStatus("current")
_Ne843Dc1Ralt_Type = DisplayString
_Ne843Dc1Ralt_Object = MibScalar
ne843Dc1Ralt = _Ne843Dc1Ralt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 80),
    _Ne843Dc1Ralt_Type()
)
ne843Dc1Ralt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ralt.setStatus("current")
_Ne843Dc1Vlva_Type = DisplayString
_Ne843Dc1Vlva_Object = MibScalar
ne843Dc1Vlva = _Ne843Dc1Vlva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 81),
    _Ne843Dc1Vlva_Type()
)
ne843Dc1Vlva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vlva.setStatus("current")
_Ne843Dc1Vlvb_Type = DisplayString
_Ne843Dc1Vlvb_Object = MibScalar
ne843Dc1Vlvb = _Ne843Dc1Vlvb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 82),
    _Ne843Dc1Vlvb_Type()
)
ne843Dc1Vlvb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Vlvb.setStatus("current")
_Ne843Dc1Ovla_Type = DisplayString
_Ne843Dc1Ovla_Object = MibScalar
ne843Dc1Ovla = _Ne843Dc1Ovla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 83),
    _Ne843Dc1Ovla_Type()
)
ne843Dc1Ovla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ovla.setStatus("current")
_Ne843Dc1Ovlb_Type = DisplayString
_Ne843Dc1Ovlb_Object = MibScalar
ne843Dc1Ovlb = _Ne843Dc1Ovlb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 84),
    _Ne843Dc1Ovlb_Type()
)
ne843Dc1Ovlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Ovlb.setStatus("current")
_Ne843Dc1Pcaux_Type = DisplayString
_Ne843Dc1Pcaux_Object = MibScalar
ne843Dc1Pcaux = _Ne843Dc1Pcaux_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 85),
    _Ne843Dc1Pcaux_Type()
)
ne843Dc1Pcaux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Pcaux.setStatus("current")
_Ne843Dc1Slot_Type = DisplayString
_Ne843Dc1Slot_Object = MibScalar
ne843Dc1Slot = _Ne843Dc1Slot_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 86),
    _Ne843Dc1Slot_Type()
)
ne843Dc1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Slot.setStatus("current")


class _Ne843Dc1Bod1_Type(Integer32):
    """Custom type ne843Dc1Bod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Dc1Bod1_Type.__name__ = "Integer32"
_Ne843Dc1Bod1_Object = MibScalar
ne843Dc1Bod1 = _Ne843Dc1Bod1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 87),
    _Ne843Dc1Bod1_Type()
)
ne843Dc1Bod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bod1.setStatus("current")
_Ne843Dc1Bdt1_Type = Integer32
_Ne843Dc1Bdt1_Object = MibScalar
ne843Dc1Bdt1 = _Ne843Dc1Bdt1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 88),
    _Ne843Dc1Bdt1_Type()
)
ne843Dc1Bdt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Bdt1.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Bdt1.setUnits("Seconds")


class _Ne843Dc1Poc1_Type(Integer32):
    """Custom type ne843Dc1Poc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ne843Dc1Poc1_Type.__name__ = "Integer32"
_Ne843Dc1Poc1_Object = MibScalar
ne843Dc1Poc1 = _Ne843Dc1Poc1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 89),
    _Ne843Dc1Poc1_Type()
)
ne843Dc1Poc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Poc1.setStatus("current")
if mibBuilder.loadTexts:
    ne843Dc1Poc1.setUnits("%")
_Ne843Dc1Fajb_Type = DisplayString
_Ne843Dc1Fajb_Object = MibScalar
ne843Dc1Fajb = _Ne843Dc1Fajb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 90),
    _Ne843Dc1Fajb_Type()
)
ne843Dc1Fajb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Fajb.setStatus("current")
_Ne843Dc1Smw_Type = DisplayString
_Ne843Dc1Smw_Object = MibScalar
ne843Dc1Smw = _Ne843Dc1Smw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 91),
    _Ne843Dc1Smw_Type()
)
ne843Dc1Smw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Smw.setStatus("current")
_Ne843Dc1Cca_Type = DisplayString
_Ne843Dc1Cca_Object = MibScalar
ne843Dc1Cca = _Ne843Dc1Cca_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 1, 92),
    _Ne843Dc1Cca_Type()
)
ne843Dc1Cca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Dc1Cca.setStatus("current")
_Ne843Ps1_ObjectIdentity = ObjectIdentity
ne843Ps1 = _Ne843Ps1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2)
)
_Ne843Ps1Ide_Type = DisplayString
_Ne843Ps1Ide_Object = MibScalar
ne843Ps1Ide = _Ne843Ps1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 1),
    _Ne843Ps1Ide_Type()
)
ne843Ps1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ide.setStatus("current")
_Ne843Ps1Des_Type = DisplayString
_Ne843Ps1Des_Object = MibScalar
ne843Ps1Des = _Ne843Ps1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 2),
    _Ne843Ps1Des_Type()
)
ne843Ps1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Des.setStatus("current")
_Ne843Ps1Sid_Type = DisplayString
_Ne843Ps1Sid_Object = MibScalar
ne843Ps1Sid = _Ne843Ps1Sid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 3),
    _Ne843Ps1Sid_Type()
)
ne843Ps1Sid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Sid.setStatus("current")
_Ne843Ps1Sde_Type = DisplayString
_Ne843Ps1Sde_Object = MibScalar
ne843Ps1Sde = _Ne843Ps1Sde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 4),
    _Ne843Ps1Sde_Type()
)
ne843Ps1Sde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Sde.setStatus("current")
_Ne843Ps1Sys_Type = DisplayString
_Ne843Ps1Sys_Object = MibScalar
ne843Ps1Sys = _Ne843Ps1Sys_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 5),
    _Ne843Ps1Sys_Type()
)
ne843Ps1Sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Sys.setStatus("current")
_Ne843Ps1Swv_Type = DisplayString
_Ne843Ps1Swv_Object = MibScalar
ne843Ps1Swv = _Ne843Ps1Swv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 6),
    _Ne843Ps1Swv_Type()
)
ne843Ps1Swv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Swv.setStatus("current")
_Ne843Ps1Verw_Type = DisplayString
_Ne843Ps1Verw_Object = MibScalar
ne843Ps1Verw = _Ne843Ps1Verw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 7),
    _Ne843Ps1Verw_Type()
)
ne843Ps1Verw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Verw.setStatus("current")
_Ne843Ps1Verb_Type = DisplayString
_Ne843Ps1Verb_Object = MibScalar
ne843Ps1Verb = _Ne843Ps1Verb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 8),
    _Ne843Ps1Verb_Type()
)
ne843Ps1Verb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Verb.setStatus("current")
_Ne843Ps1Verd_Type = DisplayString
_Ne843Ps1Verd_Object = MibScalar
ne843Ps1Verd = _Ne843Ps1Verd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 9),
    _Ne843Ps1Verd_Type()
)
ne843Ps1Verd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Verd.setStatus("current")
_Ne843Ps1Dflt_Type = DisplayString
_Ne843Ps1Dflt_Object = MibScalar
ne843Ps1Dflt = _Ne843Ps1Dflt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 10),
    _Ne843Ps1Dflt_Type()
)
ne843Ps1Dflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Dflt.setStatus("current")
_Ne843Ps1Brc_Type = DisplayString
_Ne843Ps1Brc_Object = MibScalar
ne843Ps1Brc = _Ne843Ps1Brc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 11),
    _Ne843Ps1Brc_Type()
)
ne843Ps1Brc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Brc.setStatus("current")
_Ne843Ps1Sn_Type = DisplayString
_Ne843Ps1Sn_Object = MibScalar
ne843Ps1Sn = _Ne843Ps1Sn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 12),
    _Ne843Ps1Sn_Type()
)
ne843Ps1Sn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Sn.setStatus("current")
_Ne843Ps1Dat_Type = DisplayString
_Ne843Ps1Dat_Object = MibScalar
ne843Ps1Dat = _Ne843Ps1Dat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 13),
    _Ne843Ps1Dat_Type()
)
ne843Ps1Dat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Dat.setStatus("current")
_Ne843Ps1Dtf_Type = DisplayString
_Ne843Ps1Dtf_Object = MibScalar
ne843Ps1Dtf = _Ne843Ps1Dtf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 14),
    _Ne843Ps1Dtf_Type()
)
ne843Ps1Dtf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Dtf.setStatus("current")
_Ne843Ps1Tim_Type = DisplayString
_Ne843Ps1Tim_Object = MibScalar
ne843Ps1Tim = _Ne843Ps1Tim_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 15),
    _Ne843Ps1Tim_Type()
)
ne843Ps1Tim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Tim.setStatus("current")


class _Ne843Ps1Tmf_Type(Integer32):
    """Custom type ne843Ps1Tmf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              24)
        )
    )
    namedValues = NamedValues(
        *(("h12", 12),
          ("h24", 24))
    )


_Ne843Ps1Tmf_Type.__name__ = "Integer32"
_Ne843Ps1Tmf_Object = MibScalar
ne843Ps1Tmf = _Ne843Ps1Tmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 16),
    _Ne843Ps1Tmf_Type()
)
ne843Ps1Tmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Tmf.setStatus("current")


class _Ne843Ps1Dls_Type(Integer32):
    """Custom type ne843Ps1Dls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843Ps1Dls_Type.__name__ = "Integer32"
_Ne843Ps1Dls_Object = MibScalar
ne843Ps1Dls = _Ne843Ps1Dls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 17),
    _Ne843Ps1Dls_Type()
)
ne843Ps1Dls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Dls.setStatus("current")
_Ne843Ps1Lng_Type = DisplayString
_Ne843Ps1Lng_Object = MibScalar
ne843Ps1Lng = _Ne843Ps1Lng_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 18),
    _Ne843Ps1Lng_Type()
)
ne843Ps1Lng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Lng.setStatus("current")
_Ne843Ps1Tun_Type = DisplayString
_Ne843Ps1Tun_Object = MibScalar
ne843Ps1Tun = _Ne843Ps1Tun_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 19),
    _Ne843Ps1Tun_Type()
)
ne843Ps1Tun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Tun.setStatus("current")


class _Ne843Ps1Cem_Type(Integer32):
    """Custom type ne843Ps1Cem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843Ps1Cem_Type.__name__ = "Integer32"
_Ne843Ps1Cem_Object = MibScalar
ne843Ps1Cem = _Ne843Ps1Cem_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 20),
    _Ne843Ps1Cem_Type()
)
ne843Ps1Cem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Cem.setStatus("current")


class _Ne843Ps1Fpc_Type(Integer32):
    """Custom type ne843Ps1Fpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Fpc_Type.__name__ = "Integer32"
_Ne843Ps1Fpc_Object = MibScalar
ne843Ps1Fpc = _Ne843Ps1Fpc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 21),
    _Ne843Ps1Fpc_Type()
)
ne843Ps1Fpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Fpc.setStatus("current")


class _Ne843Ps1Rrf_Type(Integer32):
    """Custom type ne843Ps1Rrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Rrf_Type.__name__ = "Integer32"
_Ne843Ps1Rrf_Object = MibScalar
ne843Ps1Rrf = _Ne843Ps1Rrf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 22),
    _Ne843Ps1Rrf_Type()
)
ne843Ps1Rrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Rrf.setStatus("current")


class _Ne843Ps1Poe_Type(Integer32):
    """Custom type ne843Ps1Poe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Poe_Type.__name__ = "Integer32"
_Ne843Ps1Poe_Object = MibScalar
ne843Ps1Poe = _Ne843Ps1Poe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 23),
    _Ne843Ps1Poe_Type()
)
ne843Ps1Poe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Poe.setStatus("current")


class _Ne843Ps1Usl_Type(Integer32):
    """Custom type ne843Ps1Usl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("uninstall", 1)
    )


_Ne843Ps1Usl_Type.__name__ = "Integer32"
_Ne843Ps1Usl_Object = MibScalar
ne843Ps1Usl = _Ne843Ps1Usl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 24),
    _Ne843Ps1Usl_Type()
)
ne843Ps1Usl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Usl.setStatus("current")


class _Ne843Ps1Usr_Type(Integer32):
    """Custom type ne843Ps1Usr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Usr_Type.__name__ = "Integer32"
_Ne843Ps1Usr_Object = MibScalar
ne843Ps1Usr = _Ne843Ps1Usr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 25),
    _Ne843Ps1Usr_Type()
)
ne843Ps1Usr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Usr.setStatus("current")
_Ne843Ps1Ptt_Type = DisplayString
_Ne843Ps1Ptt_Object = MibScalar
ne843Ps1Ptt = _Ne843Ps1Ptt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 26),
    _Ne843Ps1Ptt_Type()
)
ne843Ps1Ptt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ptt.setStatus("current")
_Ne843Ps1Amt_Type = Integer32
_Ne843Ps1Amt_Object = MibScalar
ne843Ps1Amt = _Ne843Ps1Amt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 27),
    _Ne843Ps1Amt_Type()
)
ne843Ps1Amt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Amt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Ps1Amt.setUnits("C")
_Ne843Ps1Fst_Type = DisplayString
_Ne843Ps1Fst_Object = MibScalar
ne843Ps1Fst = _Ne843Ps1Fst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 28),
    _Ne843Ps1Fst_Type()
)
ne843Ps1Fst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Fst.setStatus("current")
_Ne843Ps1Fstl_Type = DisplayString
_Ne843Ps1Fstl_Object = MibScalar
ne843Ps1Fstl = _Ne843Ps1Fstl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 29),
    _Ne843Ps1Fstl_Type()
)
ne843Ps1Fstl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Fstl.setStatus("current")


class _Ne843Ps1Fpe_Type(Integer32):
    """Custom type ne843Ps1Fpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Fpe_Type.__name__ = "Integer32"
_Ne843Ps1Fpe_Object = MibScalar
ne843Ps1Fpe = _Ne843Ps1Fpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 30),
    _Ne843Ps1Fpe_Type()
)
ne843Ps1Fpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Fpe.setStatus("current")
_Ne843Ps1Fpt_Type = Integer32
_Ne843Ps1Fpt_Object = MibScalar
ne843Ps1Fpt = _Ne843Ps1Fpt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 31),
    _Ne843Ps1Fpt_Type()
)
ne843Ps1Fpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Fpt.setStatus("current")


class _Ne843Ps1Rss_Type(Integer32):
    """Custom type ne843Ps1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_Ne843Ps1Rss_Type.__name__ = "Integer32"
_Ne843Ps1Rss_Object = MibScalar
ne843Ps1Rss = _Ne843Ps1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 32),
    _Ne843Ps1Rss_Type()
)
ne843Ps1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Rss.setStatus("current")
_Ne843Ps1Ast_Type = DisplayString
_Ne843Ps1Ast_Object = MibScalar
ne843Ps1Ast = _Ne843Ps1Ast_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 33),
    _Ne843Ps1Ast_Type()
)
ne843Ps1Ast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ast.setStatus("current")
_Ne843Ps1Dss_Type = DisplayString
_Ne843Ps1Dss_Object = MibScalar
ne843Ps1Dss = _Ne843Ps1Dss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 34),
    _Ne843Ps1Dss_Type()
)
ne843Ps1Dss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Dss.setStatus("current")
_Ne843Ps1Dse_Type = DisplayString
_Ne843Ps1Dse_Object = MibScalar
ne843Ps1Dse = _Ne843Ps1Dse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 35),
    _Ne843Ps1Dse_Type()
)
ne843Ps1Dse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Dse.setStatus("current")
_Ne843Ps1Epr_Type = DisplayString
_Ne843Ps1Epr_Object = MibScalar
ne843Ps1Epr = _Ne843Ps1Epr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 36),
    _Ne843Ps1Epr_Type()
)
ne843Ps1Epr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Epr.setStatus("current")
_Ne843Ps1Pfd_Type = DisplayString
_Ne843Ps1Pfd_Object = MibScalar
ne843Ps1Pfd = _Ne843Ps1Pfd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 37),
    _Ne843Ps1Pfd_Type()
)
ne843Ps1Pfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Pfd.setStatus("current")
_Ne843Ps1Exl_Type = DisplayString
_Ne843Ps1Exl_Object = MibScalar
ne843Ps1Exl = _Ne843Ps1Exl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 38),
    _Ne843Ps1Exl_Type()
)
ne843Ps1Exl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Exl.setStatus("current")
_Ne843Ps1Bbl_Type = DisplayString
_Ne843Ps1Bbl_Object = MibScalar
ne843Ps1Bbl = _Ne843Ps1Bbl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 39),
    _Ne843Ps1Bbl_Type()
)
ne843Ps1Bbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Bbl.setStatus("current")
_Ne843Ps1Clc_Type = DisplayString
_Ne843Ps1Clc_Object = MibScalar
ne843Ps1Clc = _Ne843Ps1Clc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 40),
    _Ne843Ps1Clc_Type()
)
ne843Ps1Clc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Clc.setStatus("current")
_Ne843Ps1Stf_Type = DisplayString
_Ne843Ps1Stf_Object = MibScalar
ne843Ps1Stf = _Ne843Ps1Stf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 41),
    _Ne843Ps1Stf_Type()
)
ne843Ps1Stf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Stf.setStatus("current")
_Ne843Ps1Pgi_Type = DisplayString
_Ne843Ps1Pgi_Object = MibScalar
ne843Ps1Pgi = _Ne843Ps1Pgi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 42),
    _Ne843Ps1Pgi_Type()
)
ne843Ps1Pgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Pgi.setStatus("current")
_Ne843Ps1Cch_Type = DisplayString
_Ne843Ps1Cch_Object = MibScalar
ne843Ps1Cch = _Ne843Ps1Cch_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 43),
    _Ne843Ps1Cch_Type()
)
ne843Ps1Cch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Cch.setStatus("current")
_Ne843Ps1Hcl_Type = DisplayString
_Ne843Ps1Hcl_Object = MibScalar
ne843Ps1Hcl = _Ne843Ps1Hcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 44),
    _Ne843Ps1Hcl_Type()
)
ne843Ps1Hcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Hcl.setStatus("current")
_Ne843Ps1Ax1_Type = DisplayString
_Ne843Ps1Ax1_Object = MibScalar
ne843Ps1Ax1 = _Ne843Ps1Ax1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 45),
    _Ne843Ps1Ax1_Type()
)
ne843Ps1Ax1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax1.setStatus("current")
_Ne843Ps1Ax2_Type = DisplayString
_Ne843Ps1Ax2_Object = MibScalar
ne843Ps1Ax2 = _Ne843Ps1Ax2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 46),
    _Ne843Ps1Ax2_Type()
)
ne843Ps1Ax2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax2.setStatus("current")
_Ne843Ps1Ax3_Type = DisplayString
_Ne843Ps1Ax3_Object = MibScalar
ne843Ps1Ax3 = _Ne843Ps1Ax3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 47),
    _Ne843Ps1Ax3_Type()
)
ne843Ps1Ax3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax3.setStatus("current")
_Ne843Ps1Ax4_Type = DisplayString
_Ne843Ps1Ax4_Object = MibScalar
ne843Ps1Ax4 = _Ne843Ps1Ax4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 48),
    _Ne843Ps1Ax4_Type()
)
ne843Ps1Ax4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax4.setStatus("current")
_Ne843Ps1Ax5_Type = DisplayString
_Ne843Ps1Ax5_Object = MibScalar
ne843Ps1Ax5 = _Ne843Ps1Ax5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 49),
    _Ne843Ps1Ax5_Type()
)
ne843Ps1Ax5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax5.setStatus("current")
_Ne843Ps1Ax6_Type = DisplayString
_Ne843Ps1Ax6_Object = MibScalar
ne843Ps1Ax6 = _Ne843Ps1Ax6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 50),
    _Ne843Ps1Ax6_Type()
)
ne843Ps1Ax6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax6.setStatus("current")
_Ne843Ps1Fan24_Type = DisplayString
_Ne843Ps1Fan24_Object = MibScalar
ne843Ps1Fan24 = _Ne843Ps1Fan24_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 51),
    _Ne843Ps1Fan24_Type()
)
ne843Ps1Fan24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Fan24.setStatus("current")
_Ne843Ps1Fan48_Type = DisplayString
_Ne843Ps1Fan48_Object = MibScalar
ne843Ps1Fan48 = _Ne843Ps1Fan48_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 52),
    _Ne843Ps1Fan48_Type()
)
ne843Ps1Fan48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Fan48.setStatus("current")
_Ne843Ps1Faj24_Type = DisplayString
_Ne843Ps1Faj24_Object = MibScalar
ne843Ps1Faj24 = _Ne843Ps1Faj24_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 53),
    _Ne843Ps1Faj24_Type()
)
ne843Ps1Faj24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Faj24.setStatus("current")
_Ne843Ps1Faj48_Type = DisplayString
_Ne843Ps1Faj48_Object = MibScalar
ne843Ps1Faj48 = _Ne843Ps1Faj48_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 54),
    _Ne843Ps1Faj48_Type()
)
ne843Ps1Faj48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Faj48.setStatus("current")
_Ne843Ps1Accl_Type = DisplayString
_Ne843Ps1Accl_Object = MibScalar
ne843Ps1Accl = _Ne843Ps1Accl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 55),
    _Ne843Ps1Accl_Type()
)
ne843Ps1Accl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Accl.setStatus("current")
_Ne843Ps1Ledl_Type = DisplayString
_Ne843Ps1Ledl_Object = MibScalar
ne843Ps1Ledl = _Ne843Ps1Ledl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 56),
    _Ne843Ps1Ledl_Type()
)
ne843Ps1Ledl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ledl.setStatus("current")
_Ne843Ps1Ax7_Type = DisplayString
_Ne843Ps1Ax7_Object = MibScalar
ne843Ps1Ax7 = _Ne843Ps1Ax7_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 57),
    _Ne843Ps1Ax7_Type()
)
ne843Ps1Ax7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax7.setStatus("current")
_Ne843Ps1Ax8_Type = DisplayString
_Ne843Ps1Ax8_Object = MibScalar
ne843Ps1Ax8 = _Ne843Ps1Ax8_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 58),
    _Ne843Ps1Ax8_Type()
)
ne843Ps1Ax8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax8.setStatus("current")
_Ne843Ps1Ax9_Type = DisplayString
_Ne843Ps1Ax9_Object = MibScalar
ne843Ps1Ax9 = _Ne843Ps1Ax9_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 59),
    _Ne843Ps1Ax9_Type()
)
ne843Ps1Ax9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax9.setStatus("current")
_Ne843Ps1Ax10_Type = DisplayString
_Ne843Ps1Ax10_Object = MibScalar
ne843Ps1Ax10 = _Ne843Ps1Ax10_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 60),
    _Ne843Ps1Ax10_Type()
)
ne843Ps1Ax10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax10.setStatus("current")
_Ne843Ps1Ax11_Type = DisplayString
_Ne843Ps1Ax11_Object = MibScalar
ne843Ps1Ax11 = _Ne843Ps1Ax11_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 61),
    _Ne843Ps1Ax11_Type()
)
ne843Ps1Ax11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax11.setStatus("current")
_Ne843Ps1Ax12_Type = DisplayString
_Ne843Ps1Ax12_Object = MibScalar
ne843Ps1Ax12 = _Ne843Ps1Ax12_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 62),
    _Ne843Ps1Ax12_Type()
)
ne843Ps1Ax12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ax12.setStatus("current")


class _Ne843Ps1Cid_Type(Integer32):
    """Custom type ne843Ps1Cid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Cid_Type.__name__ = "Integer32"
_Ne843Ps1Cid_Object = MibScalar
ne843Ps1Cid = _Ne843Ps1Cid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 63),
    _Ne843Ps1Cid_Type()
)
ne843Ps1Cid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Cid.setStatus("current")
_Ne843Ps1Lngl_Type = DisplayString
_Ne843Ps1Lngl_Object = MibScalar
ne843Ps1Lngl = _Ne843Ps1Lngl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 64),
    _Ne843Ps1Lngl_Type()
)
ne843Ps1Lngl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Lngl.setStatus("current")
_Ne843Ps1Amtl_Type = DisplayString
_Ne843Ps1Amtl_Object = MibScalar
ne843Ps1Amtl = _Ne843Ps1Amtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 65),
    _Ne843Ps1Amtl_Type()
)
ne843Ps1Amtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Amtl.setStatus("current")
_Ne843Ps1Amth_Type = DisplayString
_Ne843Ps1Amth_Object = MibScalar
ne843Ps1Amth = _Ne843Ps1Amth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 66),
    _Ne843Ps1Amth_Type()
)
ne843Ps1Amth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Amth.setStatus("current")
_Ne843Ps1Cc_Type = DisplayString
_Ne843Ps1Cc_Object = MibScalar
ne843Ps1Cc = _Ne843Ps1Cc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 67),
    _Ne843Ps1Cc_Type()
)
ne843Ps1Cc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Cc.setStatus("current")
_Ne843Ps1Clei_Type = DisplayString
_Ne843Ps1Clei_Object = MibScalar
ne843Ps1Clei = _Ne843Ps1Clei_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 68),
    _Ne843Ps1Clei_Type()
)
ne843Ps1Clei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Clei.setStatus("current")
_Ne843Ps1Ser_Type = DisplayString
_Ne843Ps1Ser_Object = MibScalar
ne843Ps1Ser = _Ne843Ps1Ser_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 69),
    _Ne843Ps1Ser_Type()
)
ne843Ps1Ser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ser.setStatus("current")
_Ne843Ps1Lamt_Type = Integer32
_Ne843Ps1Lamt_Object = MibScalar
ne843Ps1Lamt = _Ne843Ps1Lamt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 70),
    _Ne843Ps1Lamt_Type()
)
ne843Ps1Lamt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Lamt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Ps1Lamt.setUnits("C")
_Ne843Ps1Nat_Type = Integer32
_Ne843Ps1Nat_Object = MibScalar
ne843Ps1Nat = _Ne843Ps1Nat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 71),
    _Ne843Ps1Nat_Type()
)
ne843Ps1Nat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nat.setStatus("current")
_Ne843Ps1Blr_Type = DisplayString
_Ne843Ps1Blr_Object = MibScalar
ne843Ps1Blr = _Ne843Ps1Blr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 72),
    _Ne843Ps1Blr_Type()
)
ne843Ps1Blr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Blr.setStatus("current")
_Ne843Ps1Tzo_Type = Integer32
_Ne843Ps1Tzo_Object = MibScalar
ne843Ps1Tzo = _Ne843Ps1Tzo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 73),
    _Ne843Ps1Tzo_Type()
)
ne843Ps1Tzo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Tzo.setStatus("current")
if mibBuilder.loadTexts:
    ne843Ps1Tzo.setUnits("Minutes")
_Ne843Ps1Crt_Type = DisplayString
_Ne843Ps1Crt_Object = MibScalar
ne843Ps1Crt = _Ne843Ps1Crt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 74),
    _Ne843Ps1Crt_Type()
)
ne843Ps1Crt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Crt.setStatus("current")
_Ne843Ps1Nhat_Type = Integer32
_Ne843Ps1Nhat_Object = MibScalar
ne843Ps1Nhat = _Ne843Ps1Nhat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 75),
    _Ne843Ps1Nhat_Type()
)
ne843Ps1Nhat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Nhat.setStatus("current")
if mibBuilder.loadTexts:
    ne843Ps1Nhat.setUnits("C")
_Ne843Ps1Nal_Type = Integer32
_Ne843Ps1Nal_Object = MibScalar
ne843Ps1Nal = _Ne843Ps1Nal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 76),
    _Ne843Ps1Nal_Type()
)
ne843Ps1Nal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nal.setStatus("current")
_Ne843Ps1Ncr_Type = Integer32
_Ne843Ps1Ncr_Object = MibScalar
ne843Ps1Ncr = _Ne843Ps1Ncr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 77),
    _Ne843Ps1Ncr_Type()
)
ne843Ps1Ncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Ncr.setStatus("current")
_Ne843Ps1Nmj_Type = Integer32
_Ne843Ps1Nmj_Object = MibScalar
ne843Ps1Nmj = _Ne843Ps1Nmj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 78),
    _Ne843Ps1Nmj_Type()
)
ne843Ps1Nmj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nmj.setStatus("current")
_Ne843Ps1Nmn_Type = Integer32
_Ne843Ps1Nmn_Object = MibScalar
ne843Ps1Nmn = _Ne843Ps1Nmn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 79),
    _Ne843Ps1Nmn_Type()
)
ne843Ps1Nmn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nmn.setStatus("current")
_Ne843Ps1Nwa_Type = Integer32
_Ne843Ps1Nwa_Object = MibScalar
ne843Ps1Nwa = _Ne843Ps1Nwa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 80),
    _Ne843Ps1Nwa_Type()
)
ne843Ps1Nwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nwa.setStatus("current")
_Ne843Ps1Nre_Type = Integer32
_Ne843Ps1Nre_Object = MibScalar
ne843Ps1Nre = _Ne843Ps1Nre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 81),
    _Ne843Ps1Nre_Type()
)
ne843Ps1Nre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ps1Nre.setStatus("current")


class _Ne843Ps1Ere_Type(Integer32):
    """Custom type ne843Ps1Ere based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ps1Ere_Type.__name__ = "Integer32"
_Ne843Ps1Ere_Object = MibScalar
ne843Ps1Ere = _Ne843Ps1Ere_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 2, 82),
    _Ne843Ps1Ere_Type()
)
ne843Ps1Ere.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ps1Ere.setStatus("current")
_Ne843At1_ObjectIdentity = ObjectIdentity
ne843At1 = _Ne843At1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3)
)
_Ne843At1Ide_Type = DisplayString
_Ne843At1Ide_Object = MibScalar
ne843At1Ide = _Ne843At1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 1),
    _Ne843At1Ide_Type()
)
ne843At1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843At1Ide.setStatus("current")
_Ne843At1Des_Type = DisplayString
_Ne843At1Des_Object = MibScalar
ne843At1Des = _Ne843At1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 2),
    _Ne843At1Des_Type()
)
ne843At1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Des.setStatus("current")


class _Ne843At1Stt_Type(Integer32):
    """Custom type ne843At1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843At1Stt_Type.__name__ = "Integer32"
_Ne843At1Stt_Object = MibScalar
ne843At1Stt = _Ne843At1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 3),
    _Ne843At1Stt_Type()
)
ne843At1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Stt.setStatus("current")
_Ne843At1Stg_Type = DisplayString
_Ne843At1Stg_Object = MibScalar
ne843At1Stg = _Ne843At1Stg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 4),
    _Ne843At1Stg_Type()
)
ne843At1Stg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843At1Stg.setStatus("current")


class _Ne843At1Lte_Type(Integer32):
    """Custom type ne843At1Lte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843At1Lte_Type.__name__ = "Integer32"
_Ne843At1Lte_Object = MibScalar
ne843At1Lte = _Ne843At1Lte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 5),
    _Ne843At1Lte_Type()
)
ne843At1Lte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Lte.setStatus("current")


class _Ne843At1Dur_Type(Integer32):
    """Custom type ne843At1Dur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Ne843At1Dur_Type.__name__ = "Integer32"
_Ne843At1Dur_Object = MibScalar
ne843At1Dur = _Ne843At1Dur_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 6),
    _Ne843At1Dur_Type()
)
ne843At1Dur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Dur.setStatus("current")
if mibBuilder.loadTexts:
    ne843At1Dur.setUnits("Seconds")


class _Ne843At1Pcr_Type(Integer32):
    """Custom type ne843At1Pcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1Pcr_Type.__name__ = "Integer32"
_Ne843At1Pcr_Object = MibScalar
ne843At1Pcr = _Ne843At1Pcr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 7),
    _Ne843At1Pcr_Type()
)
ne843At1Pcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Pcr.setStatus("current")


class _Ne843At1Pmj_Type(Integer32):
    """Custom type ne843At1Pmj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1Pmj_Type.__name__ = "Integer32"
_Ne843At1Pmj_Object = MibScalar
ne843At1Pmj = _Ne843At1Pmj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 8),
    _Ne843At1Pmj_Type()
)
ne843At1Pmj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Pmj.setStatus("current")


class _Ne843At1Pmn_Type(Integer32):
    """Custom type ne843At1Pmn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1Pmn_Type.__name__ = "Integer32"
_Ne843At1Pmn_Object = MibScalar
ne843At1Pmn = _Ne843At1Pmn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 9),
    _Ne843At1Pmn_Type()
)
ne843At1Pmn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Pmn.setStatus("current")


class _Ne843At1R1_Type(Integer32):
    """Custom type ne843At1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R1_Type.__name__ = "Integer32"
_Ne843At1R1_Object = MibScalar
ne843At1R1 = _Ne843At1R1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 10),
    _Ne843At1R1_Type()
)
ne843At1R1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R1.setStatus("current")


class _Ne843At1R2_Type(Integer32):
    """Custom type ne843At1R2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R2_Type.__name__ = "Integer32"
_Ne843At1R2_Object = MibScalar
ne843At1R2 = _Ne843At1R2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 11),
    _Ne843At1R2_Type()
)
ne843At1R2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R2.setStatus("current")


class _Ne843At1R3_Type(Integer32):
    """Custom type ne843At1R3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R3_Type.__name__ = "Integer32"
_Ne843At1R3_Object = MibScalar
ne843At1R3 = _Ne843At1R3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 12),
    _Ne843At1R3_Type()
)
ne843At1R3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R3.setStatus("current")


class _Ne843At1R4_Type(Integer32):
    """Custom type ne843At1R4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R4_Type.__name__ = "Integer32"
_Ne843At1R4_Object = MibScalar
ne843At1R4 = _Ne843At1R4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 13),
    _Ne843At1R4_Type()
)
ne843At1R4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R4.setStatus("current")


class _Ne843At1R5_Type(Integer32):
    """Custom type ne843At1R5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R5_Type.__name__ = "Integer32"
_Ne843At1R5_Object = MibScalar
ne843At1R5 = _Ne843At1R5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 14),
    _Ne843At1R5_Type()
)
ne843At1R5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R5.setStatus("current")


class _Ne843At1R6_Type(Integer32):
    """Custom type ne843At1R6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R6_Type.__name__ = "Integer32"
_Ne843At1R6_Object = MibScalar
ne843At1R6 = _Ne843At1R6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 15),
    _Ne843At1R6_Type()
)
ne843At1R6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R6.setStatus("current")


class _Ne843At1R7_Type(Integer32):
    """Custom type ne843At1R7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843At1R7_Type.__name__ = "Integer32"
_Ne843At1R7_Object = MibScalar
ne843At1R7 = _Ne843At1R7_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 16),
    _Ne843At1R7_Type()
)
ne843At1R7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1R7.setStatus("current")


class _Ne843At1Ets_Type(Integer32):
    """Custom type ne843At1Ets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843At1Ets_Type.__name__ = "Integer32"
_Ne843At1Ets_Object = MibScalar
ne843At1Ets = _Ne843At1Ets_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 17),
    _Ne843At1Ets_Type()
)
ne843At1Ets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Ets.setStatus("current")
_Ne843At1Ems_Type = DisplayString
_Ne843At1Ems_Object = MibScalar
ne843At1Ems = _Ne843At1Ems_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 18),
    _Ne843At1Ems_Type()
)
ne843At1Ems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843At1Ems.setStatus("current")


class _Ne843At1Bzi_Type(Integer32):
    """Custom type ne843At1Bzi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Ne843At1Bzi_Type.__name__ = "Integer32"
_Ne843At1Bzi_Object = MibScalar
ne843At1Bzi = _Ne843At1Bzi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 19),
    _Ne843At1Bzi_Type()
)
ne843At1Bzi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Bzi.setStatus("current")
if mibBuilder.loadTexts:
    ne843At1Bzi.setUnits("Seconds")
_Ne843At1Bzt_Type = DisplayString
_Ne843At1Bzt_Object = MibScalar
ne843At1Bzt = _Ne843At1Bzt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 20),
    _Ne843At1Bzt_Type()
)
ne843At1Bzt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Bzt.setStatus("current")
_Ne843At1Irt_Type = DisplayString
_Ne843At1Irt_Object = MibScalar
ne843At1Irt = _Ne843At1Irt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 21),
    _Ne843At1Irt_Type()
)
ne843At1Irt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Irt.setStatus("current")
_Ne843At1Ata_Type = DisplayString
_Ne843At1Ata_Object = MibScalar
ne843At1Ata = _Ne843At1Ata_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 22),
    _Ne843At1Ata_Type()
)
ne843At1Ata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843At1Ata.setStatus("current")
_Ne843At1Atb_Type = DisplayString
_Ne843At1Atb_Object = MibScalar
ne843At1Atb = _Ne843At1Atb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 23),
    _Ne843At1Atb_Type()
)
ne843At1Atb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843At1Atb.setStatus("current")


class _Ne843At1Snt_Type(Integer32):
    """Custom type ne843At1Snt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_Ne843At1Snt_Type.__name__ = "Integer32"
_Ne843At1Snt_Object = MibScalar
ne843At1Snt = _Ne843At1Snt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 3, 24),
    _Ne843At1Snt_Type()
)
ne843At1Snt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843At1Snt.setStatus("current")
_Ne843TrsTable_Object = MibTable
ne843TrsTable = _Ne843TrsTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ne843TrsTable.setStatus("current")
_Ne843TrsEntry_Object = MibTableRow
ne843TrsEntry = _Ne843TrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4, 1)
)
ne843TrsEntry.setIndexNames(
    (0, "NE843-MIB", "ne843TrsEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843TrsEntry.setStatus("current")


class _Ne843TrsEntryIndex_Type(Integer32):
    """Custom type ne843TrsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843TrsEntryIndex_Type.__name__ = "Integer32"
_Ne843TrsEntryIndex_Object = MibTableColumn
ne843TrsEntryIndex = _Ne843TrsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4, 1, 1),
    _Ne843TrsEntryIndex_Type()
)
ne843TrsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843TrsEntryIndex.setStatus("current")
_Ne843TrsEntryIde_Type = DisplayString
_Ne843TrsEntryIde_Object = MibTableColumn
ne843TrsEntryIde = _Ne843TrsEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4, 1, 2),
    _Ne843TrsEntryIde_Type()
)
ne843TrsEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843TrsEntryIde.setStatus("current")
_Ne843TrsEntryDes_Type = DisplayString
_Ne843TrsEntryDes_Object = MibTableColumn
ne843TrsEntryDes = _Ne843TrsEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4, 1, 3),
    _Ne843TrsEntryDes_Type()
)
ne843TrsEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843TrsEntryDes.setStatus("current")
_Ne843TrsEntrySrc_Type = DisplayString
_Ne843TrsEntrySrc_Object = MibTableColumn
ne843TrsEntrySrc = _Ne843TrsEntrySrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 4, 1, 4),
    _Ne843TrsEntrySrc_Type()
)
ne843TrsEntrySrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843TrsEntrySrc.setStatus("current")
_Ne843Aco1_ObjectIdentity = ObjectIdentity
ne843Aco1 = _Ne843Aco1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5)
)
_Ne843Aco1Ide_Type = DisplayString
_Ne843Aco1Ide_Object = MibScalar
ne843Aco1Ide = _Ne843Aco1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 1),
    _Ne843Aco1Ide_Type()
)
ne843Aco1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Aco1Ide.setStatus("current")
_Ne843Aco1Des_Type = DisplayString
_Ne843Aco1Des_Object = MibScalar
ne843Aco1Des = _Ne843Aco1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 2),
    _Ne843Aco1Des_Type()
)
ne843Aco1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Des.setStatus("current")


class _Ne843Aco1Stt_Type(Integer32):
    """Custom type ne843Aco1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Aco1Stt_Type.__name__ = "Integer32"
_Ne843Aco1Stt_Object = MibScalar
ne843Aco1Stt = _Ne843Aco1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 3),
    _Ne843Aco1Stt_Type()
)
ne843Aco1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Stt.setStatus("current")


class _Ne843Aco1Cst_Type(Integer32):
    """Custom type ne843Aco1Cst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Aco1Cst_Type.__name__ = "Integer32"
_Ne843Aco1Cst_Object = MibScalar
ne843Aco1Cst = _Ne843Aco1Cst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 4),
    _Ne843Aco1Cst_Type()
)
ne843Aco1Cst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Aco1Cst.setStatus("current")


class _Ne843Aco1Cae_Type(Integer32):
    """Custom type ne843Aco1Cae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Aco1Cae_Type.__name__ = "Integer32"
_Ne843Aco1Cae_Object = MibScalar
ne843Aco1Cae = _Ne843Aco1Cae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 5),
    _Ne843Aco1Cae_Type()
)
ne843Aco1Cae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Cae.setStatus("current")


class _Ne843Aco1Cto_Type(Integer32):
    """Custom type ne843Aco1Cto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ne843Aco1Cto_Type.__name__ = "Integer32"
_Ne843Aco1Cto_Object = MibScalar
ne843Aco1Cto = _Ne843Aco1Cto_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 6),
    _Ne843Aco1Cto_Type()
)
ne843Aco1Cto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Cto.setStatus("current")
if mibBuilder.loadTexts:
    ne843Aco1Cto.setUnits("Hours")


class _Ne843Aco1Jst_Type(Integer32):
    """Custom type ne843Aco1Jst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Aco1Jst_Type.__name__ = "Integer32"
_Ne843Aco1Jst_Object = MibScalar
ne843Aco1Jst = _Ne843Aco1Jst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 7),
    _Ne843Aco1Jst_Type()
)
ne843Aco1Jst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Aco1Jst.setStatus("current")


class _Ne843Aco1Jae_Type(Integer32):
    """Custom type ne843Aco1Jae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Aco1Jae_Type.__name__ = "Integer32"
_Ne843Aco1Jae_Object = MibScalar
ne843Aco1Jae = _Ne843Aco1Jae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 8),
    _Ne843Aco1Jae_Type()
)
ne843Aco1Jae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Jae.setStatus("current")


class _Ne843Aco1Jto_Type(Integer32):
    """Custom type ne843Aco1Jto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ne843Aco1Jto_Type.__name__ = "Integer32"
_Ne843Aco1Jto_Object = MibScalar
ne843Aco1Jto = _Ne843Aco1Jto_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 9),
    _Ne843Aco1Jto_Type()
)
ne843Aco1Jto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Jto.setStatus("current")
if mibBuilder.loadTexts:
    ne843Aco1Jto.setUnits("Hours")


class _Ne843Aco1Nst_Type(Integer32):
    """Custom type ne843Aco1Nst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Aco1Nst_Type.__name__ = "Integer32"
_Ne843Aco1Nst_Object = MibScalar
ne843Aco1Nst = _Ne843Aco1Nst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 10),
    _Ne843Aco1Nst_Type()
)
ne843Aco1Nst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Aco1Nst.setStatus("current")


class _Ne843Aco1Nae_Type(Integer32):
    """Custom type ne843Aco1Nae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Aco1Nae_Type.__name__ = "Integer32"
_Ne843Aco1Nae_Object = MibScalar
ne843Aco1Nae = _Ne843Aco1Nae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 11),
    _Ne843Aco1Nae_Type()
)
ne843Aco1Nae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Nae.setStatus("current")


class _Ne843Aco1Nto_Type(Integer32):
    """Custom type ne843Aco1Nto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_Ne843Aco1Nto_Type.__name__ = "Integer32"
_Ne843Aco1Nto_Object = MibScalar
ne843Aco1Nto = _Ne843Aco1Nto_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 12),
    _Ne843Aco1Nto_Type()
)
ne843Aco1Nto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Nto.setStatus("current")
if mibBuilder.loadTexts:
    ne843Aco1Nto.setUnits("Hours")


class _Ne843Aco1Lbe_Type(Integer32):
    """Custom type ne843Aco1Lbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Aco1Lbe_Type.__name__ = "Integer32"
_Ne843Aco1Lbe_Object = MibScalar
ne843Aco1Lbe = _Ne843Aco1Lbe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 13),
    _Ne843Aco1Lbe_Type()
)
ne843Aco1Lbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Aco1Lbe.setStatus("current")
_Ne843Aco1Aac_Type = DisplayString
_Ne843Aco1Aac_Object = MibScalar
ne843Aco1Aac = _Ne843Aco1Aac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 5, 14),
    _Ne843Aco1Aac_Type()
)
ne843Aco1Aac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Aco1Aac.setStatus("current")
_Ne843Gm1_ObjectIdentity = ObjectIdentity
ne843Gm1 = _Ne843Gm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6)
)
_Ne843Gm1Ide_Type = DisplayString
_Ne843Gm1Ide_Object = MibScalar
ne843Gm1Ide = _Ne843Gm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 1),
    _Ne843Gm1Ide_Type()
)
ne843Gm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gm1Ide.setStatus("current")
_Ne843Gm1Des_Type = DisplayString
_Ne843Gm1Des_Object = MibScalar
ne843Gm1Des = _Ne843Gm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 2),
    _Ne843Gm1Des_Type()
)
ne843Gm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Des.setStatus("current")


class _Ne843Gm1Lse_Type(Integer32):
    """Custom type ne843Gm1Lse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gm1Lse_Type.__name__ = "Integer32"
_Ne843Gm1Lse_Object = MibScalar
ne843Gm1Lse = _Ne843Gm1Lse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 3),
    _Ne843Gm1Lse_Type()
)
ne843Gm1Lse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Lse.setStatus("current")


class _Ne843Gm1Rme_Type(Integer32):
    """Custom type ne843Gm1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gm1Rme_Type.__name__ = "Integer32"
_Ne843Gm1Rme_Object = MibScalar
ne843Gm1Rme = _Ne843Gm1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 4),
    _Ne843Gm1Rme_Type()
)
ne843Gm1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Rme.setStatus("current")


class _Ne843Gm1Fsd_Type(Integer32):
    """Custom type ne843Gm1Fsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25000, 30000),
        ValueRangeConstraint(50000, 60000),
    )


_Ne843Gm1Fsd_Type.__name__ = "Integer32"
_Ne843Gm1Fsd_Object = MibScalar
ne843Gm1Fsd = _Ne843Gm1Fsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 5),
    _Ne843Gm1Fsd_Type()
)
ne843Gm1Fsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Fsd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Fsd.setUnits("mV")


class _Ne843Gm1Bsd_Type(Integer32):
    """Custom type ne843Gm1Bsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(26000, 30000),
        ValueRangeConstraint(52000, 60000),
    )


_Ne843Gm1Bsd_Type.__name__ = "Integer32"
_Ne843Gm1Bsd_Object = MibScalar
ne843Gm1Bsd = _Ne843Gm1Bsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 6),
    _Ne843Gm1Bsd_Type()
)
ne843Gm1Bsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Bsd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Bsd.setUnits("mV")


class _Ne843Gm1Fsp_Type(Integer32):
    """Custom type ne843Gm1Fsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 28000),
        ValueRangeConstraint(44000, 56500),
    )


_Ne843Gm1Fsp_Type.__name__ = "Integer32"
_Ne843Gm1Fsp_Object = MibScalar
ne843Gm1Fsp = _Ne843Gm1Fsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 7),
    _Ne843Gm1Fsp_Type()
)
ne843Gm1Fsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Fsp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Fsp.setUnits("mV")


class _Ne843Gm1Bsp_Type(Integer32):
    """Custom type ne843Gm1Bsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 30000),
        ValueRangeConstraint(48000, 60000),
    )


_Ne843Gm1Bsp_Type.__name__ = "Integer32"
_Ne843Gm1Bsp_Object = MibScalar
ne843Gm1Bsp = _Ne843Gm1Bsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 8),
    _Ne843Gm1Bsp_Type()
)
ne843Gm1Bsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Bsp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Bsp.setUnits("mV")


class _Ne843Gm1Fcl_Type(Integer32):
    """Custom type ne843Gm1Fcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 110),
    )


_Ne843Gm1Fcl_Type.__name__ = "Integer32"
_Ne843Gm1Fcl_Object = MibScalar
ne843Gm1Fcl = _Ne843Gm1Fcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 9),
    _Ne843Gm1Fcl_Type()
)
ne843Gm1Fcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Fcl.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Fcl.setUnits("%")


class _Ne843Gm1Bcl_Type(Integer32):
    """Custom type ne843Gm1Bcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 110),
    )


_Ne843Gm1Bcl_Type.__name__ = "Integer32"
_Ne843Gm1Bcl_Object = MibScalar
ne843Gm1Bcl = _Ne843Gm1Bcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 10),
    _Ne843Gm1Bcl_Type()
)
ne843Gm1Bcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Bcl.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gm1Bcl.setUnits("%")


class _Ne843Gm1Oft_Type(Integer32):
    """Custom type ne843Gm1Oft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_Ne843Gm1Oft_Type.__name__ = "Integer32"
_Ne843Gm1Oft_Object = MibScalar
ne843Gm1Oft = _Ne843Gm1Oft_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 11),
    _Ne843Gm1Oft_Type()
)
ne843Gm1Oft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Oft.setStatus("current")


class _Ne843Gm1Wie_Type(Integer32):
    """Custom type ne843Gm1Wie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gm1Wie_Type.__name__ = "Integer32"
_Ne843Gm1Wie_Object = MibScalar
ne843Gm1Wie = _Ne843Gm1Wie_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 12),
    _Ne843Gm1Wie_Type()
)
ne843Gm1Wie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Wie.setStatus("current")


class _Ne843Gm1Sof_Type(Integer32):
    """Custom type ne843Gm1Sof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gm1Sof_Type.__name__ = "Integer32"
_Ne843Gm1Sof_Object = MibScalar
ne843Gm1Sof = _Ne843Gm1Sof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 13),
    _Ne843Gm1Sof_Type()
)
ne843Gm1Sof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Sof.setStatus("current")


class _Ne843Gm1Lsfe_Type(Integer32):
    """Custom type ne843Gm1Lsfe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gm1Lsfe_Type.__name__ = "Integer32"
_Ne843Gm1Lsfe_Object = MibScalar
ne843Gm1Lsfe = _Ne843Gm1Lsfe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 14),
    _Ne843Gm1Lsfe_Type()
)
ne843Gm1Lsfe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gm1Lsfe.setStatus("current")
_Ne843Gm1Nro_Type = DisplayString
_Ne843Gm1Nro_Object = MibScalar
ne843Gm1Nro = _Ne843Gm1Nro_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 15),
    _Ne843Gm1Nro_Type()
)
ne843Gm1Nro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gm1Nro.setStatus("current")
_Ne843Gm1Lst_Type = Integer32
_Ne843Gm1Lst_Object = MibScalar
ne843Gm1Lst = _Ne843Gm1Lst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 16),
    _Ne843Gm1Lst_Type()
)
ne843Gm1Lst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gm1Lst.setStatus("current")
_Ne843Gm1Nro1_Type = Integer32
_Ne843Gm1Nro1_Object = MibScalar
ne843Gm1Nro1 = _Ne843Gm1Nro1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 6, 17),
    _Ne843Gm1Nro1_Type()
)
ne843Gm1Nro1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gm1Nro1.setStatus("current")
_Ne843RecTable_Object = MibTable
ne843RecTable = _Ne843RecTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ne843RecTable.setStatus("current")
_Ne843RecEntry_Object = MibTableRow
ne843RecEntry = _Ne843RecEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1)
)
ne843RecEntry.setIndexNames(
    (0, "NE843-MIB", "ne843RecEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843RecEntry.setStatus("current")


class _Ne843RecEntryIndex_Type(Integer32):
    """Custom type ne843RecEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843RecEntryIndex_Type.__name__ = "Integer32"
_Ne843RecEntryIndex_Object = MibTableColumn
ne843RecEntryIndex = _Ne843RecEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 1),
    _Ne843RecEntryIndex_Type()
)
ne843RecEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryIndex.setStatus("current")
_Ne843RecEntryIde_Type = DisplayString
_Ne843RecEntryIde_Object = MibTableColumn
ne843RecEntryIde = _Ne843RecEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 2),
    _Ne843RecEntryIde_Type()
)
ne843RecEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryIde.setStatus("current")
_Ne843RecEntryDes_Type = DisplayString
_Ne843RecEntryDes_Object = MibTableColumn
ne843RecEntryDes = _Ne843RecEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 3),
    _Ne843RecEntryDes_Type()
)
ne843RecEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RecEntryDes.setStatus("current")
_Ne843RecEntryTyp_Type = DisplayString
_Ne843RecEntryTyp_Object = MibTableColumn
ne843RecEntryTyp = _Ne843RecEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 4),
    _Ne843RecEntryTyp_Type()
)
ne843RecEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RecEntryTyp.setStatus("current")
_Ne843RecEntrySn_Type = DisplayString
_Ne843RecEntrySn_Object = MibTableColumn
ne843RecEntrySn = _Ne843RecEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 5),
    _Ne843RecEntrySn_Type()
)
ne843RecEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntrySn.setStatus("current")
_Ne843RecEntryAdc_Type = Integer32
_Ne843RecEntryAdc_Object = MibTableColumn
ne843RecEntryAdc = _Ne843RecEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 6),
    _Ne843RecEntryAdc_Type()
)
ne843RecEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryAdc.setUnits("Amps")
_Ne843RecEntryVdc_Type = Integer32
_Ne843RecEntryVdc_Object = MibTableColumn
ne843RecEntryVdc = _Ne843RecEntryVdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 7),
    _Ne843RecEntryVdc_Type()
)
ne843RecEntryVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryVdc.setUnits("mV")
_Ne843RecEntryStt_Type = DisplayString
_Ne843RecEntryStt_Object = MibTableColumn
ne843RecEntryStt = _Ne843RecEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 8),
    _Ne843RecEntryStt_Type()
)
ne843RecEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RecEntryStt.setStatus("current")
_Ne843RecEntryCap_Type = Integer32
_Ne843RecEntryCap_Object = MibTableColumn
ne843RecEntryCap = _Ne843RecEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 9),
    _Ne843RecEntryCap_Type()
)
ne843RecEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryCap.setUnits("Amps")
_Ne843RecEntryVac_Type = Integer32
_Ne843RecEntryVac_Object = MibTableColumn
ne843RecEntryVac = _Ne843RecEntryVac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 10),
    _Ne843RecEntryVac_Type()
)
ne843RecEntryVac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVac.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryVac.setUnits("Volts")
_Ne843RecEntryAac_Type = Integer32
_Ne843RecEntryAac_Object = MibTableColumn
ne843RecEntryAac = _Ne843RecEntryAac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 11),
    _Ne843RecEntryAac_Type()
)
ne843RecEntryAac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAac.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryAac.setUnits("mA")
_Ne843RecEntryTmp_Type = Integer32
_Ne843RecEntryTmp_Object = MibTableColumn
ne843RecEntryTmp = _Ne843RecEntryTmp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 12),
    _Ne843RecEntryTmp_Type()
)
ne843RecEntryTmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryTmp.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryTmp.setUnits("C")


class _Ne843RecEntrySeq_Type(Integer32):
    """Custom type ne843RecEntrySeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843RecEntrySeq_Type.__name__ = "Integer32"
_Ne843RecEntrySeq_Object = MibTableColumn
ne843RecEntrySeq = _Ne843RecEntrySeq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 13),
    _Ne843RecEntrySeq_Type()
)
ne843RecEntrySeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RecEntrySeq.setStatus("current")
_Ne843RecEntryRfa_Type = DisplayString
_Ne843RecEntryRfa_Object = MibTableColumn
ne843RecEntryRfa = _Ne843RecEntryRfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 14),
    _Ne843RecEntryRfa_Type()
)
ne843RecEntryRfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRfa.setStatus("current")
_Ne843RecEntryAcf_Type = DisplayString
_Ne843RecEntryAcf_Object = MibTableColumn
ne843RecEntryAcf = _Ne843RecEntryAcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 15),
    _Ne843RecEntryAcf_Type()
)
ne843RecEntryAcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAcf.setStatus("current")
_Ne843RecEntryMan_Type = DisplayString
_Ne843RecEntryMan_Object = MibTableColumn
ne843RecEntryMan = _Ne843RecEntryMan_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 16),
    _Ne843RecEntryMan_Type()
)
ne843RecEntryMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryMan.setStatus("current")
_Ne843RecEntryDid_Type = DisplayString
_Ne843RecEntryDid_Object = MibTableColumn
ne843RecEntryDid = _Ne843RecEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 17),
    _Ne843RecEntryDid_Type()
)
ne843RecEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryDid.setStatus("current")
_Ne843RecEntryClm_Type = DisplayString
_Ne843RecEntryClm_Object = MibTableColumn
ne843RecEntryClm = _Ne843RecEntryClm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 18),
    _Ne843RecEntryClm_Type()
)
ne843RecEntryClm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryClm.setStatus("current")
_Ne843RecEntryRcf_Type = DisplayString
_Ne843RecEntryRcf_Object = MibTableColumn
ne843RecEntryRcf = _Ne843RecEntryRcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 19),
    _Ne843RecEntryRcf_Type()
)
ne843RecEntryRcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRcf.setStatus("current")
_Ne843RecEntryRfn_Type = DisplayString
_Ne843RecEntryRfn_Object = MibTableColumn
ne843RecEntryRfn = _Ne843RecEntryRfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 20),
    _Ne843RecEntryRfn_Type()
)
ne843RecEntryRfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRfn.setStatus("current")
_Ne843RecEntryRif_Type = DisplayString
_Ne843RecEntryRif_Object = MibTableColumn
ne843RecEntryRif = _Ne843RecEntryRif_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 21),
    _Ne843RecEntryRif_Type()
)
ne843RecEntryRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRif.setStatus("current")
_Ne843RecEntryLsf_Type = DisplayString
_Ne843RecEntryLsf_Object = MibTableColumn
ne843RecEntryLsf = _Ne843RecEntryLsf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 22),
    _Ne843RecEntryLsf_Type()
)
ne843RecEntryLsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryLsf.setStatus("current")
_Ne843RecEntryCc_Type = DisplayString
_Ne843RecEntryCc_Object = MibTableColumn
ne843RecEntryCc = _Ne843RecEntryCc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 23),
    _Ne843RecEntryCc_Type()
)
ne843RecEntryCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryCc.setStatus("current")
_Ne843RecEntryClei_Type = DisplayString
_Ne843RecEntryClei_Object = MibTableColumn
ne843RecEntryClei = _Ne843RecEntryClei_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 24),
    _Ne843RecEntryClei_Type()
)
ne843RecEntryClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryClei.setStatus("current")
_Ne843RecEntrySer_Type = DisplayString
_Ne843RecEntrySer_Object = MibTableColumn
ne843RecEntrySer = _Ne843RecEntrySer_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 25),
    _Ne843RecEntrySer_Type()
)
ne843RecEntrySer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntrySer.setStatus("current")
_Ne843RecEntryVerp_Type = DisplayString
_Ne843RecEntryVerp_Object = MibTableColumn
ne843RecEntryVerp = _Ne843RecEntryVerp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 26),
    _Ne843RecEntryVerp_Type()
)
ne843RecEntryVerp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVerp.setStatus("current")
_Ne843RecEntryVers_Type = DisplayString
_Ne843RecEntryVers_Object = MibTableColumn
ne843RecEntryVers = _Ne843RecEntryVers_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 27),
    _Ne843RecEntryVers_Type()
)
ne843RecEntryVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVers.setStatus("current")
_Ne843RecEntryLin_Type = DisplayString
_Ne843RecEntryLin_Object = MibTableColumn
ne843RecEntryLin = _Ne843RecEntryLin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 28),
    _Ne843RecEntryLin_Type()
)
ne843RecEntryLin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryLin.setStatus("current")
_Ne843RecEntryHin_Type = DisplayString
_Ne843RecEntryHin_Object = MibTableColumn
ne843RecEntryHin = _Ne843RecEntryHin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 29),
    _Ne843RecEntryHin_Type()
)
ne843RecEntryHin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryHin.setStatus("current")
_Ne843RecEntryBof_Type = DisplayString
_Ne843RecEntryBof_Object = MibTableColumn
ne843RecEntryBof = _Ne843RecEntryBof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 30),
    _Ne843RecEntryBof_Type()
)
ne843RecEntryBof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryBof.setStatus("current")
_Ne843RecEntrySof_Type = DisplayString
_Ne843RecEntrySof_Object = MibTableColumn
ne843RecEntrySof = _Ne843RecEntrySof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 31),
    _Ne843RecEntrySof_Type()
)
ne843RecEntrySof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntrySof.setStatus("current")
_Ne843RecEntryDer_Type = DisplayString
_Ne843RecEntryDer_Object = MibTableColumn
ne843RecEntryDer = _Ne843RecEntryDer_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 32),
    _Ne843RecEntryDer_Type()
)
ne843RecEntryDer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryDer.setStatus("current")
_Ne843RecEntryEcap_Type = Integer32
_Ne843RecEntryEcap_Object = MibTableColumn
ne843RecEntryEcap = _Ne843RecEntryEcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 33),
    _Ne843RecEntryEcap_Type()
)
ne843RecEntryEcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryEcap.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryEcap.setUnits("Amps")
_Ne843RecEntryEmod_Type = Integer32
_Ne843RecEntryEmod_Object = MibTableColumn
ne843RecEntryEmod = _Ne843RecEntryEmod_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 34),
    _Ne843RecEntryEmod_Type()
)
ne843RecEntryEmod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryEmod.setStatus("current")
_Ne843RecEntryMppt_Type = Integer32
_Ne843RecEntryMppt_Object = MibTableColumn
ne843RecEntryMppt = _Ne843RecEntryMppt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 35),
    _Ne843RecEntryMppt_Type()
)
ne843RecEntryMppt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryMppt.setStatus("current")
_Ne843RecEntryRtm_Type = Integer32
_Ne843RecEntryRtm_Object = MibTableColumn
ne843RecEntryRtm = _Ne843RecEntryRtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 36),
    _Ne843RecEntryRtm_Type()
)
ne843RecEntryRtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRtm.setStatus("current")
_Ne843RecEntryVan_Type = Integer32
_Ne843RecEntryVan_Object = MibTableColumn
ne843RecEntryVan = _Ne843RecEntryVan_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 37),
    _Ne843RecEntryVan_Type()
)
ne843RecEntryVan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVan.setStatus("current")
_Ne843RecEntryVac1_Type = Integer32
_Ne843RecEntryVac1_Object = MibTableColumn
ne843RecEntryVac1 = _Ne843RecEntryVac1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 38),
    _Ne843RecEntryVac1_Type()
)
ne843RecEntryVac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVac1.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryVac1.setUnits("Volts")
_Ne843RecEntryAac1_Type = Integer32
_Ne843RecEntryAac1_Object = MibTableColumn
ne843RecEntryAac1 = _Ne843RecEntryAac1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 39),
    _Ne843RecEntryAac1_Type()
)
ne843RecEntryAac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAac1.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryAac1.setUnits("mA")
_Ne843RecEntryVac2_Type = Integer32
_Ne843RecEntryVac2_Object = MibTableColumn
ne843RecEntryVac2 = _Ne843RecEntryVac2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 40),
    _Ne843RecEntryVac2_Type()
)
ne843RecEntryVac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVac2.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryVac2.setUnits("Volts")
_Ne843RecEntryAac2_Type = Integer32
_Ne843RecEntryAac2_Object = MibTableColumn
ne843RecEntryAac2 = _Ne843RecEntryAac2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 41),
    _Ne843RecEntryAac2_Type()
)
ne843RecEntryAac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAac2.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryAac2.setUnits("mA")
_Ne843RecEntryVac3_Type = Integer32
_Ne843RecEntryVac3_Object = MibTableColumn
ne843RecEntryVac3 = _Ne843RecEntryVac3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 42),
    _Ne843RecEntryVac3_Type()
)
ne843RecEntryVac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryVac3.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryVac3.setUnits("Volts")
_Ne843RecEntryAac3_Type = Integer32
_Ne843RecEntryAac3_Object = MibTableColumn
ne843RecEntryAac3 = _Ne843RecEntryAac3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 43),
    _Ne843RecEntryAac3_Type()
)
ne843RecEntryAac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAac3.setStatus("current")
if mibBuilder.loadTexts:
    ne843RecEntryAac3.setUnits("mA")


class _Ne843RecEntryRfa1_Type(Integer32):
    """Custom type ne843RecEntryRfa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryRfa1_Type.__name__ = "Integer32"
_Ne843RecEntryRfa1_Object = MibTableColumn
ne843RecEntryRfa1 = _Ne843RecEntryRfa1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 44),
    _Ne843RecEntryRfa1_Type()
)
ne843RecEntryRfa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRfa1.setStatus("current")


class _Ne843RecEntryAcf1_Type(Integer32):
    """Custom type ne843RecEntryAcf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryAcf1_Type.__name__ = "Integer32"
_Ne843RecEntryAcf1_Object = MibTableColumn
ne843RecEntryAcf1 = _Ne843RecEntryAcf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 45),
    _Ne843RecEntryAcf1_Type()
)
ne843RecEntryAcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryAcf1.setStatus("current")


class _Ne843RecEntryMan1_Type(Integer32):
    """Custom type ne843RecEntryMan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryMan1_Type.__name__ = "Integer32"
_Ne843RecEntryMan1_Object = MibTableColumn
ne843RecEntryMan1 = _Ne843RecEntryMan1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 46),
    _Ne843RecEntryMan1_Type()
)
ne843RecEntryMan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryMan1.setStatus("current")


class _Ne843RecEntryDid1_Type(Integer32):
    """Custom type ne843RecEntryDid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryDid1_Type.__name__ = "Integer32"
_Ne843RecEntryDid1_Object = MibTableColumn
ne843RecEntryDid1 = _Ne843RecEntryDid1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 47),
    _Ne843RecEntryDid1_Type()
)
ne843RecEntryDid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryDid1.setStatus("current")


class _Ne843RecEntryClm1_Type(Integer32):
    """Custom type ne843RecEntryClm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryClm1_Type.__name__ = "Integer32"
_Ne843RecEntryClm1_Object = MibTableColumn
ne843RecEntryClm1 = _Ne843RecEntryClm1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 48),
    _Ne843RecEntryClm1_Type()
)
ne843RecEntryClm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryClm1.setStatus("current")


class _Ne843RecEntryRcf1_Type(Integer32):
    """Custom type ne843RecEntryRcf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryRcf1_Type.__name__ = "Integer32"
_Ne843RecEntryRcf1_Object = MibTableColumn
ne843RecEntryRcf1 = _Ne843RecEntryRcf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 49),
    _Ne843RecEntryRcf1_Type()
)
ne843RecEntryRcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRcf1.setStatus("current")


class _Ne843RecEntryRfn1_Type(Integer32):
    """Custom type ne843RecEntryRfn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryRfn1_Type.__name__ = "Integer32"
_Ne843RecEntryRfn1_Object = MibTableColumn
ne843RecEntryRfn1 = _Ne843RecEntryRfn1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 50),
    _Ne843RecEntryRfn1_Type()
)
ne843RecEntryRfn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRfn1.setStatus("current")


class _Ne843RecEntryRif1_Type(Integer32):
    """Custom type ne843RecEntryRif1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryRif1_Type.__name__ = "Integer32"
_Ne843RecEntryRif1_Object = MibTableColumn
ne843RecEntryRif1 = _Ne843RecEntryRif1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 51),
    _Ne843RecEntryRif1_Type()
)
ne843RecEntryRif1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryRif1.setStatus("current")


class _Ne843RecEntryLsf1_Type(Integer32):
    """Custom type ne843RecEntryLsf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryLsf1_Type.__name__ = "Integer32"
_Ne843RecEntryLsf1_Object = MibTableColumn
ne843RecEntryLsf1 = _Ne843RecEntryLsf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 52),
    _Ne843RecEntryLsf1_Type()
)
ne843RecEntryLsf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryLsf1.setStatus("current")


class _Ne843RecEntryLin1_Type(Integer32):
    """Custom type ne843RecEntryLin1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryLin1_Type.__name__ = "Integer32"
_Ne843RecEntryLin1_Object = MibTableColumn
ne843RecEntryLin1 = _Ne843RecEntryLin1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 53),
    _Ne843RecEntryLin1_Type()
)
ne843RecEntryLin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryLin1.setStatus("current")


class _Ne843RecEntryHin1_Type(Integer32):
    """Custom type ne843RecEntryHin1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryHin1_Type.__name__ = "Integer32"
_Ne843RecEntryHin1_Object = MibTableColumn
ne843RecEntryHin1 = _Ne843RecEntryHin1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 54),
    _Ne843RecEntryHin1_Type()
)
ne843RecEntryHin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryHin1.setStatus("current")


class _Ne843RecEntryBof1_Type(Integer32):
    """Custom type ne843RecEntryBof1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryBof1_Type.__name__ = "Integer32"
_Ne843RecEntryBof1_Object = MibTableColumn
ne843RecEntryBof1 = _Ne843RecEntryBof1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 55),
    _Ne843RecEntryBof1_Type()
)
ne843RecEntryBof1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryBof1.setStatus("current")


class _Ne843RecEntrySof1_Type(Integer32):
    """Custom type ne843RecEntrySof1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntrySof1_Type.__name__ = "Integer32"
_Ne843RecEntrySof1_Object = MibTableColumn
ne843RecEntrySof1 = _Ne843RecEntrySof1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 56),
    _Ne843RecEntrySof1_Type()
)
ne843RecEntrySof1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntrySof1.setStatus("current")


class _Ne843RecEntryDer1_Type(Integer32):
    """Custom type ne843RecEntryDer1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RecEntryDer1_Type.__name__ = "Integer32"
_Ne843RecEntryDer1_Object = MibTableColumn
ne843RecEntryDer1 = _Ne843RecEntryDer1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 7, 1, 57),
    _Ne843RecEntryDer1_Type()
)
ne843RecEntryDer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RecEntryDer1.setStatus("current")
_Ne843Cp1_ObjectIdentity = ObjectIdentity
ne843Cp1 = _Ne843Cp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8)
)
_Ne843Cp1Ide_Type = DisplayString
_Ne843Cp1Ide_Object = MibScalar
ne843Cp1Ide = _Ne843Cp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 1),
    _Ne843Cp1Ide_Type()
)
ne843Cp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Ide.setStatus("current")
_Ne843Cp1Des_Type = DisplayString
_Ne843Cp1Des_Object = MibScalar
ne843Cp1Des = _Ne843Cp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 2),
    _Ne843Cp1Des_Type()
)
ne843Cp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Des.setStatus("current")
_Ne843Cp1Typ_Type = DisplayString
_Ne843Cp1Typ_Object = MibScalar
ne843Cp1Typ = _Ne843Cp1Typ_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 3),
    _Ne843Cp1Typ_Type()
)
ne843Cp1Typ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Typ.setStatus("current")
_Ne843Cp1Vdc_Type = Integer32
_Ne843Cp1Vdc_Object = MibScalar
ne843Cp1Vdc = _Ne843Cp1Vdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 4),
    _Ne843Cp1Vdc_Type()
)
ne843Cp1Vdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Vdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Vdc.setUnits("mV")
_Ne843Cp1Adc_Type = Integer32
_Ne843Cp1Adc_Object = MibScalar
ne843Cp1Adc = _Ne843Cp1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 5),
    _Ne843Cp1Adc_Type()
)
ne843Cp1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Adc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Adc.setUnits("Amps")
_Ne843Cp1Cap_Type = Integer32
_Ne843Cp1Cap_Object = MibScalar
ne843Cp1Cap = _Ne843Cp1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 6),
    _Ne843Cp1Cap_Type()
)
ne843Cp1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Cap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Cap.setUnits("Amps")
_Ne843Cp1Olcap_Type = Integer32
_Ne843Cp1Olcap_Object = MibScalar
ne843Cp1Olcap = _Ne843Cp1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 7),
    _Ne843Cp1Olcap_Type()
)
ne843Cp1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Olcap.setUnits("Amps")


class _Ne843Cp1Vsp_Type(Integer32):
    """Custom type ne843Cp1Vsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23000, 28000),
        ValueRangeConstraint(46000, 57000),
    )


_Ne843Cp1Vsp_Type.__name__ = "Integer32"
_Ne843Cp1Vsp_Object = MibScalar
ne843Cp1Vsp = _Ne843Cp1Vsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 8),
    _Ne843Cp1Vsp_Type()
)
ne843Cp1Vsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Vsp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Vsp.setUnits("mV")


class _Ne843Cp1Vsd_Type(Integer32):
    """Custom type ne843Cp1Vsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25000, 30000),
        ValueRangeConstraint(50000, 60000),
    )


_Ne843Cp1Vsd_Type.__name__ = "Integer32"
_Ne843Cp1Vsd_Object = MibScalar
ne843Cp1Vsd = _Ne843Cp1Vsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 9),
    _Ne843Cp1Vsd_Type()
)
ne843Cp1Vsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Vsd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Vsd.setUnits("mV")


class _Ne843Cp1Clm_Type(Integer32):
    """Custom type ne843Cp1Clm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_Ne843Cp1Clm_Type.__name__ = "Integer32"
_Ne843Cp1Clm_Object = MibScalar
ne843Cp1Clm = _Ne843Cp1Clm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 10),
    _Ne843Cp1Clm_Type()
)
ne843Cp1Clm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Clm.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Clm.setUnits("%")


class _Ne843Cp1Dth_Type(Integer32):
    """Custom type ne843Cp1Dth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 25000),
        ValueRangeConstraint(40000, 50000),
    )


_Ne843Cp1Dth_Type.__name__ = "Integer32"
_Ne843Cp1Dth_Object = MibScalar
ne843Cp1Dth = _Ne843Cp1Dth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 11),
    _Ne843Cp1Dth_Type()
)
ne843Cp1Dth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Dth.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Dth.setUnits("mV")


class _Ne843Cp1Rth_Type(Integer32):
    """Custom type ne843Cp1Rth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 27000),
        ValueRangeConstraint(44000, 54000),
    )


_Ne843Cp1Rth_Type.__name__ = "Integer32"
_Ne843Cp1Rth_Object = MibScalar
ne843Cp1Rth = _Ne843Cp1Rth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 12),
    _Ne843Cp1Rth_Type()
)
ne843Cp1Rth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Rth.setStatus("current")
if mibBuilder.loadTexts:
    ne843Cp1Rth.setUnits("mV")


class _Ne843Cp1Lvd_Type(Integer32):
    """Custom type ne843Cp1Lvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Cp1Lvd_Type.__name__ = "Integer32"
_Ne843Cp1Lvd_Object = MibScalar
ne843Cp1Lvd = _Ne843Cp1Lvd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 13),
    _Ne843Cp1Lvd_Type()
)
ne843Cp1Lvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Lvd.setStatus("current")


class _Ne843Cp1Rss_Type(Integer32):
    """Custom type ne843Cp1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843Cp1Rss_Type.__name__ = "Integer32"
_Ne843Cp1Rss_Object = MibScalar
ne843Cp1Rss = _Ne843Cp1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 14),
    _Ne843Cp1Rss_Type()
)
ne843Cp1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Rss.setStatus("current")


class _Ne843Cp1Rme_Type(Integer32):
    """Custom type ne843Cp1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Cp1Rme_Type.__name__ = "Integer32"
_Ne843Cp1Rme_Object = MibScalar
ne843Cp1Rme = _Ne843Cp1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 15),
    _Ne843Cp1Rme_Type()
)
ne843Cp1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Rme.setStatus("current")


class _Ne843Cp1Rof_Type(Integer32):
    """Custom type ne843Cp1Rof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Cp1Rof_Type.__name__ = "Integer32"
_Ne843Cp1Rof_Object = MibScalar
ne843Cp1Rof = _Ne843Cp1Rof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 16),
    _Ne843Cp1Rof_Type()
)
ne843Cp1Rof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cp1Rof.setStatus("current")
_Ne843Cp1Cfa_Type = DisplayString
_Ne843Cp1Cfa_Object = MibScalar
ne843Cp1Cfa = _Ne843Cp1Cfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 17),
    _Ne843Cp1Cfa_Type()
)
ne843Cp1Cfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Cfa.setStatus("current")
_Ne843Cp1Cfn_Type = DisplayString
_Ne843Cp1Cfn_Object = MibScalar
ne843Cp1Cfn = _Ne843Cp1Cfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 18),
    _Ne843Cp1Cfn_Type()
)
ne843Cp1Cfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Cfn.setStatus("current")
_Ne843Cp1Cfj_Type = DisplayString
_Ne843Cp1Cfj_Object = MibScalar
ne843Cp1Cfj = _Ne843Cp1Cfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 19),
    _Ne843Cp1Cfj_Type()
)
ne843Cp1Cfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Cfj.setStatus("current")
_Ne843Cp1Dfa_Type = DisplayString
_Ne843Cp1Dfa_Object = MibScalar
ne843Cp1Dfa = _Ne843Cp1Dfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 20),
    _Ne843Cp1Dfa_Type()
)
ne843Cp1Dfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Dfa.setStatus("current")
_Ne843Cp1Did_Type = DisplayString
_Ne843Cp1Did_Object = MibScalar
ne843Cp1Did = _Ne843Cp1Did_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 21),
    _Ne843Cp1Did_Type()
)
ne843Cp1Did.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Did.setStatus("current")
_Ne843Cp1Icc_Type = DisplayString
_Ne843Cp1Icc_Object = MibScalar
ne843Cp1Icc = _Ne843Cp1Icc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 22),
    _Ne843Cp1Icc_Type()
)
ne843Cp1Icc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Icc.setStatus("current")
_Ne843Cp1Mfa_Type = DisplayString
_Ne843Cp1Mfa_Object = MibScalar
ne843Cp1Mfa = _Ne843Cp1Mfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 23),
    _Ne843Cp1Mfa_Type()
)
ne843Cp1Mfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Mfa.setStatus("current")
_Ne843Cp1Hva_Type = DisplayString
_Ne843Cp1Hva_Object = MibScalar
ne843Cp1Hva = _Ne843Cp1Hva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 24),
    _Ne843Cp1Hva_Type()
)
ne843Cp1Hva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Hva.setStatus("current")
_Ne843Cp1Hfv_Type = DisplayString
_Ne843Cp1Hfv_Object = MibScalar
ne843Cp1Hfv = _Ne843Cp1Hfv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 25),
    _Ne843Cp1Hfv_Type()
)
ne843Cp1Hfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Hfv.setStatus("current")
_Ne843Cp1Vla_Type = DisplayString
_Ne843Cp1Vla_Object = MibScalar
ne843Cp1Vla = _Ne843Cp1Vla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 26),
    _Ne843Cp1Vla_Type()
)
ne843Cp1Vla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Vla.setStatus("current")
_Ne843Cp1Rl_Type = DisplayString
_Ne843Cp1Rl_Object = MibScalar
ne843Cp1Rl = _Ne843Cp1Rl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 27),
    _Ne843Cp1Rl_Type()
)
ne843Cp1Rl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Rl.setStatus("current")
_Ne843Cp1Cin_Type = DisplayString
_Ne843Cp1Cin_Object = MibScalar
ne843Cp1Cin = _Ne843Cp1Cin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 8, 28),
    _Ne843Cp1Cin_Type()
)
ne843Cp1Cin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cp1Cin.setStatus("current")
_Ne843DccTable_Object = MibTable
ne843DccTable = _Ne843DccTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    ne843DccTable.setStatus("current")
_Ne843DccEntry_Object = MibTableRow
ne843DccEntry = _Ne843DccEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1)
)
ne843DccEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DccEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DccEntry.setStatus("current")


class _Ne843DccEntryIndex_Type(Integer32):
    """Custom type ne843DccEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DccEntryIndex_Type.__name__ = "Integer32"
_Ne843DccEntryIndex_Object = MibTableColumn
ne843DccEntryIndex = _Ne843DccEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 1),
    _Ne843DccEntryIndex_Type()
)
ne843DccEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryIndex.setStatus("current")
_Ne843DccEntryIde_Type = DisplayString
_Ne843DccEntryIde_Object = MibTableColumn
ne843DccEntryIde = _Ne843DccEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 2),
    _Ne843DccEntryIde_Type()
)
ne843DccEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryIde.setStatus("current")
_Ne843DccEntryDes_Type = DisplayString
_Ne843DccEntryDes_Object = MibTableColumn
ne843DccEntryDes = _Ne843DccEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 3),
    _Ne843DccEntryDes_Type()
)
ne843DccEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DccEntryDes.setStatus("current")
_Ne843DccEntryTyp_Type = DisplayString
_Ne843DccEntryTyp_Object = MibTableColumn
ne843DccEntryTyp = _Ne843DccEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 4),
    _Ne843DccEntryTyp_Type()
)
ne843DccEntryTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryTyp.setStatus("current")
_Ne843DccEntrySn_Type = DisplayString
_Ne843DccEntrySn_Object = MibTableColumn
ne843DccEntrySn = _Ne843DccEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 5),
    _Ne843DccEntrySn_Type()
)
ne843DccEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntrySn.setStatus("current")
_Ne843DccEntryAdc_Type = Integer32
_Ne843DccEntryAdc_Object = MibTableColumn
ne843DccEntryAdc = _Ne843DccEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 6),
    _Ne843DccEntryAdc_Type()
)
ne843DccEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843DccEntryAdc.setUnits("Amps")
_Ne843DccEntryCap_Type = Integer32
_Ne843DccEntryCap_Object = MibTableColumn
ne843DccEntryCap = _Ne843DccEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 7),
    _Ne843DccEntryCap_Type()
)
ne843DccEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    ne843DccEntryCap.setUnits("Amps")
_Ne843DccEntryStt_Type = DisplayString
_Ne843DccEntryStt_Object = MibTableColumn
ne843DccEntryStt = _Ne843DccEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 8),
    _Ne843DccEntryStt_Type()
)
ne843DccEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DccEntryStt.setStatus("current")
_Ne843DccEntryCfa_Type = DisplayString
_Ne843DccEntryCfa_Object = MibTableColumn
ne843DccEntryCfa = _Ne843DccEntryCfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 9),
    _Ne843DccEntryCfa_Type()
)
ne843DccEntryCfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCfa.setStatus("current")
_Ne843DccEntryDfa_Type = DisplayString
_Ne843DccEntryDfa_Object = MibTableColumn
ne843DccEntryDfa = _Ne843DccEntryDfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 10),
    _Ne843DccEntryDfa_Type()
)
ne843DccEntryDfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryDfa.setStatus("current")
_Ne843DccEntryDid_Type = DisplayString
_Ne843DccEntryDid_Object = MibTableColumn
ne843DccEntryDid = _Ne843DccEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 11),
    _Ne843DccEntryDid_Type()
)
ne843DccEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryDid.setStatus("current")
_Ne843DccEntryCcf_Type = DisplayString
_Ne843DccEntryCcf_Object = MibTableColumn
ne843DccEntryCcf = _Ne843DccEntryCcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 12),
    _Ne843DccEntryCcf_Type()
)
ne843DccEntryCcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCcf.setStatus("current")
_Ne843DccEntryCfn_Type = DisplayString
_Ne843DccEntryCfn_Object = MibTableColumn
ne843DccEntryCfn = _Ne843DccEntryCfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 13),
    _Ne843DccEntryCfn_Type()
)
ne843DccEntryCfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCfn.setStatus("current")


class _Ne843DccEntryCfa1_Type(Integer32):
    """Custom type ne843DccEntryCfa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843DccEntryCfa1_Type.__name__ = "Integer32"
_Ne843DccEntryCfa1_Object = MibTableColumn
ne843DccEntryCfa1 = _Ne843DccEntryCfa1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 14),
    _Ne843DccEntryCfa1_Type()
)
ne843DccEntryCfa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCfa1.setStatus("current")


class _Ne843DccEntryDfa1_Type(Integer32):
    """Custom type ne843DccEntryDfa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843DccEntryDfa1_Type.__name__ = "Integer32"
_Ne843DccEntryDfa1_Object = MibTableColumn
ne843DccEntryDfa1 = _Ne843DccEntryDfa1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 15),
    _Ne843DccEntryDfa1_Type()
)
ne843DccEntryDfa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryDfa1.setStatus("current")


class _Ne843DccEntryDid1_Type(Integer32):
    """Custom type ne843DccEntryDid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843DccEntryDid1_Type.__name__ = "Integer32"
_Ne843DccEntryDid1_Object = MibTableColumn
ne843DccEntryDid1 = _Ne843DccEntryDid1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 16),
    _Ne843DccEntryDid1_Type()
)
ne843DccEntryDid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryDid1.setStatus("current")


class _Ne843DccEntryCcf1_Type(Integer32):
    """Custom type ne843DccEntryCcf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843DccEntryCcf1_Type.__name__ = "Integer32"
_Ne843DccEntryCcf1_Object = MibTableColumn
ne843DccEntryCcf1 = _Ne843DccEntryCcf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 17),
    _Ne843DccEntryCcf1_Type()
)
ne843DccEntryCcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCcf1.setStatus("current")


class _Ne843DccEntryCfn1_Type(Integer32):
    """Custom type ne843DccEntryCfn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843DccEntryCfn1_Type.__name__ = "Integer32"
_Ne843DccEntryCfn1_Object = MibTableColumn
ne843DccEntryCfn1 = _Ne843DccEntryCfn1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 9, 1, 18),
    _Ne843DccEntryCfn1_Type()
)
ne843DccEntryCfn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DccEntryCfn1.setStatus("current")
_Ne843Bs1_ObjectIdentity = ObjectIdentity
ne843Bs1 = _Ne843Bs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10)
)
_Ne843Bs1Ide_Type = DisplayString
_Ne843Bs1Ide_Object = MibScalar
ne843Bs1Ide = _Ne843Bs1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 1),
    _Ne843Bs1Ide_Type()
)
ne843Bs1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Bs1Ide.setStatus("current")
_Ne843Bs1Des_Type = DisplayString
_Ne843Bs1Des_Object = MibScalar
ne843Bs1Des = _Ne843Bs1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 2),
    _Ne843Bs1Des_Type()
)
ne843Bs1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Bs1Des.setStatus("current")
_Ne843Bs1Stt_Type = DisplayString
_Ne843Bs1Stt_Object = MibScalar
ne843Bs1Stt = _Ne843Bs1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 3),
    _Ne843Bs1Stt_Type()
)
ne843Bs1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Bs1Stt.setStatus("current")
_Ne843Bs1Atm_Type = DisplayString
_Ne843Bs1Atm_Object = MibScalar
ne843Bs1Atm = _Ne843Bs1Atm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 4),
    _Ne843Bs1Atm_Type()
)
ne843Bs1Atm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Bs1Atm.setStatus("current")


class _Ne843Bs1Tmd_Type(Integer32):
    """Custom type ne843Bs1Tmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_Ne843Bs1Tmd_Type.__name__ = "Integer32"
_Ne843Bs1Tmd_Object = MibScalar
ne843Bs1Tmd = _Ne843Bs1Tmd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 5),
    _Ne843Bs1Tmd_Type()
)
ne843Bs1Tmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Bs1Tmd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Bs1Tmd.setUnits("Hours")


class _Ne843Bs1Amf_Type(Integer32):
    """Custom type ne843Bs1Amf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Ne843Bs1Amf_Type.__name__ = "Integer32"
_Ne843Bs1Amf_Object = MibScalar
ne843Bs1Amf = _Ne843Bs1Amf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 6),
    _Ne843Bs1Amf_Type()
)
ne843Bs1Amf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Bs1Amf.setStatus("current")


class _Ne843Bs1Cta_Type(Integer32):
    """Custom type ne843Bs1Cta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Ne843Bs1Cta_Type.__name__ = "Integer32"
_Ne843Bs1Cta_Object = MibScalar
ne843Bs1Cta = _Ne843Bs1Cta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 10, 7),
    _Ne843Bs1Cta_Type()
)
ne843Bs1Cta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Bs1Cta.setStatus("current")
_Ne843Sc1_ObjectIdentity = ObjectIdentity
ne843Sc1 = _Ne843Sc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11)
)
_Ne843Sc1Ide_Type = DisplayString
_Ne843Sc1Ide_Object = MibScalar
ne843Sc1Ide = _Ne843Sc1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 1),
    _Ne843Sc1Ide_Type()
)
ne843Sc1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Sc1Ide.setStatus("current")
_Ne843Sc1Des_Type = DisplayString
_Ne843Sc1Des_Object = MibScalar
ne843Sc1Des = _Ne843Sc1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 2),
    _Ne843Sc1Des_Type()
)
ne843Sc1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Des.setStatus("current")


class _Ne843Sc1Stt_Type(Integer32):
    """Custom type ne843Sc1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Sc1Stt_Type.__name__ = "Integer32"
_Ne843Sc1Stt_Object = MibScalar
ne843Sc1Stt = _Ne843Sc1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 3),
    _Ne843Sc1Stt_Type()
)
ne843Sc1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Stt.setStatus("current")


class _Ne843Sc1Rve_Type(Integer32):
    """Custom type ne843Sc1Rve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Sc1Rve_Type.__name__ = "Integer32"
_Ne843Sc1Rve_Object = MibScalar
ne843Sc1Rve = _Ne843Sc1Rve_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 4),
    _Ne843Sc1Rve_Type()
)
ne843Sc1Rve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Rve.setStatus("current")
_Ne843Sc1Ltt_Type = Integer32
_Ne843Sc1Ltt_Object = MibScalar
ne843Sc1Ltt = _Ne843Sc1Ltt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 5),
    _Ne843Sc1Ltt_Type()
)
ne843Sc1Ltt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Ltt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Ltt.setUnits("C")
_Ne843Sc1Ntt_Type = Integer32
_Ne843Sc1Ntt_Object = MibScalar
ne843Sc1Ntt = _Ne843Sc1Ntt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 6),
    _Ne843Sc1Ntt_Type()
)
ne843Sc1Ntt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Ntt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Ntt.setUnits("C")
_Ne843Sc1Utt_Type = Integer32
_Ne843Sc1Utt_Object = MibScalar
ne843Sc1Utt = _Ne843Sc1Utt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 7),
    _Ne843Sc1Utt_Type()
)
ne843Sc1Utt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Utt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Utt.setUnits("C")
_Ne843Sc1Spt_Type = Integer32
_Ne843Sc1Spt_Object = MibScalar
ne843Sc1Spt = _Ne843Sc1Spt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 8),
    _Ne843Sc1Spt_Type()
)
ne843Sc1Spt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Spt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Spt.setUnits("C")


class _Ne843Sc1Lsp_Type(Integer32):
    """Custom type ne843Sc1Lsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Ne843Sc1Lsp_Type.__name__ = "Integer32"
_Ne843Sc1Lsp_Object = MibScalar
ne843Sc1Lsp = _Ne843Sc1Lsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 9),
    _Ne843Sc1Lsp_Type()
)
ne843Sc1Lsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Lsp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Lsp.setUnits("mV/C")


class _Ne843Sc1Usp_Type(Integer32):
    """Custom type ne843Sc1Usp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Ne843Sc1Usp_Type.__name__ = "Integer32"
_Ne843Sc1Usp_Object = MibScalar
ne843Sc1Usp = _Ne843Sc1Usp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 10),
    _Ne843Sc1Usp_Type()
)
ne843Sc1Usp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Usp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Sc1Usp.setUnits("mV/C")


class _Ne843Sc1Fse_Type(Integer32):
    """Custom type ne843Sc1Fse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Sc1Fse_Type.__name__ = "Integer32"
_Ne843Sc1Fse_Object = MibScalar
ne843Sc1Fse = _Ne843Sc1Fse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 11, 11),
    _Ne843Sc1Fse_Type()
)
ne843Sc1Fse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Sc1Fse.setStatus("current")
_Ne843BtdTable_Object = MibTable
ne843BtdTable = _Ne843BtdTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12)
)
if mibBuilder.loadTexts:
    ne843BtdTable.setStatus("current")
_Ne843BtdEntry_Object = MibTableRow
ne843BtdEntry = _Ne843BtdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1)
)
ne843BtdEntry.setIndexNames(
    (0, "NE843-MIB", "ne843BtdEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843BtdEntry.setStatus("current")


class _Ne843BtdEntryIndex_Type(Integer32):
    """Custom type ne843BtdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843BtdEntryIndex_Type.__name__ = "Integer32"
_Ne843BtdEntryIndex_Object = MibTableColumn
ne843BtdEntryIndex = _Ne843BtdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 1),
    _Ne843BtdEntryIndex_Type()
)
ne843BtdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BtdEntryIndex.setStatus("current")
_Ne843BtdEntryIde_Type = DisplayString
_Ne843BtdEntryIde_Object = MibTableColumn
ne843BtdEntryIde = _Ne843BtdEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 2),
    _Ne843BtdEntryIde_Type()
)
ne843BtdEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BtdEntryIde.setStatus("current")
_Ne843BtdEntryDes_Type = DisplayString
_Ne843BtdEntryDes_Object = MibTableColumn
ne843BtdEntryDes = _Ne843BtdEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 3),
    _Ne843BtdEntryDes_Type()
)
ne843BtdEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BtdEntryDes.setStatus("current")
_Ne843BtdEntryBty_Type = DisplayString
_Ne843BtdEntryBty_Object = MibTableColumn
ne843BtdEntryBty = _Ne843BtdEntryBty_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 4),
    _Ne843BtdEntryBty_Type()
)
ne843BtdEntryBty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BtdEntryBty.setStatus("current")
_Ne843BtdEntryBtc_Type = DisplayString
_Ne843BtdEntryBtc_Object = MibTableColumn
ne843BtdEntryBtc = _Ne843BtdEntryBtc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 5),
    _Ne843BtdEntryBtc_Type()
)
ne843BtdEntryBtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BtdEntryBtc.setStatus("current")
_Ne843BtdEntryCap_Type = Integer32
_Ne843BtdEntryCap_Object = MibTableColumn
ne843BtdEntryCap = _Ne843BtdEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 12, 1, 6),
    _Ne843BtdEntryCap_Type()
)
ne843BtdEntryCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BtdEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    ne843BtdEntryCap.setUnits("Amps")
_Ne843Br1_ObjectIdentity = ObjectIdentity
ne843Br1 = _Ne843Br1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13)
)
_Ne843Br1Ide_Type = DisplayString
_Ne843Br1Ide_Object = MibScalar
ne843Br1Ide = _Ne843Br1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 1),
    _Ne843Br1Ide_Type()
)
ne843Br1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Ide.setStatus("current")
_Ne843Br1Des_Type = DisplayString
_Ne843Br1Des_Object = MibScalar
ne843Br1Des = _Ne843Br1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 2),
    _Ne843Br1Des_Type()
)
ne843Br1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Des.setStatus("current")
_Ne843Br1Adc_Type = Integer32
_Ne843Br1Adc_Object = MibScalar
ne843Br1Adc = _Ne843Br1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 3),
    _Ne843Br1Adc_Type()
)
ne843Br1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Adc.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Adc.setUnits("Amps")
_Ne843Br1Hbt_Type = Integer32
_Ne843Br1Hbt_Object = MibScalar
ne843Br1Hbt = _Ne843Br1Hbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 4),
    _Ne843Br1Hbt_Type()
)
ne843Br1Hbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Hbt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Hbt.setUnits("C")
_Ne843Br1Cap_Type = Integer32
_Ne843Br1Cap_Object = MibScalar
ne843Br1Cap = _Ne843Br1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 5),
    _Ne843Br1Cap_Type()
)
ne843Br1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Cap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Cap.setUnits("Amps")
_Ne843Br1Olcap_Type = Integer32
_Ne843Br1Olcap_Object = MibScalar
ne843Br1Olcap = _Ne843Br1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 6),
    _Ne843Br1Olcap_Type()
)
ne843Br1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Olcap.setUnits("Amps")
_Ne843Br1Btr_Type = DisplayString
_Ne843Br1Btr_Object = MibScalar
ne843Br1Btr = _Ne843Br1Btr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 7),
    _Ne843Br1Btr_Type()
)
ne843Br1Btr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Btr.setStatus("current")


class _Ne843Br1Tth_Type(Integer32):
    """Custom type ne843Br1Tth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 194),
    )


_Ne843Br1Tth_Type.__name__ = "Integer32"
_Ne843Br1Tth_Object = MibScalar
ne843Br1Tth = _Ne843Br1Tth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 8),
    _Ne843Br1Tth_Type()
)
ne843Br1Tth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Tth.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Tth.setUnits("C")


class _Ne843Br1Cle_Type(Integer32):
    """Custom type ne843Br1Cle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Br1Cle_Type.__name__ = "Integer32"
_Ne843Br1Cle_Object = MibScalar
ne843Br1Cle = _Ne843Br1Cle_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 9),
    _Ne843Br1Cle_Type()
)
ne843Br1Cle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Cle.setStatus("current")


class _Ne843Br1Clt_Type(Integer32):
    """Custom type ne843Br1Clt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_Ne843Br1Clt_Type.__name__ = "Integer32"
_Ne843Br1Clt_Object = MibScalar
ne843Br1Clt = _Ne843Br1Clt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 10),
    _Ne843Br1Clt_Type()
)
ne843Br1Clt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Clt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Clt.setUnits("Amps")


class _Ne843Br1Cev_Type(Integer32):
    """Custom type ne843Br1Cev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19250, 22750),
        ValueRangeConstraint(40250, 43750),
    )


_Ne843Br1Cev_Type.__name__ = "Integer32"
_Ne843Br1Cev_Object = MibScalar
ne843Br1Cev = _Ne843Br1Cev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 11),
    _Ne843Br1Cev_Type()
)
ne843Br1Cev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Cev.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Cev.setUnits("mV")


class _Ne843Br1Bts_Type(Integer32):
    """Custom type ne843Br1Bts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843Br1Bts_Type.__name__ = "Integer32"
_Ne843Br1Bts_Object = MibScalar
ne843Br1Bts = _Ne843Br1Bts_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 12),
    _Ne843Br1Bts_Type()
)
ne843Br1Bts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Bts.setStatus("current")
_Ne843Br1Mtt_Type = DisplayString
_Ne843Br1Mtt_Object = MibScalar
ne843Br1Mtt = _Ne843Br1Mtt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 13),
    _Ne843Br1Mtt_Type()
)
ne843Br1Mtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Mtt.setStatus("current")


class _Ne843Br1Tev_Type(Integer32):
    """Custom type ne843Br1Tev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21000, 27000),
        ValueRangeConstraint(36000, 48000),
    )


_Ne843Br1Tev_Type.__name__ = "Integer32"
_Ne843Br1Tev_Object = MibScalar
ne843Br1Tev = _Ne843Br1Tev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 14),
    _Ne843Br1Tev_Type()
)
ne843Br1Tev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Tev.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Tev.setUnits("mV")


class _Ne843Br1Tmd_Type(Integer32):
    """Custom type ne843Br1Tmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 99900),
    )


_Ne843Br1Tmd_Type.__name__ = "Integer32"
_Ne843Br1Tmd_Object = MibScalar
ne843Br1Tmd = _Ne843Br1Tmd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 15),
    _Ne843Br1Tmd_Type()
)
ne843Br1Tmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Tmd.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Tmd.setUnits("Hours x 1000")
_Ne843Br1Bte_Type = DisplayString
_Ne843Br1Bte_Object = MibScalar
ne843Br1Bte = _Ne843Br1Bte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 16),
    _Ne843Br1Bte_Type()
)
ne843Br1Bte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Bte.setStatus("current")


class _Ne843Br1Btv_Type(Integer32):
    """Custom type ne843Br1Btv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21000, 26000),
        ValueRangeConstraint(42000, 52000),
    )


_Ne843Br1Btv_Type.__name__ = "Integer32"
_Ne843Br1Btv_Object = MibScalar
ne843Br1Btv = _Ne843Br1Btv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 17),
    _Ne843Br1Btv_Type()
)
ne843Br1Btv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Btv.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Btv.setUnits("mV")


class _Ne843Br1Ath_Type(Integer32):
    """Custom type ne843Br1Ath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Ne843Br1Ath_Type.__name__ = "Integer32"
_Ne843Br1Ath_Object = MibScalar
ne843Br1Ath = _Ne843Br1Ath_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 18),
    _Ne843Br1Ath_Type()
)
ne843Br1Ath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Ath.setStatus("current")


class _Ne843Br1Tin_Type(Integer32):
    """Custom type ne843Br1Tin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_Ne843Br1Tin_Type.__name__ = "Integer32"
_Ne843Br1Tin_Object = MibScalar
ne843Br1Tin = _Ne843Br1Tin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 19),
    _Ne843Br1Tin_Type()
)
ne843Br1Tin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Tin.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Tin.setUnits("Months")


class _Ne843Br1Atw_Type(Integer32):
    """Custom type ne843Br1Atw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Ne843Br1Atw_Type.__name__ = "Integer32"
_Ne843Br1Atw_Object = MibScalar
ne843Br1Atw = _Ne843Br1Atw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 20),
    _Ne843Br1Atw_Type()
)
ne843Br1Atw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Atw.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Atw.setUnits("Hours")
_Ne843Br1Atd_Type = DisplayString
_Ne843Br1Atd_Object = MibScalar
ne843Br1Atd = _Ne843Br1Atd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 21),
    _Ne843Br1Atd_Type()
)
ne843Br1Atd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Atd.setStatus("current")
_Ne843Br1Nvm_Type = Integer32
_Ne843Br1Nvm_Object = MibScalar
ne843Br1Nvm = _Ne843Br1Nvm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 22),
    _Ne843Br1Nvm_Type()
)
ne843Br1Nvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Nvm.setStatus("current")
_Ne843Br1Ntm_Type = Integer32
_Ne843Br1Ntm_Object = MibScalar
ne843Br1Ntm = _Ne843Br1Ntm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 23),
    _Ne843Br1Ntm_Type()
)
ne843Br1Ntm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Ntm.setStatus("current")


class _Ne843Br1Scd_Type(Integer32):
    """Custom type ne843Br1Scd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Br1Scd_Type.__name__ = "Integer32"
_Ne843Br1Scd_Object = MibScalar
ne843Br1Scd = _Ne843Br1Scd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 24),
    _Ne843Br1Scd_Type()
)
ne843Br1Scd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Scd.setStatus("current")


class _Ne843Br1Scv_Type(Integer32):
    """Custom type ne843Br1Scv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_Ne843Br1Scv_Type.__name__ = "Integer32"
_Ne843Br1Scv_Object = MibScalar
ne843Br1Scv = _Ne843Br1Scv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 25),
    _Ne843Br1Scv_Type()
)
ne843Br1Scv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Br1Scv.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Scv.setUnits("mV")
_Ne843Br1Bta_Type = DisplayString
_Ne843Br1Bta_Object = MibScalar
ne843Br1Bta = _Ne843Br1Bta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 26),
    _Ne843Br1Bta_Type()
)
ne843Br1Bta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Bta.setStatus("current")
_Ne843Br1Bfa_Type = DisplayString
_Ne843Br1Bfa_Object = MibScalar
ne843Br1Bfa = _Ne843Br1Bfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 27),
    _Ne843Br1Bfa_Type()
)
ne843Br1Bfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Bfa.setStatus("current")
_Ne843Br1Scda_Type = DisplayString
_Ne843Br1Scda_Object = MibScalar
ne843Br1Scda = _Ne843Br1Scda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 28),
    _Ne843Br1Scda_Type()
)
ne843Br1Scda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Scda.setStatus("current")
_Ne843Br1Isda_Type = DisplayString
_Ne843Br1Isda_Object = MibScalar
ne843Br1Isda = _Ne843Br1Isda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 29),
    _Ne843Br1Isda_Type()
)
ne843Br1Isda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Isda.setStatus("current")
_Ne843Br1Mdp_Type = DisplayString
_Ne843Br1Mdp_Object = MibScalar
ne843Br1Mdp = _Ne843Br1Mdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 30),
    _Ne843Br1Mdp_Type()
)
ne843Br1Mdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Mdp.setStatus("current")
_Ne843Br1Mzd_Type = DisplayString
_Ne843Br1Mzd_Object = MibScalar
ne843Br1Mzd = _Ne843Br1Mzd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 31),
    _Ne843Br1Mzd_Type()
)
ne843Br1Mzd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Mzd.setStatus("current")
_Ne843Br1Btha_Type = DisplayString
_Ne843Br1Btha_Object = MibScalar
ne843Br1Btha = _Ne843Br1Btha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 32),
    _Ne843Br1Btha_Type()
)
ne843Br1Btha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Btha.setStatus("current")
_Ne843Br1Lbt_Type = Integer32
_Ne843Br1Lbt_Object = MibScalar
ne843Br1Lbt = _Ne843Br1Lbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 33),
    _Ne843Br1Lbt_Type()
)
ne843Br1Lbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Lbt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Br1Lbt.setUnits("C")
_Ne843Br1Btla_Type = DisplayString
_Ne843Br1Btla_Object = MibScalar
ne843Br1Btla = _Ne843Br1Btla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 34),
    _Ne843Br1Btla_Type()
)
ne843Br1Btla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Btla.setStatus("current")
_Ne843Br1Btvh_Type = DisplayString
_Ne843Br1Btvh_Object = MibScalar
ne843Br1Btvh = _Ne843Br1Btvh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 35),
    _Ne843Br1Btvh_Type()
)
ne843Br1Btvh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Btvh.setStatus("current")
_Ne843Br1Btvl_Type = DisplayString
_Ne843Br1Btvl_Object = MibScalar
ne843Br1Btvl = _Ne843Br1Btvl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 36),
    _Ne843Br1Btvl_Type()
)
ne843Br1Btvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Btvl.setStatus("current")
_Ne843Br1Rba_Type = DisplayString
_Ne843Br1Rba_Object = MibScalar
ne843Br1Rba = _Ne843Br1Rba_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 13, 37),
    _Ne843Br1Rba_Type()
)
ne843Br1Rba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Br1Rba.setStatus("current")
_Ne843CntTable_Object = MibTable
ne843CntTable = _Ne843CntTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14)
)
if mibBuilder.loadTexts:
    ne843CntTable.setStatus("current")
_Ne843CntEntry_Object = MibTableRow
ne843CntEntry = _Ne843CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1)
)
ne843CntEntry.setIndexNames(
    (0, "NE843-MIB", "ne843CntEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843CntEntry.setStatus("current")


class _Ne843CntEntryIndex_Type(Integer32):
    """Custom type ne843CntEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843CntEntryIndex_Type.__name__ = "Integer32"
_Ne843CntEntryIndex_Object = MibTableColumn
ne843CntEntryIndex = _Ne843CntEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 1),
    _Ne843CntEntryIndex_Type()
)
ne843CntEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryIndex.setStatus("current")
_Ne843CntEntryIde_Type = DisplayString
_Ne843CntEntryIde_Object = MibTableColumn
ne843CntEntryIde = _Ne843CntEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 2),
    _Ne843CntEntryIde_Type()
)
ne843CntEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryIde.setStatus("current")
_Ne843CntEntryDes_Type = DisplayString
_Ne843CntEntryDes_Object = MibTableColumn
ne843CntEntryDes = _Ne843CntEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 3),
    _Ne843CntEntryDes_Type()
)
ne843CntEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDes.setStatus("current")
_Ne843CntEntryStt_Type = DisplayString
_Ne843CntEntryStt_Object = MibTableColumn
ne843CntEntryStt = _Ne843CntEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 4),
    _Ne843CntEntryStt_Type()
)
ne843CntEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryStt.setStatus("current")


class _Ne843CntEntryEna_Type(Integer32):
    """Custom type ne843CntEntryEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843CntEntryEna_Type.__name__ = "Integer32"
_Ne843CntEntryEna_Object = MibTableColumn
ne843CntEntryEna = _Ne843CntEntryEna_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 5),
    _Ne843CntEntryEna_Type()
)
ne843CntEntryEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryEna.setStatus("current")


class _Ne843CntEntryDth_Type(Integer32):
    """Custom type ne843CntEntryDth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19000, 25000),
        ValueRangeConstraint(39000, 50000),
    )


_Ne843CntEntryDth_Type.__name__ = "Integer32"
_Ne843CntEntryDth_Object = MibTableColumn
ne843CntEntryDth = _Ne843CntEntryDth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 6),
    _Ne843CntEntryDth_Type()
)
ne843CntEntryDth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDth.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryDth.setUnits("mV")
_Ne843CntEntryDdy_Type = DisplayString
_Ne843CntEntryDdy_Object = MibTableColumn
ne843CntEntryDdy = _Ne843CntEntryDdy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 7),
    _Ne843CntEntryDdy_Type()
)
ne843CntEntryDdy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDdy.setStatus("current")


class _Ne843CntEntryDam_Type(Integer32):
    """Custom type ne843CntEntryDam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("voltage", 1),
          ("voltageAndTime", 2),
          ("adaptive", 3),
          ("temperature", 4),
          ("voltageandtemperature", 5),
          ("voltageandtimeandtemperature", 6),
          ("adaptiveandtemperature", 7))
    )


_Ne843CntEntryDam_Type.__name__ = "Integer32"
_Ne843CntEntryDam_Object = MibTableColumn
ne843CntEntryDam = _Ne843CntEntryDam_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 8),
    _Ne843CntEntryDam_Type()
)
ne843CntEntryDam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDam.setStatus("current")
_Ne843CntEntryDtm_Type = DisplayString
_Ne843CntEntryDtm_Object = MibTableColumn
ne843CntEntryDtm = _Ne843CntEntryDtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 9),
    _Ne843CntEntryDtm_Type()
)
ne843CntEntryDtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryDtm.setStatus("current")


class _Ne843CntEntryRth_Type(Integer32):
    """Custom type ne843CntEntryRth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19500, 27000),
        ValueRangeConstraint(39000, 55000),
    )


_Ne843CntEntryRth_Type.__name__ = "Integer32"
_Ne843CntEntryRth_Object = MibTableColumn
ne843CntEntryRth = _Ne843CntEntryRth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 10),
    _Ne843CntEntryRth_Type()
)
ne843CntEntryRth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryRth.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryRth.setUnits("mV")
_Ne843CntEntryRdy_Type = DisplayString
_Ne843CntEntryRdy_Object = MibTableColumn
ne843CntEntryRdy = _Ne843CntEntryRdy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 11),
    _Ne843CntEntryRdy_Type()
)
ne843CntEntryRdy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryRdy.setStatus("current")


class _Ne843CntEntryRam_Type(Integer32):
    """Custom type ne843CntEntryRam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("voltage", 1),
          ("voltageAndTime", 2),
          ("adaptive", 3),
          ("temperature", 4),
          ("voltageandtemperature", 5),
          ("voltageandtimeandtemperature", 6),
          ("adaptiveandtemperature", 7))
    )


_Ne843CntEntryRam_Type.__name__ = "Integer32"
_Ne843CntEntryRam_Object = MibTableColumn
ne843CntEntryRam = _Ne843CntEntryRam_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 12),
    _Ne843CntEntryRam_Type()
)
ne843CntEntryRam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryRam.setStatus("current")
_Ne843CntEntryRtm_Type = DisplayString
_Ne843CntEntryRtm_Object = MibTableColumn
ne843CntEntryRtm = _Ne843CntEntryRtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 13),
    _Ne843CntEntryRtm_Type()
)
ne843CntEntryRtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryRtm.setStatus("current")
_Ne843CntEntryCno_Type = DisplayString
_Ne843CntEntryCno_Object = MibTableColumn
ne843CntEntryCno = _Ne843CntEntryCno_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 14),
    _Ne843CntEntryCno_Type()
)
ne843CntEntryCno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryCno.setStatus("current")
_Ne843CntEntryCnf_Type = DisplayString
_Ne843CntEntryCnf_Object = MibTableColumn
ne843CntEntryCnf = _Ne843CntEntryCnf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 15),
    _Ne843CntEntryCnf_Type()
)
ne843CntEntryCnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryCnf.setStatus("current")


class _Ne843CntEntryDvx_Type(Integer32):
    """Custom type ne843CntEntryDvx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(39000, 50000),
    )


_Ne843CntEntryDvx_Type.__name__ = "Integer32"
_Ne843CntEntryDvx_Object = MibTableColumn
ne843CntEntryDvx = _Ne843CntEntryDvx_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 16),
    _Ne843CntEntryDvx_Type()
)
ne843CntEntryDvx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDvx.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryDvx.setUnits("mV")


class _Ne843CntEntryDin_Type(Integer32):
    """Custom type ne843CntEntryDin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_Ne843CntEntryDin_Type.__name__ = "Integer32"
_Ne843CntEntryDin_Object = MibTableColumn
ne843CntEntryDin = _Ne843CntEntryDin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 17),
    _Ne843CntEntryDin_Type()
)
ne843CntEntryDin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDin.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryDin.setUnits("mA")


class _Ne843CntEntryDix_Type(Integer32):
    """Custom type ne843CntEntryDix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_Ne843CntEntryDix_Type.__name__ = "Integer32"
_Ne843CntEntryDix_Object = MibTableColumn
ne843CntEntryDix = _Ne843CntEntryDix_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 18),
    _Ne843CntEntryDix_Type()
)
ne843CntEntryDix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDix.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryDix.setUnits("mA")
_Ne843CntEntryDvt_Type = Integer32
_Ne843CntEntryDvt_Object = MibTableColumn
ne843CntEntryDvt = _Ne843CntEntryDvt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 19),
    _Ne843CntEntryDvt_Type()
)
ne843CntEntryDvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CntEntryDvt.setStatus("current")
if mibBuilder.loadTexts:
    ne843CntEntryDvt.setUnits("mV")
_Ne843CntEntryDtd_Type = DisplayString
_Ne843CntEntryDtd_Object = MibTableColumn
ne843CntEntryDtd = _Ne843CntEntryDtd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 20),
    _Ne843CntEntryDtd_Type()
)
ne843CntEntryDtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDtd.setStatus("current")


class _Ne843CntEntryDtp_Type(Integer32):
    """Custom type ne843CntEntryDtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1125, 5625),
    )


_Ne843CntEntryDtp_Type.__name__ = "Integer32"
_Ne843CntEntryDtp_Object = MibTableColumn
ne843CntEntryDtp = _Ne843CntEntryDtp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 21),
    _Ne843CntEntryDtp_Type()
)
ne843CntEntryDtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryDtp.setStatus("current")
_Ne843CntEntryRtd_Type = DisplayString
_Ne843CntEntryRtd_Object = MibTableColumn
ne843CntEntryRtd = _Ne843CntEntryRtd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 22),
    _Ne843CntEntryRtd_Type()
)
ne843CntEntryRtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryRtd.setStatus("current")


class _Ne843CntEntryRtp_Type(Integer32):
    """Custom type ne843CntEntryRtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1080, 5400),
    )


_Ne843CntEntryRtp_Type.__name__ = "Integer32"
_Ne843CntEntryRtp_Object = MibTableColumn
ne843CntEntryRtp = _Ne843CntEntryRtp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 14, 1, 23),
    _Ne843CntEntryRtp_Type()
)
ne843CntEntryRtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CntEntryRtp.setStatus("current")
_Ne843DcnTable_Object = MibTable
ne843DcnTable = _Ne843DcnTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15)
)
if mibBuilder.loadTexts:
    ne843DcnTable.setStatus("current")
_Ne843DcnEntry_Object = MibTableRow
ne843DcnEntry = _Ne843DcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1)
)
ne843DcnEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DcnEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DcnEntry.setStatus("current")


class _Ne843DcnEntryIndex_Type(Integer32):
    """Custom type ne843DcnEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DcnEntryIndex_Type.__name__ = "Integer32"
_Ne843DcnEntryIndex_Object = MibTableColumn
ne843DcnEntryIndex = _Ne843DcnEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 1),
    _Ne843DcnEntryIndex_Type()
)
ne843DcnEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcnEntryIndex.setStatus("current")
_Ne843DcnEntryIde_Type = DisplayString
_Ne843DcnEntryIde_Object = MibTableColumn
ne843DcnEntryIde = _Ne843DcnEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 2),
    _Ne843DcnEntryIde_Type()
)
ne843DcnEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcnEntryIde.setStatus("current")
_Ne843DcnEntryDes_Type = DisplayString
_Ne843DcnEntryDes_Object = MibTableColumn
ne843DcnEntryDes = _Ne843DcnEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 3),
    _Ne843DcnEntryDes_Type()
)
ne843DcnEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcnEntryDes.setStatus("current")
_Ne843DcnEntryStt_Type = DisplayString
_Ne843DcnEntryStt_Object = MibTableColumn
ne843DcnEntryStt = _Ne843DcnEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 4),
    _Ne843DcnEntryStt_Type()
)
ne843DcnEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcnEntryStt.setStatus("current")
_Ne843DcnEntryTyp_Type = DisplayString
_Ne843DcnEntryTyp_Object = MibTableColumn
ne843DcnEntryTyp = _Ne843DcnEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 5),
    _Ne843DcnEntryTyp_Type()
)
ne843DcnEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcnEntryTyp.setStatus("current")
_Ne843DcnEntrySn_Type = DisplayString
_Ne843DcnEntrySn_Object = MibTableColumn
ne843DcnEntrySn = _Ne843DcnEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 6),
    _Ne843DcnEntrySn_Type()
)
ne843DcnEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcnEntrySn.setStatus("current")
_Ne843DcnEntryBrc_Type = DisplayString
_Ne843DcnEntryBrc_Object = MibTableColumn
ne843DcnEntryBrc = _Ne843DcnEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 15, 1, 7),
    _Ne843DcnEntryBrc_Type()
)
ne843DcnEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcnEntryBrc.setStatus("current")
_Ne843DcmTable_Object = MibTable
ne843DcmTable = _Ne843DcmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16)
)
if mibBuilder.loadTexts:
    ne843DcmTable.setStatus("current")
_Ne843DcmEntry_Object = MibTableRow
ne843DcmEntry = _Ne843DcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1)
)
ne843DcmEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DcmEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DcmEntry.setStatus("current")


class _Ne843DcmEntryIndex_Type(Integer32):
    """Custom type ne843DcmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DcmEntryIndex_Type.__name__ = "Integer32"
_Ne843DcmEntryIndex_Object = MibTableColumn
ne843DcmEntryIndex = _Ne843DcmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 1),
    _Ne843DcmEntryIndex_Type()
)
ne843DcmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntryIndex.setStatus("current")
_Ne843DcmEntryIde_Type = DisplayString
_Ne843DcmEntryIde_Object = MibTableColumn
ne843DcmEntryIde = _Ne843DcmEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 2),
    _Ne843DcmEntryIde_Type()
)
ne843DcmEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntryIde.setStatus("current")
_Ne843DcmEntryDes_Type = DisplayString
_Ne843DcmEntryDes_Object = MibTableColumn
ne843DcmEntryDes = _Ne843DcmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 3),
    _Ne843DcmEntryDes_Type()
)
ne843DcmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcmEntryDes.setStatus("current")
_Ne843DcmEntryStt_Type = DisplayString
_Ne843DcmEntryStt_Object = MibTableColumn
ne843DcmEntryStt = _Ne843DcmEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 4),
    _Ne843DcmEntryStt_Type()
)
ne843DcmEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntryStt.setStatus("current")
_Ne843DcmEntryTyp_Type = DisplayString
_Ne843DcmEntryTyp_Object = MibTableColumn
ne843DcmEntryTyp = _Ne843DcmEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 5),
    _Ne843DcmEntryTyp_Type()
)
ne843DcmEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcmEntryTyp.setStatus("current")
_Ne843DcmEntryVal_Type = Integer32
_Ne843DcmEntryVal_Object = MibTableColumn
ne843DcmEntryVal = _Ne843DcmEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 6),
    _Ne843DcmEntryVal_Type()
)
ne843DcmEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntryVal.setStatus("current")
if mibBuilder.loadTexts:
    ne843DcmEntryVal.setUnits("mA")
_Ne843DcmEntrySha_Type = Integer32
_Ne843DcmEntrySha_Object = MibTableColumn
ne843DcmEntrySha = _Ne843DcmEntrySha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 7),
    _Ne843DcmEntrySha_Type()
)
ne843DcmEntrySha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcmEntrySha.setStatus("current")
if mibBuilder.loadTexts:
    ne843DcmEntrySha.setUnits("Amps")
_Ne843DcmEntrySn_Type = DisplayString
_Ne843DcmEntrySn_Object = MibTableColumn
ne843DcmEntrySn = _Ne843DcmEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 8),
    _Ne843DcmEntrySn_Type()
)
ne843DcmEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntrySn.setStatus("current")
_Ne843DcmEntryBrc_Type = DisplayString
_Ne843DcmEntryBrc_Object = MibTableColumn
ne843DcmEntryBrc = _Ne843DcmEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 9),
    _Ne843DcmEntryBrc_Type()
)
ne843DcmEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DcmEntryBrc.setStatus("current")
_Ne843DcmEntryKwh_Type = DisplayString
_Ne843DcmEntryKwh_Object = MibTableColumn
ne843DcmEntryKwh = _Ne843DcmEntryKwh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 16, 1, 10),
    _Ne843DcmEntryKwh_Type()
)
ne843DcmEntryKwh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DcmEntryKwh.setStatus("current")
if mibBuilder.loadTexts:
    ne843DcmEntryKwh.setUnits("kWh")
_Ne843UdeTable_Object = MibTable
ne843UdeTable = _Ne843UdeTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17)
)
if mibBuilder.loadTexts:
    ne843UdeTable.setStatus("current")
_Ne843UdeEntry_Object = MibTableRow
ne843UdeEntry = _Ne843UdeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1)
)
ne843UdeEntry.setIndexNames(
    (0, "NE843-MIB", "ne843UdeEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843UdeEntry.setStatus("current")


class _Ne843UdeEntryIndex_Type(Integer32):
    """Custom type ne843UdeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843UdeEntryIndex_Type.__name__ = "Integer32"
_Ne843UdeEntryIndex_Object = MibTableColumn
ne843UdeEntryIndex = _Ne843UdeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 1),
    _Ne843UdeEntryIndex_Type()
)
ne843UdeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843UdeEntryIndex.setStatus("current")
_Ne843UdeEntryIde_Type = DisplayString
_Ne843UdeEntryIde_Object = MibTableColumn
ne843UdeEntryIde = _Ne843UdeEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 2),
    _Ne843UdeEntryIde_Type()
)
ne843UdeEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843UdeEntryIde.setStatus("current")
_Ne843UdeEntryDes_Type = DisplayString
_Ne843UdeEntryDes_Object = MibTableColumn
ne843UdeEntryDes = _Ne843UdeEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 3),
    _Ne843UdeEntryDes_Type()
)
ne843UdeEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryDes.setStatus("current")
_Ne843UdeEntryFds_Type = DisplayString
_Ne843UdeEntryFds_Object = MibTableColumn
ne843UdeEntryFds = _Ne843UdeEntryFds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 4),
    _Ne843UdeEntryFds_Type()
)
ne843UdeEntryFds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryFds.setStatus("current")
_Ne843UdeEntryAst_Type = DisplayString
_Ne843UdeEntryAst_Object = MibTableColumn
ne843UdeEntryAst = _Ne843UdeEntryAst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 5),
    _Ne843UdeEntryAst_Type()
)
ne843UdeEntryAst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843UdeEntryAst.setStatus("current")
_Ne843UdeEntrySev_Type = DisplayString
_Ne843UdeEntrySev_Object = MibTableColumn
ne843UdeEntrySev = _Ne843UdeEntrySev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 6),
    _Ne843UdeEntrySev_Type()
)
ne843UdeEntrySev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntrySev.setStatus("current")
_Ne843UdeEntryPrg_Type = DisplayString
_Ne843UdeEntryPrg_Object = MibTableColumn
ne843UdeEntryPrg = _Ne843UdeEntryPrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 7),
    _Ne843UdeEntryPrg_Type()
)
ne843UdeEntryPrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryPrg.setStatus("current")
_Ne843UdeEntryDur_Type = DisplayString
_Ne843UdeEntryDur_Object = MibTableColumn
ne843UdeEntryDur = _Ne843UdeEntryDur_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 8),
    _Ne843UdeEntryDur_Type()
)
ne843UdeEntryDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryDur.setStatus("current")
_Ne843UdeEntryLed_Type = DisplayString
_Ne843UdeEntryLed_Object = MibTableColumn
ne843UdeEntryLed = _Ne843UdeEntryLed_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 9),
    _Ne843UdeEntryLed_Type()
)
ne843UdeEntryLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryLed.setStatus("current")


class _Ne843UdeEntryLat_Type(Integer32):
    """Custom type ne843UdeEntryLat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843UdeEntryLat_Type.__name__ = "Integer32"
_Ne843UdeEntryLat_Object = MibTableColumn
ne843UdeEntryLat = _Ne843UdeEntryLat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 10),
    _Ne843UdeEntryLat_Type()
)
ne843UdeEntryLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryLat.setStatus("current")
_Ne843UdeEntryAcc_Type = DisplayString
_Ne843UdeEntryAcc_Object = MibTableColumn
ne843UdeEntryAcc = _Ne843UdeEntryAcc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 11),
    _Ne843UdeEntryAcc_Type()
)
ne843UdeEntryAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryAcc.setStatus("current")


class _Ne843UdeEntryDly_Type(Integer32):
    """Custom type ne843UdeEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 540),
    )


_Ne843UdeEntryDly_Type.__name__ = "Integer32"
_Ne843UdeEntryDly_Object = MibTableColumn
ne843UdeEntryDly = _Ne843UdeEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 12),
    _Ne843UdeEntryDly_Type()
)
ne843UdeEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryDly.setStatus("current")
if mibBuilder.loadTexts:
    ne843UdeEntryDly.setUnits("Seconds")


class _Ne843UdeEntryNoo_Type(Integer32):
    """Custom type ne843UdeEntryNoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843UdeEntryNoo_Type.__name__ = "Integer32"
_Ne843UdeEntryNoo_Object = MibTableColumn
ne843UdeEntryNoo = _Ne843UdeEntryNoo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 13),
    _Ne843UdeEntryNoo_Type()
)
ne843UdeEntryNoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryNoo.setStatus("current")


class _Ne843UdeEntryNor_Type(Integer32):
    """Custom type ne843UdeEntryNor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843UdeEntryNor_Type.__name__ = "Integer32"
_Ne843UdeEntryNor_Object = MibTableColumn
ne843UdeEntryNor = _Ne843UdeEntryNor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 14),
    _Ne843UdeEntryNor_Type()
)
ne843UdeEntryNor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryNor.setStatus("current")


class _Ne843UdeEntryNag_Type(Integer32):
    """Custom type ne843UdeEntryNag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843UdeEntryNag_Type.__name__ = "Integer32"
_Ne843UdeEntryNag_Object = MibTableColumn
ne843UdeEntryNag = _Ne843UdeEntryNag_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 15),
    _Ne843UdeEntryNag_Type()
)
ne843UdeEntryNag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryNag.setStatus("current")
_Ne843UdeEntryDst_Type = DisplayString
_Ne843UdeEntryDst_Object = MibTableColumn
ne843UdeEntryDst = _Ne843UdeEntryDst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 16),
    _Ne843UdeEntryDst_Type()
)
ne843UdeEntryDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843UdeEntryDst.setStatus("current")


class _Ne843UdeEntryAst1_Type(Integer32):
    """Custom type ne843UdeEntryAst1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843UdeEntryAst1_Type.__name__ = "Integer32"
_Ne843UdeEntryAst1_Object = MibTableColumn
ne843UdeEntryAst1 = _Ne843UdeEntryAst1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 17, 1, 17),
    _Ne843UdeEntryAst1_Type()
)
ne843UdeEntryAst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843UdeEntryAst1.setStatus("current")
_Ne843Cm1_ObjectIdentity = ObjectIdentity
ne843Cm1 = _Ne843Cm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18)
)
_Ne843Cm1Ide_Type = DisplayString
_Ne843Cm1Ide_Object = MibScalar
ne843Cm1Ide = _Ne843Cm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 1),
    _Ne843Cm1Ide_Type()
)
ne843Cm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cm1Ide.setStatus("current")
_Ne843Cm1Des_Type = DisplayString
_Ne843Cm1Des_Object = MibScalar
ne843Cm1Des = _Ne843Cm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 2),
    _Ne843Cm1Des_Type()
)
ne843Cm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cm1Des.setStatus("current")


class _Ne843Cm1Ngi_Type(Integer32):
    """Custom type ne843Cm1Ngi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_Ne843Cm1Ngi_Type.__name__ = "Integer32"
_Ne843Cm1Ngi_Object = MibScalar
ne843Cm1Ngi = _Ne843Cm1Ngi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 3),
    _Ne843Cm1Ngi_Type()
)
ne843Cm1Ngi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cm1Ngi.setStatus("current")
_Ne843Cm1Cof_Type = DisplayString
_Ne843Cm1Cof_Object = MibScalar
ne843Cm1Cof = _Ne843Cm1Cof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 4),
    _Ne843Cm1Cof_Type()
)
ne843Cm1Cof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cm1Cof.setStatus("current")
_Ne843Cm1Cor_Type = DisplayString
_Ne843Cm1Cor_Object = MibScalar
ne843Cm1Cor = _Ne843Cm1Cor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 5),
    _Ne843Cm1Cor_Type()
)
ne843Cm1Cor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cm1Cor.setStatus("current")
_Ne843Cm1Nnc_Type = DisplayString
_Ne843Cm1Nnc_Object = MibScalar
ne843Cm1Nnc = _Ne843Cm1Nnc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 18, 6),
    _Ne843Cm1Nnc_Type()
)
ne843Cm1Nnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cm1Nnc.setStatus("current")
_Ne843CopTable_Object = MibTable
ne843CopTable = _Ne843CopTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19)
)
if mibBuilder.loadTexts:
    ne843CopTable.setStatus("current")
_Ne843CopEntry_Object = MibTableRow
ne843CopEntry = _Ne843CopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1)
)
ne843CopEntry.setIndexNames(
    (0, "NE843-MIB", "ne843CopEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843CopEntry.setStatus("current")


class _Ne843CopEntryIndex_Type(Integer32):
    """Custom type ne843CopEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843CopEntryIndex_Type.__name__ = "Integer32"
_Ne843CopEntryIndex_Object = MibTableColumn
ne843CopEntryIndex = _Ne843CopEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 1),
    _Ne843CopEntryIndex_Type()
)
ne843CopEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CopEntryIndex.setStatus("current")
_Ne843CopEntryIde_Type = DisplayString
_Ne843CopEntryIde_Object = MibTableColumn
ne843CopEntryIde = _Ne843CopEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 2),
    _Ne843CopEntryIde_Type()
)
ne843CopEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CopEntryIde.setStatus("current")
_Ne843CopEntryDes_Type = DisplayString
_Ne843CopEntryDes_Object = MibTableColumn
ne843CopEntryDes = _Ne843CopEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 3),
    _Ne843CopEntryDes_Type()
)
ne843CopEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryDes.setStatus("current")
_Ne843CopEntryTyp_Type = DisplayString
_Ne843CopEntryTyp_Object = MibTableColumn
ne843CopEntryTyp = _Ne843CopEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 4),
    _Ne843CopEntryTyp_Type()
)
ne843CopEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryTyp.setStatus("current")
_Ne843CopEntryPhn_Type = DisplayString
_Ne843CopEntryPhn_Object = MibTableColumn
ne843CopEntryPhn = _Ne843CopEntryPhn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 5),
    _Ne843CopEntryPhn_Type()
)
ne843CopEntryPhn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryPhn.setStatus("current")


class _Ne843CopEntryBdr_Type(Integer32):
    """Custom type ne843CopEntryBdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843CopEntryBdr_Type.__name__ = "Integer32"
_Ne843CopEntryBdr_Object = MibTableColumn
ne843CopEntryBdr = _Ne843CopEntryBdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 6),
    _Ne843CopEntryBdr_Type()
)
ne843CopEntryBdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryBdr.setStatus("current")


class _Ne843CopEntryDbt_Type(Integer32):
    """Custom type ne843CopEntryDbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Ne843CopEntryDbt_Type.__name__ = "Integer32"
_Ne843CopEntryDbt_Object = MibTableColumn
ne843CopEntryDbt = _Ne843CopEntryDbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 7),
    _Ne843CopEntryDbt_Type()
)
ne843CopEntryDbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryDbt.setStatus("current")
_Ne843CopEntryPry_Type = DisplayString
_Ne843CopEntryPry_Object = MibTableColumn
ne843CopEntryPry = _Ne843CopEntryPry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 8),
    _Ne843CopEntryPry_Type()
)
ne843CopEntryPry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryPry.setStatus("current")


class _Ne843CopEntrySbt_Type(Integer32):
    """Custom type ne843CopEntrySbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Ne843CopEntrySbt_Type.__name__ = "Integer32"
_Ne843CopEntrySbt_Object = MibTableColumn
ne843CopEntrySbt = _Ne843CopEntrySbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 9),
    _Ne843CopEntrySbt_Type()
)
ne843CopEntrySbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntrySbt.setStatus("current")


class _Ne843CopEntryDly_Type(Integer32):
    """Custom type ne843CopEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Ne843CopEntryDly_Type.__name__ = "Integer32"
_Ne843CopEntryDly_Object = MibTableColumn
ne843CopEntryDly = _Ne843CopEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 10),
    _Ne843CopEntryDly_Type()
)
ne843CopEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryDly.setStatus("current")
_Ne843CopEntryPgr_Type = DisplayString
_Ne843CopEntryPgr_Object = MibTableColumn
ne843CopEntryPgr = _Ne843CopEntryPgr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 11),
    _Ne843CopEntryPgr_Type()
)
ne843CopEntryPgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryPgr.setStatus("current")
_Ne843CopEntryMsg_Type = DisplayString
_Ne843CopEntryMsg_Object = MibTableColumn
ne843CopEntryMsg = _Ne843CopEntryMsg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 19, 1, 12),
    _Ne843CopEntryMsg_Type()
)
ne843CopEntryMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CopEntryMsg.setStatus("current")
_Ne843CoeTable_Object = MibTable
ne843CoeTable = _Ne843CoeTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20)
)
if mibBuilder.loadTexts:
    ne843CoeTable.setStatus("current")
_Ne843CoeEntry_Object = MibTableRow
ne843CoeEntry = _Ne843CoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1)
)
ne843CoeEntry.setIndexNames(
    (0, "NE843-MIB", "ne843CoeEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843CoeEntry.setStatus("current")


class _Ne843CoeEntryIndex_Type(Integer32):
    """Custom type ne843CoeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843CoeEntryIndex_Type.__name__ = "Integer32"
_Ne843CoeEntryIndex_Object = MibTableColumn
ne843CoeEntryIndex = _Ne843CoeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1, 1),
    _Ne843CoeEntryIndex_Type()
)
ne843CoeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CoeEntryIndex.setStatus("current")
_Ne843CoeEntryIde_Type = DisplayString
_Ne843CoeEntryIde_Object = MibTableColumn
ne843CoeEntryIde = _Ne843CoeEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1, 2),
    _Ne843CoeEntryIde_Type()
)
ne843CoeEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843CoeEntryIde.setStatus("current")
_Ne843CoeEntryDes_Type = DisplayString
_Ne843CoeEntryDes_Object = MibTableColumn
ne843CoeEntryDes = _Ne843CoeEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1, 3),
    _Ne843CoeEntryDes_Type()
)
ne843CoeEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CoeEntryDes.setStatus("current")
_Ne843CoeEntryAdr_Type = DisplayString
_Ne843CoeEntryAdr_Object = MibTableColumn
ne843CoeEntryAdr = _Ne843CoeEntryAdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1, 4),
    _Ne843CoeEntryAdr_Type()
)
ne843CoeEntryAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CoeEntryAdr.setStatus("current")
_Ne843CoeEntryTyp_Type = DisplayString
_Ne843CoeEntryTyp_Object = MibTableColumn
ne843CoeEntryTyp = _Ne843CoeEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 20, 1, 5),
    _Ne843CoeEntryTyp_Type()
)
ne843CoeEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843CoeEntryTyp.setStatus("current")
_Ne843SndTable_Object = MibTable
ne843SndTable = _Ne843SndTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21)
)
if mibBuilder.loadTexts:
    ne843SndTable.setStatus("current")
_Ne843SndEntry_Object = MibTableRow
ne843SndEntry = _Ne843SndEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1)
)
ne843SndEntry.setIndexNames(
    (0, "NE843-MIB", "ne843SndEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843SndEntry.setStatus("current")


class _Ne843SndEntryIndex_Type(Integer32):
    """Custom type ne843SndEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843SndEntryIndex_Type.__name__ = "Integer32"
_Ne843SndEntryIndex_Object = MibTableColumn
ne843SndEntryIndex = _Ne843SndEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1, 1),
    _Ne843SndEntryIndex_Type()
)
ne843SndEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843SndEntryIndex.setStatus("current")
_Ne843SndEntryIde_Type = DisplayString
_Ne843SndEntryIde_Object = MibTableColumn
ne843SndEntryIde = _Ne843SndEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1, 2),
    _Ne843SndEntryIde_Type()
)
ne843SndEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843SndEntryIde.setStatus("current")
_Ne843SndEntryDes_Type = DisplayString
_Ne843SndEntryDes_Object = MibTableColumn
ne843SndEntryDes = _Ne843SndEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1, 3),
    _Ne843SndEntryDes_Type()
)
ne843SndEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843SndEntryDes.setStatus("current")
_Ne843SndEntryIp_Type = DisplayString
_Ne843SndEntryIp_Object = MibTableColumn
ne843SndEntryIp = _Ne843SndEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1, 4),
    _Ne843SndEntryIp_Type()
)
ne843SndEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843SndEntryIp.setStatus("current")
_Ne843SndEntryCs_Type = DisplayString
_Ne843SndEntryCs_Object = MibTableColumn
ne843SndEntryCs = _Ne843SndEntryCs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 21, 1, 5),
    _Ne843SndEntryCs_Type()
)
ne843SndEntryCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843SndEntryCs.setStatus("current")
_Ne843Po1_ObjectIdentity = ObjectIdentity
ne843Po1 = _Ne843Po1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22)
)
_Ne843Po1Ide_Type = DisplayString
_Ne843Po1Ide_Object = MibScalar
ne843Po1Ide = _Ne843Po1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 1),
    _Ne843Po1Ide_Type()
)
ne843Po1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Po1Ide.setStatus("current")
_Ne843Po1Des_Type = DisplayString
_Ne843Po1Des_Object = MibScalar
ne843Po1Des = _Ne843Po1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 2),
    _Ne843Po1Des_Type()
)
ne843Po1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Des.setStatus("current")
_Ne843Po1Phn_Type = DisplayString
_Ne843Po1Phn_Object = MibScalar
ne843Po1Phn = _Ne843Po1Phn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 3),
    _Ne843Po1Phn_Type()
)
ne843Po1Phn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Phn.setStatus("current")


class _Ne843Po1Bdr_Type(Integer32):
    """Custom type ne843Po1Bdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Po1Bdr_Type.__name__ = "Integer32"
_Ne843Po1Bdr_Object = MibScalar
ne843Po1Bdr = _Ne843Po1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 4),
    _Ne843Po1Bdr_Type()
)
ne843Po1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Bdr.setStatus("current")


class _Ne843Po1Dbt_Type(Integer32):
    """Custom type ne843Po1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Ne843Po1Dbt_Type.__name__ = "Integer32"
_Ne843Po1Dbt_Object = MibScalar
ne843Po1Dbt = _Ne843Po1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 5),
    _Ne843Po1Dbt_Type()
)
ne843Po1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Dbt.setStatus("current")
_Ne843Po1Pry_Type = DisplayString
_Ne843Po1Pry_Object = MibScalar
ne843Po1Pry = _Ne843Po1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 6),
    _Ne843Po1Pry_Type()
)
ne843Po1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Pry.setStatus("current")


class _Ne843Po1Sbt_Type(Integer32):
    """Custom type ne843Po1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Ne843Po1Sbt_Type.__name__ = "Integer32"
_Ne843Po1Sbt_Object = MibScalar
ne843Po1Sbt = _Ne843Po1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 7),
    _Ne843Po1Sbt_Type()
)
ne843Po1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Sbt.setStatus("current")
_Ne843Po1Int_Type = DisplayString
_Ne843Po1Int_Object = MibScalar
ne843Po1Int = _Ne843Po1Int_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 8),
    _Ne843Po1Int_Type()
)
ne843Po1Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Int.setStatus("current")
_Ne843Po1Tim_Type = DisplayString
_Ne843Po1Tim_Object = MibScalar
ne843Po1Tim = _Ne843Po1Tim_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 9),
    _Ne843Po1Tim_Type()
)
ne843Po1Tim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Tim.setStatus("current")
_Ne843Po1Cl01_Type = DisplayString
_Ne843Po1Cl01_Object = MibScalar
ne843Po1Cl01 = _Ne843Po1Cl01_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 10),
    _Ne843Po1Cl01_Type()
)
ne843Po1Cl01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl01.setStatus("current")
_Ne843Po1Cl02_Type = DisplayString
_Ne843Po1Cl02_Object = MibScalar
ne843Po1Cl02 = _Ne843Po1Cl02_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 11),
    _Ne843Po1Cl02_Type()
)
ne843Po1Cl02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl02.setStatus("current")
_Ne843Po1Cl03_Type = DisplayString
_Ne843Po1Cl03_Object = MibScalar
ne843Po1Cl03 = _Ne843Po1Cl03_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 12),
    _Ne843Po1Cl03_Type()
)
ne843Po1Cl03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl03.setStatus("current")
_Ne843Po1Cl04_Type = DisplayString
_Ne843Po1Cl04_Object = MibScalar
ne843Po1Cl04 = _Ne843Po1Cl04_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 13),
    _Ne843Po1Cl04_Type()
)
ne843Po1Cl04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl04.setStatus("current")
_Ne843Po1Cl05_Type = DisplayString
_Ne843Po1Cl05_Object = MibScalar
ne843Po1Cl05 = _Ne843Po1Cl05_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 14),
    _Ne843Po1Cl05_Type()
)
ne843Po1Cl05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl05.setStatus("current")
_Ne843Po1Cl06_Type = DisplayString
_Ne843Po1Cl06_Object = MibScalar
ne843Po1Cl06 = _Ne843Po1Cl06_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 15),
    _Ne843Po1Cl06_Type()
)
ne843Po1Cl06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl06.setStatus("current")
_Ne843Po1Cl07_Type = DisplayString
_Ne843Po1Cl07_Object = MibScalar
ne843Po1Cl07 = _Ne843Po1Cl07_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 16),
    _Ne843Po1Cl07_Type()
)
ne843Po1Cl07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl07.setStatus("current")
_Ne843Po1Cl08_Type = DisplayString
_Ne843Po1Cl08_Object = MibScalar
ne843Po1Cl08 = _Ne843Po1Cl08_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 17),
    _Ne843Po1Cl08_Type()
)
ne843Po1Cl08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl08.setStatus("current")
_Ne843Po1Cl09_Type = DisplayString
_Ne843Po1Cl09_Object = MibScalar
ne843Po1Cl09 = _Ne843Po1Cl09_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 18),
    _Ne843Po1Cl09_Type()
)
ne843Po1Cl09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl09.setStatus("current")
_Ne843Po1Cl10_Type = DisplayString
_Ne843Po1Cl10_Object = MibScalar
ne843Po1Cl10 = _Ne843Po1Cl10_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 19),
    _Ne843Po1Cl10_Type()
)
ne843Po1Cl10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Po1Cl10.setStatus("current")
_Ne843Po1Por_Type = DisplayString
_Ne843Po1Por_Object = MibScalar
ne843Po1Por = _Ne843Po1Por_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 22, 20),
    _Ne843Po1Por_Type()
)
ne843Po1Por.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Po1Por.setStatus("current")
_Ne843Cb1_ObjectIdentity = ObjectIdentity
ne843Cb1 = _Ne843Cb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23)
)
_Ne843Cb1Ide_Type = DisplayString
_Ne843Cb1Ide_Object = MibScalar
ne843Cb1Ide = _Ne843Cb1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 1),
    _Ne843Cb1Ide_Type()
)
ne843Cb1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Cb1Ide.setStatus("current")
_Ne843Cb1Des_Type = DisplayString
_Ne843Cb1Des_Object = MibScalar
ne843Cb1Des = _Ne843Cb1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 2),
    _Ne843Cb1Des_Type()
)
ne843Cb1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Des.setStatus("current")


class _Ne843Cb1Stt_Type(Integer32):
    """Custom type ne843Cb1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843Cb1Stt_Type.__name__ = "Integer32"
_Ne843Cb1Stt_Object = MibScalar
ne843Cb1Stt = _Ne843Cb1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 3),
    _Ne843Cb1Stt_Type()
)
ne843Cb1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Stt.setStatus("current")
_Ne843Cb1Ph1_Type = DisplayString
_Ne843Cb1Ph1_Object = MibScalar
ne843Cb1Ph1 = _Ne843Cb1Ph1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 4),
    _Ne843Cb1Ph1_Type()
)
ne843Cb1Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Ph1.setStatus("current")


class _Ne843Cb1Br1_Type(Integer32):
    """Custom type ne843Cb1Br1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Cb1Br1_Type.__name__ = "Integer32"
_Ne843Cb1Br1_Object = MibScalar
ne843Cb1Br1 = _Ne843Cb1Br1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 5),
    _Ne843Cb1Br1_Type()
)
ne843Cb1Br1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Br1.setStatus("current")
_Ne843Cb1Ph2_Type = DisplayString
_Ne843Cb1Ph2_Object = MibScalar
ne843Cb1Ph2 = _Ne843Cb1Ph2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 6),
    _Ne843Cb1Ph2_Type()
)
ne843Cb1Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Ph2.setStatus("current")


class _Ne843Cb1Br2_Type(Integer32):
    """Custom type ne843Cb1Br2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Cb1Br2_Type.__name__ = "Integer32"
_Ne843Cb1Br2_Object = MibScalar
ne843Cb1Br2 = _Ne843Cb1Br2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 7),
    _Ne843Cb1Br2_Type()
)
ne843Cb1Br2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Br2.setStatus("current")
_Ne843Cb1Ph3_Type = DisplayString
_Ne843Cb1Ph3_Object = MibScalar
ne843Cb1Ph3 = _Ne843Cb1Ph3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 8),
    _Ne843Cb1Ph3_Type()
)
ne843Cb1Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Ph3.setStatus("current")


class _Ne843Cb1Br3_Type(Integer32):
    """Custom type ne843Cb1Br3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Cb1Br3_Type.__name__ = "Integer32"
_Ne843Cb1Br3_Object = MibScalar
ne843Cb1Br3 = _Ne843Cb1Br3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 9),
    _Ne843Cb1Br3_Type()
)
ne843Cb1Br3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Br3.setStatus("current")
_Ne843Cb1Ph4_Type = DisplayString
_Ne843Cb1Ph4_Object = MibScalar
ne843Cb1Ph4 = _Ne843Cb1Ph4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 10),
    _Ne843Cb1Ph4_Type()
)
ne843Cb1Ph4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Ph4.setStatus("current")


class _Ne843Cb1Br4_Type(Integer32):
    """Custom type ne843Cb1Br4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Cb1Br4_Type.__name__ = "Integer32"
_Ne843Cb1Br4_Object = MibScalar
ne843Cb1Br4 = _Ne843Cb1Br4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 11),
    _Ne843Cb1Br4_Type()
)
ne843Cb1Br4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Br4.setStatus("current")
_Ne843Cb1Ph5_Type = DisplayString
_Ne843Cb1Ph5_Object = MibScalar
ne843Cb1Ph5 = _Ne843Cb1Ph5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 12),
    _Ne843Cb1Ph5_Type()
)
ne843Cb1Ph5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Ph5.setStatus("current")


class _Ne843Cb1Br5_Type(Integer32):
    """Custom type ne843Cb1Br5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Cb1Br5_Type.__name__ = "Integer32"
_Ne843Cb1Br5_Object = MibScalar
ne843Cb1Br5 = _Ne843Cb1Br5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 23, 13),
    _Ne843Cb1Br5_Type()
)
ne843Cb1Br5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Cb1Br5.setStatus("current")
_Ne843Mp1_ObjectIdentity = ObjectIdentity
ne843Mp1 = _Ne843Mp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24)
)
_Ne843Mp1Ide_Type = DisplayString
_Ne843Mp1Ide_Object = MibScalar
ne843Mp1Ide = _Ne843Mp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 1),
    _Ne843Mp1Ide_Type()
)
ne843Mp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Mp1Ide.setStatus("current")
_Ne843Mp1Des_Type = DisplayString
_Ne843Mp1Des_Object = MibScalar
ne843Mp1Des = _Ne843Mp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 2),
    _Ne843Mp1Des_Type()
)
ne843Mp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Des.setStatus("current")
_Ne843Mp1Stt_Type = DisplayString
_Ne843Mp1Stt_Object = MibScalar
ne843Mp1Stt = _Ne843Mp1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 3),
    _Ne843Mp1Stt_Type()
)
ne843Mp1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Mp1Stt.setStatus("current")


class _Ne843Mp1Bdr_Type(Integer32):
    """Custom type ne843Mp1Bdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Mp1Bdr_Type.__name__ = "Integer32"
_Ne843Mp1Bdr_Object = MibScalar
ne843Mp1Bdr = _Ne843Mp1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 4),
    _Ne843Mp1Bdr_Type()
)
ne843Mp1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Bdr.setStatus("current")


class _Ne843Mp1Dbt_Type(Integer32):
    """Custom type ne843Mp1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Ne843Mp1Dbt_Type.__name__ = "Integer32"
_Ne843Mp1Dbt_Object = MibScalar
ne843Mp1Dbt = _Ne843Mp1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 5),
    _Ne843Mp1Dbt_Type()
)
ne843Mp1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Dbt.setStatus("current")
_Ne843Mp1Pry_Type = DisplayString
_Ne843Mp1Pry_Object = MibScalar
ne843Mp1Pry = _Ne843Mp1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 6),
    _Ne843Mp1Pry_Type()
)
ne843Mp1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Pry.setStatus("current")


class _Ne843Mp1Sbt_Type(Integer32):
    """Custom type ne843Mp1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Ne843Mp1Sbt_Type.__name__ = "Integer32"
_Ne843Mp1Sbt_Object = MibScalar
ne843Mp1Sbt = _Ne843Mp1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 7),
    _Ne843Mp1Sbt_Type()
)
ne843Mp1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Sbt.setStatus("current")


class _Ne843Mp1Tmo_Type(Integer32):
    """Custom type ne843Mp1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_Ne843Mp1Tmo_Type.__name__ = "Integer32"
_Ne843Mp1Tmo_Object = MibScalar
ne843Mp1Tmo = _Ne843Mp1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 8),
    _Ne843Mp1Tmo_Type()
)
ne843Mp1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Tmo.setStatus("current")
_Ne843Mp1Hsh_Type = DisplayString
_Ne843Mp1Hsh_Object = MibScalar
ne843Mp1Hsh = _Ne843Mp1Hsh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 9),
    _Ne843Mp1Hsh_Type()
)
ne843Mp1Hsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Hsh.setStatus("current")


class _Ne843Mp1Nrg_Type(Integer32):
    """Custom type ne843Mp1Nrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Ne843Mp1Nrg_Type.__name__ = "Integer32"
_Ne843Mp1Nrg_Object = MibScalar
ne843Mp1Nrg = _Ne843Mp1Nrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 10),
    _Ne843Mp1Nrg_Type()
)
ne843Mp1Nrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Nrg.setStatus("current")


class _Ne843Mp1Wre_Type(Integer32):
    """Custom type ne843Mp1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Mp1Wre_Type.__name__ = "Integer32"
_Ne843Mp1Wre_Object = MibScalar
ne843Mp1Wre = _Ne843Mp1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 11),
    _Ne843Mp1Wre_Type()
)
ne843Mp1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Wre.setStatus("current")
_Ne843Mp1Ins_Type = DisplayString
_Ne843Mp1Ins_Object = MibScalar
ne843Mp1Ins = _Ne843Mp1Ins_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 24, 12),
    _Ne843Mp1Ins_Type()
)
ne843Mp1Ins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Mp1Ins.setStatus("current")
_Ne843Lp1_ObjectIdentity = ObjectIdentity
ne843Lp1 = _Ne843Lp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25)
)
_Ne843Lp1Ide_Type = DisplayString
_Ne843Lp1Ide_Object = MibScalar
ne843Lp1Ide = _Ne843Lp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 1),
    _Ne843Lp1Ide_Type()
)
ne843Lp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Lp1Ide.setStatus("current")
_Ne843Lp1Des_Type = DisplayString
_Ne843Lp1Des_Object = MibScalar
ne843Lp1Des = _Ne843Lp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 2),
    _Ne843Lp1Des_Type()
)
ne843Lp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Des.setStatus("current")
_Ne843Lp1Stt_Type = DisplayString
_Ne843Lp1Stt_Object = MibScalar
ne843Lp1Stt = _Ne843Lp1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 3),
    _Ne843Lp1Stt_Type()
)
ne843Lp1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Lp1Stt.setStatus("current")


class _Ne843Lp1Bdr_Type(Integer32):
    """Custom type ne843Lp1Bdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b300", 300),
          ("b1200", 1200),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200))
    )


_Ne843Lp1Bdr_Type.__name__ = "Integer32"
_Ne843Lp1Bdr_Object = MibScalar
ne843Lp1Bdr = _Ne843Lp1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 4),
    _Ne843Lp1Bdr_Type()
)
ne843Lp1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Bdr.setStatus("current")


class _Ne843Lp1Dbt_Type(Integer32):
    """Custom type ne843Lp1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Ne843Lp1Dbt_Type.__name__ = "Integer32"
_Ne843Lp1Dbt_Object = MibScalar
ne843Lp1Dbt = _Ne843Lp1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 5),
    _Ne843Lp1Dbt_Type()
)
ne843Lp1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Dbt.setStatus("current")
_Ne843Lp1Pry_Type = DisplayString
_Ne843Lp1Pry_Object = MibScalar
ne843Lp1Pry = _Ne843Lp1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 6),
    _Ne843Lp1Pry_Type()
)
ne843Lp1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Pry.setStatus("current")


class _Ne843Lp1Sbt_Type(Integer32):
    """Custom type ne843Lp1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Ne843Lp1Sbt_Type.__name__ = "Integer32"
_Ne843Lp1Sbt_Object = MibScalar
ne843Lp1Sbt = _Ne843Lp1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 7),
    _Ne843Lp1Sbt_Type()
)
ne843Lp1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Sbt.setStatus("current")


class _Ne843Lp1Tmo_Type(Integer32):
    """Custom type ne843Lp1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_Ne843Lp1Tmo_Type.__name__ = "Integer32"
_Ne843Lp1Tmo_Object = MibScalar
ne843Lp1Tmo = _Ne843Lp1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 8),
    _Ne843Lp1Tmo_Type()
)
ne843Lp1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Tmo.setStatus("current")
_Ne843Lp1Hsh_Type = DisplayString
_Ne843Lp1Hsh_Object = MibScalar
ne843Lp1Hsh = _Ne843Lp1Hsh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 9),
    _Ne843Lp1Hsh_Type()
)
ne843Lp1Hsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Hsh.setStatus("current")
_Ne843Lp1App_Type = DisplayString
_Ne843Lp1App_Object = MibScalar
ne843Lp1App = _Ne843Lp1App_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 10),
    _Ne843Lp1App_Type()
)
ne843Lp1App.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1App.setStatus("current")


class _Ne843Lp1Wre_Type(Integer32):
    """Custom type ne843Lp1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Lp1Wre_Type.__name__ = "Integer32"
_Ne843Lp1Wre_Object = MibScalar
ne843Lp1Wre = _Ne843Lp1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 25, 11),
    _Ne843Lp1Wre_Type()
)
ne843Lp1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Lp1Wre.setStatus("current")
_Ne843Tlm1_ObjectIdentity = ObjectIdentity
ne843Tlm1 = _Ne843Tlm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26)
)
_Ne843Tlm1Ide_Type = DisplayString
_Ne843Tlm1Ide_Object = MibScalar
ne843Tlm1Ide = _Ne843Tlm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26, 1),
    _Ne843Tlm1Ide_Type()
)
ne843Tlm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Tlm1Ide.setStatus("current")
_Ne843Tlm1Des_Type = DisplayString
_Ne843Tlm1Des_Object = MibScalar
ne843Tlm1Des = _Ne843Tlm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26, 2),
    _Ne843Tlm1Des_Type()
)
ne843Tlm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tlm1Des.setStatus("current")


class _Ne843Tlm1Aue_Type(Integer32):
    """Custom type ne843Tlm1Aue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Tlm1Aue_Type.__name__ = "Integer32"
_Ne843Tlm1Aue_Object = MibScalar
ne843Tlm1Aue = _Ne843Tlm1Aue_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26, 3),
    _Ne843Tlm1Aue_Type()
)
ne843Tlm1Aue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tlm1Aue.setStatus("current")
_Ne843Tlm1Prt_Type = Integer32
_Ne843Tlm1Prt_Object = MibScalar
ne843Tlm1Prt = _Ne843Tlm1Prt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26, 4),
    _Ne843Tlm1Prt_Type()
)
ne843Tlm1Prt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tlm1Prt.setStatus("current")


class _Ne843Tlm1Tmo_Type(Integer32):
    """Custom type ne843Tlm1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Ne843Tlm1Tmo_Type.__name__ = "Integer32"
_Ne843Tlm1Tmo_Object = MibScalar
ne843Tlm1Tmo = _Ne843Tlm1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 26, 5),
    _Ne843Tlm1Tmo_Type()
)
ne843Tlm1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tlm1Tmo.setStatus("current")
if mibBuilder.loadTexts:
    ne843Tlm1Tmo.setUnits("Minutes")
_Ne843Tl1Table_Object = MibTable
ne843Tl1Table = _Ne843Tl1Table_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27)
)
if mibBuilder.loadTexts:
    ne843Tl1Table.setStatus("current")
_Ne843Tl1Entry_Object = MibTableRow
ne843Tl1Entry = _Ne843Tl1Entry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1)
)
ne843Tl1Entry.setIndexNames(
    (0, "NE843-MIB", "ne843Tl1EntryIndex"),
)
if mibBuilder.loadTexts:
    ne843Tl1Entry.setStatus("current")


class _Ne843Tl1EntryIndex_Type(Integer32):
    """Custom type ne843Tl1EntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843Tl1EntryIndex_Type.__name__ = "Integer32"
_Ne843Tl1EntryIndex_Object = MibTableColumn
ne843Tl1EntryIndex = _Ne843Tl1EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 1),
    _Ne843Tl1EntryIndex_Type()
)
ne843Tl1EntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Tl1EntryIndex.setStatus("current")
_Ne843Tl1EntryIde_Type = DisplayString
_Ne843Tl1EntryIde_Object = MibTableColumn
ne843Tl1EntryIde = _Ne843Tl1EntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 2),
    _Ne843Tl1EntryIde_Type()
)
ne843Tl1EntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Tl1EntryIde.setStatus("current")
_Ne843Tl1EntryDes_Type = DisplayString
_Ne843Tl1EntryDes_Object = MibTableColumn
ne843Tl1EntryDes = _Ne843Tl1EntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 3),
    _Ne843Tl1EntryDes_Type()
)
ne843Tl1EntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntryDes.setStatus("current")
_Ne843Tl1EntryCds_Type = DisplayString
_Ne843Tl1EntryCds_Object = MibTableColumn
ne843Tl1EntryCds = _Ne843Tl1EntryCds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 4),
    _Ne843Tl1EntryCds_Type()
)
ne843Tl1EntryCds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntryCds.setStatus("current")
_Ne843Tl1EntryAid_Type = DisplayString
_Ne843Tl1EntryAid_Object = MibTableColumn
ne843Tl1EntryAid = _Ne843Tl1EntryAid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 5),
    _Ne843Tl1EntryAid_Type()
)
ne843Tl1EntryAid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntryAid.setStatus("current")
_Ne843Tl1EntryCnd_Type = DisplayString
_Ne843Tl1EntryCnd_Object = MibTableColumn
ne843Tl1EntryCnd = _Ne843Tl1EntryCnd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 6),
    _Ne843Tl1EntryCnd_Type()
)
ne843Tl1EntryCnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntryCnd.setStatus("current")


class _Ne843Tl1EntrySaf_Type(Integer32):
    """Custom type ne843Tl1EntrySaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843Tl1EntrySaf_Type.__name__ = "Integer32"
_Ne843Tl1EntrySaf_Object = MibTableColumn
ne843Tl1EntrySaf = _Ne843Tl1EntrySaf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 7),
    _Ne843Tl1EntrySaf_Type()
)
ne843Tl1EntrySaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntrySaf.setStatus("current")
_Ne843Tl1EntryRpt_Type = DisplayString
_Ne843Tl1EntryRpt_Object = MibTableColumn
ne843Tl1EntryRpt = _Ne843Tl1EntryRpt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 27, 1, 8),
    _Ne843Tl1EntryRpt_Type()
)
ne843Tl1EntryRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Tl1EntryRpt.setStatus("current")
_Ne843Net1_ObjectIdentity = ObjectIdentity
ne843Net1 = _Ne843Net1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28)
)
_Ne843Net1Ide_Type = DisplayString
_Ne843Net1Ide_Object = MibScalar
ne843Net1Ide = _Ne843Net1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 1),
    _Ne843Net1Ide_Type()
)
ne843Net1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Ide.setStatus("current")
_Ne843Net1Des_Type = DisplayString
_Ne843Net1Des_Object = MibScalar
ne843Net1Des = _Ne843Net1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 2),
    _Ne843Net1Des_Type()
)
ne843Net1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Des.setStatus("current")
_Ne843Net1Ead_Type = DisplayString
_Ne843Net1Ead_Object = MibScalar
ne843Net1Ead = _Ne843Net1Ead_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 3),
    _Ne843Net1Ead_Type()
)
ne843Net1Ead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Ead.setStatus("current")


class _Ne843Net1Dhcp_Type(Integer32):
    """Custom type ne843Net1Dhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcpClient", 1),
          ("dhcpServer", 2))
    )


_Ne843Net1Dhcp_Type.__name__ = "Integer32"
_Ne843Net1Dhcp_Object = MibScalar
ne843Net1Dhcp = _Ne843Net1Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 4),
    _Ne843Net1Dhcp_Type()
)
ne843Net1Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Dhcp.setStatus("current")
_Ne843Net1Ip_Type = DisplayString
_Ne843Net1Ip_Object = MibScalar
ne843Net1Ip = _Ne843Net1Ip_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 5),
    _Ne843Net1Ip_Type()
)
ne843Net1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Ip.setStatus("current")
_Ne843Net1Wip_Type = DisplayString
_Ne843Net1Wip_Object = MibScalar
ne843Net1Wip = _Ne843Net1Wip_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 6),
    _Ne843Net1Wip_Type()
)
ne843Net1Wip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Wip.setStatus("current")
_Ne843Net1Sub_Type = DisplayString
_Ne843Net1Sub_Object = MibScalar
ne843Net1Sub = _Ne843Net1Sub_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 7),
    _Ne843Net1Sub_Type()
)
ne843Net1Sub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Sub.setStatus("current")
_Ne843Net1Gtwy_Type = DisplayString
_Ne843Net1Gtwy_Object = MibScalar
ne843Net1Gtwy = _Ne843Net1Gtwy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 8),
    _Ne843Net1Gtwy_Type()
)
ne843Net1Gtwy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Gtwy.setStatus("current")
_Ne843Net1Host_Type = DisplayString
_Ne843Net1Host_Object = MibScalar
ne843Net1Host = _Ne843Net1Host_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 9),
    _Ne843Net1Host_Type()
)
ne843Net1Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Host.setStatus("current")
_Ne843Net1Dom_Type = DisplayString
_Ne843Net1Dom_Object = MibScalar
ne843Net1Dom = _Ne843Net1Dom_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 10),
    _Ne843Net1Dom_Type()
)
ne843Net1Dom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Dom.setStatus("current")
_Ne843Net1Dns_Type = DisplayString
_Ne843Net1Dns_Object = MibScalar
ne843Net1Dns = _Ne843Net1Dns_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 11),
    _Ne843Net1Dns_Type()
)
ne843Net1Dns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Dns.setStatus("current")


class _Ne843Net1Wre_Type(Integer32):
    """Custom type ne843Net1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Wre_Type.__name__ = "Integer32"
_Ne843Net1Wre_Object = MibScalar
ne843Net1Wre = _Ne843Net1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 12),
    _Ne843Net1Wre_Type()
)
ne843Net1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Wre.setStatus("current")


class _Ne843Net1Tmo_Type(Integer32):
    """Custom type ne843Net1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Ne843Net1Tmo_Type.__name__ = "Integer32"
_Ne843Net1Tmo_Object = MibScalar
ne843Net1Tmo = _Ne843Net1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 13),
    _Ne843Net1Tmo_Type()
)
ne843Net1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Tmo.setStatus("current")
if mibBuilder.loadTexts:
    ne843Net1Tmo.setUnits("Minutes")
_Ne843Net1Msrv_Type = DisplayString
_Ne843Net1Msrv_Object = MibScalar
ne843Net1Msrv = _Ne843Net1Msrv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 14),
    _Ne843Net1Msrv_Type()
)
ne843Net1Msrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Msrv.setStatus("current")
_Ne843Net1Ntp_Type = DisplayString
_Ne843Net1Ntp_Object = MibScalar
ne843Net1Ntp = _Ne843Net1Ntp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 15),
    _Ne843Net1Ntp_Type()
)
ne843Net1Ntp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Ntp.setStatus("current")
_Ne843Net1Sma_Type = DisplayString
_Ne843Net1Sma_Object = MibScalar
ne843Net1Sma = _Ne843Net1Sma_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 16),
    _Ne843Net1Sma_Type()
)
ne843Net1Sma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Sma.setStatus("current")
_Ne843Net1Sid_Type = DisplayString
_Ne843Net1Sid_Object = MibScalar
ne843Net1Sid = _Ne843Net1Sid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 17),
    _Ne843Net1Sid_Type()
)
ne843Net1Sid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Sid.setStatus("current")


class _Ne843Net1Fpe_Type(Integer32):
    """Custom type ne843Net1Fpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Fpe_Type.__name__ = "Integer32"
_Ne843Net1Fpe_Object = MibScalar
ne843Net1Fpe = _Ne843Net1Fpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 18),
    _Ne843Net1Fpe_Type()
)
ne843Net1Fpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Fpe.setStatus("current")


class _Ne843Net1Hpe_Type(Integer32):
    """Custom type ne843Net1Hpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Hpe_Type.__name__ = "Integer32"
_Ne843Net1Hpe_Object = MibScalar
ne843Net1Hpe = _Ne843Net1Hpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 19),
    _Ne843Net1Hpe_Type()
)
ne843Net1Hpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Hpe.setStatus("current")


class _Ne843Net1Hse_Type(Integer32):
    """Custom type ne843Net1Hse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Hse_Type.__name__ = "Integer32"
_Ne843Net1Hse_Object = MibScalar
ne843Net1Hse = _Ne843Net1Hse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 20),
    _Ne843Net1Hse_Type()
)
ne843Net1Hse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Hse.setStatus("current")


class _Ne843Net1She_Type(Integer32):
    """Custom type ne843Net1She based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1She_Type.__name__ = "Integer32"
_Ne843Net1She_Object = MibScalar
ne843Net1She = _Ne843Net1She_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 21),
    _Ne843Net1She_Type()
)
ne843Net1She.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1She.setStatus("current")


class _Ne843Net1Sne_Type(Integer32):
    """Custom type ne843Net1Sne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Sne_Type.__name__ = "Integer32"
_Ne843Net1Sne_Object = MibScalar
ne843Net1Sne = _Ne843Net1Sne_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 22),
    _Ne843Net1Sne_Type()
)
ne843Net1Sne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Sne.setStatus("current")


class _Ne843Net1Tle_Type(Integer32):
    """Custom type ne843Net1Tle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Net1Tle_Type.__name__ = "Integer32"
_Ne843Net1Tle_Object = MibScalar
ne843Net1Tle = _Ne843Net1Tle_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 23),
    _Ne843Net1Tle_Type()
)
ne843Net1Tle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Tle.setStatus("current")
_Ne843Net1Ip6_Type = DisplayString
_Ne843Net1Ip6_Object = MibScalar
ne843Net1Ip6 = _Ne843Net1Ip6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 24),
    _Ne843Net1Ip6_Type()
)
ne843Net1Ip6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Ip6.setStatus("current")
_Ne843Net1Gtwy6_Type = DisplayString
_Ne843Net1Gtwy6_Object = MibScalar
ne843Net1Gtwy6 = _Ne843Net1Gtwy6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 25),
    _Ne843Net1Gtwy6_Type()
)
ne843Net1Gtwy6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Gtwy6.setStatus("current")
_Ne843Net1Wip6_Type = DisplayString
_Ne843Net1Wip6_Object = MibScalar
ne843Net1Wip6 = _Ne843Net1Wip6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 26),
    _Ne843Net1Wip6_Type()
)
ne843Net1Wip6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Wip6.setStatus("current")
_Ne843Net1Ll6_Type = DisplayString
_Ne843Net1Ll6_Object = MibScalar
ne843Net1Ll6 = _Ne843Net1Ll6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 27),
    _Ne843Net1Ll6_Type()
)
ne843Net1Ll6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Ll6.setStatus("current")


class _Ne843Net1Pl6_Type(Integer32):
    """Custom type ne843Net1Pl6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Ne843Net1Pl6_Type.__name__ = "Integer32"
_Ne843Net1Pl6_Object = MibScalar
ne843Net1Pl6 = _Ne843Net1Pl6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 28),
    _Ne843Net1Pl6_Type()
)
ne843Net1Pl6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Net1Pl6.setStatus("current")
_Ne843Net1Wgtwy6_Type = DisplayString
_Ne843Net1Wgtwy6_Object = MibScalar
ne843Net1Wgtwy6 = _Ne843Net1Wgtwy6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 28, 29),
    _Ne843Net1Wgtwy6_Type()
)
ne843Net1Wgtwy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Net1Wgtwy6.setStatus("current")
_Ne843DrcTable_Object = MibTable
ne843DrcTable = _Ne843DrcTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29)
)
if mibBuilder.loadTexts:
    ne843DrcTable.setStatus("current")
_Ne843DrcEntry_Object = MibTableRow
ne843DrcEntry = _Ne843DrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1)
)
ne843DrcEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DrcEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DrcEntry.setStatus("current")


class _Ne843DrcEntryIndex_Type(Integer32):
    """Custom type ne843DrcEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DrcEntryIndex_Type.__name__ = "Integer32"
_Ne843DrcEntryIndex_Object = MibTableColumn
ne843DrcEntryIndex = _Ne843DrcEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 1),
    _Ne843DrcEntryIndex_Type()
)
ne843DrcEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DrcEntryIndex.setStatus("current")
_Ne843DrcEntryIde_Type = DisplayString
_Ne843DrcEntryIde_Object = MibTableColumn
ne843DrcEntryIde = _Ne843DrcEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 2),
    _Ne843DrcEntryIde_Type()
)
ne843DrcEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DrcEntryIde.setStatus("current")
_Ne843DrcEntryDes_Type = DisplayString
_Ne843DrcEntryDes_Object = MibTableColumn
ne843DrcEntryDes = _Ne843DrcEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 3),
    _Ne843DrcEntryDes_Type()
)
ne843DrcEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DrcEntryDes.setStatus("current")
_Ne843DrcEntryVal_Type = DisplayString
_Ne843DrcEntryVal_Object = MibTableColumn
ne843DrcEntryVal = _Ne843DrcEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 4),
    _Ne843DrcEntryVal_Type()
)
ne843DrcEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DrcEntryVal.setStatus("current")
_Ne843DrcEntryPrg_Type = DisplayString
_Ne843DrcEntryPrg_Object = MibTableColumn
ne843DrcEntryPrg = _Ne843DrcEntryPrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 5),
    _Ne843DrcEntryPrg_Type()
)
ne843DrcEntryPrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DrcEntryPrg.setStatus("current")
_Ne843DrcEntryUni_Type = DisplayString
_Ne843DrcEntryUni_Object = MibTableColumn
ne843DrcEntryUni = _Ne843DrcEntryUni_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 29, 1, 6),
    _Ne843DrcEntryUni_Type()
)
ne843DrcEntryUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DrcEntryUni.setStatus("current")
_Ne843InpTable_Object = MibTable
ne843InpTable = _Ne843InpTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30)
)
if mibBuilder.loadTexts:
    ne843InpTable.setStatus("current")
_Ne843InpEntry_Object = MibTableRow
ne843InpEntry = _Ne843InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1)
)
ne843InpEntry.setIndexNames(
    (0, "NE843-MIB", "ne843InpEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843InpEntry.setStatus("current")


class _Ne843InpEntryIndex_Type(Integer32):
    """Custom type ne843InpEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843InpEntryIndex_Type.__name__ = "Integer32"
_Ne843InpEntryIndex_Object = MibTableColumn
ne843InpEntryIndex = _Ne843InpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 1),
    _Ne843InpEntryIndex_Type()
)
ne843InpEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InpEntryIndex.setStatus("current")
_Ne843InpEntryIde_Type = DisplayString
_Ne843InpEntryIde_Object = MibTableColumn
ne843InpEntryIde = _Ne843InpEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 2),
    _Ne843InpEntryIde_Type()
)
ne843InpEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InpEntryIde.setStatus("current")
_Ne843InpEntryDes_Type = DisplayString
_Ne843InpEntryDes_Object = MibTableColumn
ne843InpEntryDes = _Ne843InpEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 3),
    _Ne843InpEntryDes_Type()
)
ne843InpEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InpEntryDes.setStatus("current")


class _Ne843InpEntryStt_Type(Integer32):
    """Custom type ne843InpEntryStt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonAlarming", 0),
          ("alarming", 1))
    )


_Ne843InpEntryStt_Type.__name__ = "Integer32"
_Ne843InpEntryStt_Object = MibTableColumn
ne843InpEntryStt = _Ne843InpEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 4),
    _Ne843InpEntryStt_Type()
)
ne843InpEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InpEntryStt.setStatus("current")
_Ne843InpEntryTyp_Type = DisplayString
_Ne843InpEntryTyp_Object = MibTableColumn
ne843InpEntryTyp = _Ne843InpEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 5),
    _Ne843InpEntryTyp_Type()
)
ne843InpEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InpEntryTyp.setStatus("current")
_Ne843InpEntryPol_Type = DisplayString
_Ne843InpEntryPol_Object = MibTableColumn
ne843InpEntryPol = _Ne843InpEntryPol_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 6),
    _Ne843InpEntryPol_Type()
)
ne843InpEntryPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InpEntryPol.setStatus("current")
_Ne843InpEntrySn_Type = DisplayString
_Ne843InpEntrySn_Object = MibTableColumn
ne843InpEntrySn = _Ne843InpEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 7),
    _Ne843InpEntrySn_Type()
)
ne843InpEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InpEntrySn.setStatus("current")
_Ne843InpEntryBrc_Type = DisplayString
_Ne843InpEntryBrc_Object = MibTableColumn
ne843InpEntryBrc = _Ne843InpEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 30, 1, 8),
    _Ne843InpEntryBrc_Type()
)
ne843InpEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InpEntryBrc.setStatus("current")
_Ne843MsvTable_Object = MibTable
ne843MsvTable = _Ne843MsvTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31)
)
if mibBuilder.loadTexts:
    ne843MsvTable.setStatus("current")
_Ne843MsvEntry_Object = MibTableRow
ne843MsvEntry = _Ne843MsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1)
)
ne843MsvEntry.setIndexNames(
    (0, "NE843-MIB", "ne843MsvEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843MsvEntry.setStatus("current")


class _Ne843MsvEntryIndex_Type(Integer32):
    """Custom type ne843MsvEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843MsvEntryIndex_Type.__name__ = "Integer32"
_Ne843MsvEntryIndex_Object = MibTableColumn
ne843MsvEntryIndex = _Ne843MsvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 1),
    _Ne843MsvEntryIndex_Type()
)
ne843MsvEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryIndex.setStatus("current")
_Ne843MsvEntryIde_Type = DisplayString
_Ne843MsvEntryIde_Object = MibTableColumn
ne843MsvEntryIde = _Ne843MsvEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 2),
    _Ne843MsvEntryIde_Type()
)
ne843MsvEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryIde.setStatus("current")
_Ne843MsvEntryDes_Type = DisplayString
_Ne843MsvEntryDes_Object = MibTableColumn
ne843MsvEntryDes = _Ne843MsvEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 3),
    _Ne843MsvEntryDes_Type()
)
ne843MsvEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843MsvEntryDes.setStatus("current")
_Ne843MsvEntryStt_Type = DisplayString
_Ne843MsvEntryStt_Object = MibTableColumn
ne843MsvEntryStt = _Ne843MsvEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 4),
    _Ne843MsvEntryStt_Type()
)
ne843MsvEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryStt.setStatus("current")
_Ne843MsvEntryVal_Type = Integer32
_Ne843MsvEntryVal_Object = MibTableColumn
ne843MsvEntryVal = _Ne843MsvEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 5),
    _Ne843MsvEntryVal_Type()
)
ne843MsvEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryVal.setStatus("current")
if mibBuilder.loadTexts:
    ne843MsvEntryVal.setUnits("mV")
_Ne843MsvEntryDid_Type = DisplayString
_Ne843MsvEntryDid_Object = MibTableColumn
ne843MsvEntryDid = _Ne843MsvEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 6),
    _Ne843MsvEntryDid_Type()
)
ne843MsvEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryDid.setStatus("current")


class _Ne843MsvEntryDid1_Type(Integer32):
    """Custom type ne843MsvEntryDid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843MsvEntryDid1_Type.__name__ = "Integer32"
_Ne843MsvEntryDid1_Object = MibTableColumn
ne843MsvEntryDid1 = _Ne843MsvEntryDid1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 31, 1, 7),
    _Ne843MsvEntryDid1_Type()
)
ne843MsvEntryDid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843MsvEntryDid1.setStatus("current")
_Ne843Rp1_ObjectIdentity = ObjectIdentity
ne843Rp1 = _Ne843Rp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32)
)
_Ne843Rp1Ide_Type = DisplayString
_Ne843Rp1Ide_Object = MibScalar
ne843Rp1Ide = _Ne843Rp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 1),
    _Ne843Rp1Ide_Type()
)
ne843Rp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Ide.setStatus("current")
_Ne843Rp1Des_Type = DisplayString
_Ne843Rp1Des_Object = MibScalar
ne843Rp1Des = _Ne843Rp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 2),
    _Ne843Rp1Des_Type()
)
ne843Rp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Des.setStatus("current")


class _Ne843Rp1Frq_Type(Integer32):
    """Custom type ne843Rp1Frq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 50),
    )


_Ne843Rp1Frq_Type.__name__ = "Integer32"
_Ne843Rp1Frq_Object = MibScalar
ne843Rp1Frq = _Ne843Rp1Frq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 3),
    _Ne843Rp1Frq_Type()
)
ne843Rp1Frq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Frq.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rp1Frq.setUnits("Hz")


class _Ne843Rp1Vsp_Type(Integer32):
    """Custom type ne843Rp1Vsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 100),
    )


_Ne843Rp1Vsp_Type.__name__ = "Integer32"
_Ne843Rp1Vsp_Object = MibScalar
ne843Rp1Vsp = _Ne843Rp1Vsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 4),
    _Ne843Rp1Vsp_Type()
)
ne843Rp1Vsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Vsp.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rp1Vsp.setUnits("Volts")


class _Ne843Rp1Ofe_Type(Integer32):
    """Custom type ne843Rp1Ofe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Rp1Ofe_Type.__name__ = "Integer32"
_Ne843Rp1Ofe_Object = MibScalar
ne843Rp1Ofe = _Ne843Rp1Ofe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 5),
    _Ne843Rp1Ofe_Type()
)
ne843Rp1Ofe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Ofe.setStatus("current")


class _Ne843Rp1Rme_Type(Integer32):
    """Custom type ne843Rp1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Rp1Rme_Type.__name__ = "Integer32"
_Ne843Rp1Rme_Object = MibScalar
ne843Rp1Rme = _Ne843Rp1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 6),
    _Ne843Rp1Rme_Type()
)
ne843Rp1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Rme.setStatus("current")


class _Ne843Rp1Rss_Type(Integer32):
    """Custom type ne843Rp1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_Ne843Rp1Rss_Type.__name__ = "Integer32"
_Ne843Rp1Rss_Object = MibScalar
ne843Rp1Rss = _Ne843Rp1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 7),
    _Ne843Rp1Rss_Type()
)
ne843Rp1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Rss.setStatus("current")
_Ne843Rp1Rf_Type = DisplayString
_Ne843Rp1Rf_Object = MibScalar
ne843Rp1Rf = _Ne843Rp1Rf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 8),
    _Ne843Rp1Rf_Type()
)
ne843Rp1Rf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rf.setStatus("current")
_Ne843Rp1Rpff_Type = DisplayString
_Ne843Rp1Rpff_Object = MibScalar
ne843Rp1Rpff = _Ne843Rp1Rpff_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 9),
    _Ne843Rp1Rpff_Type()
)
ne843Rp1Rpff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rpff.setStatus("current")
_Ne843Rp1Rprl_Type = DisplayString
_Ne843Rp1Rprl_Object = MibScalar
ne843Rp1Rprl = _Ne843Rp1Rprl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 10),
    _Ne843Rp1Rprl_Type()
)
ne843Rp1Rprl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rprl.setStatus("current")
_Ne843Rp1Rpfj_Type = DisplayString
_Ne843Rp1Rpfj_Object = MibScalar
ne843Rp1Rpfj = _Ne843Rp1Rpfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 11),
    _Ne843Rp1Rpfj_Type()
)
ne843Rp1Rpfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rpfj.setStatus("current")
_Ne843Rp1Rpxj_Type = DisplayString
_Ne843Rp1Rpxj_Object = MibScalar
ne843Rp1Rpxj = _Ne843Rp1Rpxj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 12),
    _Ne843Rp1Rpxj_Type()
)
ne843Rp1Rpxj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rpxj.setStatus("current")
_Ne843Rp1Rpxn_Type = DisplayString
_Ne843Rp1Rpxn_Object = MibScalar
ne843Rp1Rpxn = _Ne843Rp1Rpxn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 13),
    _Ne843Rp1Rpxn_Type()
)
ne843Rp1Rpxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rpxn.setStatus("current")
_Ne843Rp1Rcdp_Type = DisplayString
_Ne843Rp1Rcdp_Object = MibScalar
ne843Rp1Rcdp = _Ne843Rp1Rcdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 14),
    _Ne843Rp1Rcdp_Type()
)
ne843Rp1Rcdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Rcdp.setStatus("current")
_Ne843Rp1Cap_Type = Integer32
_Ne843Rp1Cap_Object = MibScalar
ne843Rp1Cap = _Ne843Rp1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 15),
    _Ne843Rp1Cap_Type()
)
ne843Rp1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Cap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rp1Cap.setUnits("VA")
_Ne843Rp1Olcap_Type = Integer32
_Ne843Rp1Olcap_Object = MibScalar
ne843Rp1Olcap = _Ne843Rp1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 16),
    _Ne843Rp1Olcap_Type()
)
ne843Rp1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rp1Olcap.setUnits("VA")
_Ne843Rp1Va_Type = Integer32
_Ne843Rp1Va_Object = MibScalar
ne843Rp1Va = _Ne843Rp1Va_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 17),
    _Ne843Rp1Va_Type()
)
ne843Rp1Va.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rp1Va.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rp1Va.setUnits("VA")


class _Ne843Rp1Rrf_Type(Integer32):
    """Custom type ne843Rp1Rrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Rp1Rrf_Type.__name__ = "Integer32"
_Ne843Rp1Rrf_Object = MibScalar
ne843Rp1Rrf = _Ne843Rp1Rrf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 32, 18),
    _Ne843Rp1Rrf_Type()
)
ne843Rp1Rrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rp1Rrf.setStatus("current")
_Ne843RchTable_Object = MibTable
ne843RchTable = _Ne843RchTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33)
)
if mibBuilder.loadTexts:
    ne843RchTable.setStatus("current")
_Ne843RchEntry_Object = MibTableRow
ne843RchEntry = _Ne843RchEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1)
)
ne843RchEntry.setIndexNames(
    (0, "NE843-MIB", "ne843RchEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843RchEntry.setStatus("current")


class _Ne843RchEntryIndex_Type(Integer32):
    """Custom type ne843RchEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843RchEntryIndex_Type.__name__ = "Integer32"
_Ne843RchEntryIndex_Object = MibTableColumn
ne843RchEntryIndex = _Ne843RchEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 1),
    _Ne843RchEntryIndex_Type()
)
ne843RchEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryIndex.setStatus("current")
_Ne843RchEntryIde_Type = DisplayString
_Ne843RchEntryIde_Object = MibTableColumn
ne843RchEntryIde = _Ne843RchEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 2),
    _Ne843RchEntryIde_Type()
)
ne843RchEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryIde.setStatus("current")
_Ne843RchEntryDes_Type = DisplayString
_Ne843RchEntryDes_Object = MibTableColumn
ne843RchEntryDes = _Ne843RchEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 3),
    _Ne843RchEntryDes_Type()
)
ne843RchEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RchEntryDes.setStatus("current")
_Ne843RchEntryStt_Type = DisplayString
_Ne843RchEntryStt_Object = MibTableColumn
ne843RchEntryStt = _Ne843RchEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 4),
    _Ne843RchEntryStt_Type()
)
ne843RchEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843RchEntryStt.setStatus("current")
_Ne843RchEntryVa_Type = Integer32
_Ne843RchEntryVa_Object = MibTableColumn
ne843RchEntryVa = _Ne843RchEntryVa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 5),
    _Ne843RchEntryVa_Type()
)
ne843RchEntryVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryVa.setStatus("current")
if mibBuilder.loadTexts:
    ne843RchEntryVa.setUnits("mVA")
_Ne843RchEntryPri_Type = DisplayString
_Ne843RchEntryPri_Object = MibTableColumn
ne843RchEntryPri = _Ne843RchEntryPri_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 6),
    _Ne843RchEntryPri_Type()
)
ne843RchEntryPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryPri.setStatus("current")
_Ne843RchEntrySec_Type = DisplayString
_Ne843RchEntrySec_Object = MibTableColumn
ne843RchEntrySec = _Ne843RchEntrySec_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 7),
    _Ne843RchEntrySec_Type()
)
ne843RchEntrySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntrySec.setStatus("current")


class _Ne843RchEntryRf_Type(Integer32):
    """Custom type ne843RchEntryRf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRf_Type.__name__ = "Integer32"
_Ne843RchEntryRf_Object = MibTableColumn
ne843RchEntryRf = _Ne843RchEntryRf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 8),
    _Ne843RchEntryRf_Type()
)
ne843RchEntryRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRf.setStatus("current")


class _Ne843RchEntryRpff_Type(Integer32):
    """Custom type ne843RchEntryRpff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRpff_Type.__name__ = "Integer32"
_Ne843RchEntryRpff_Object = MibTableColumn
ne843RchEntryRpff = _Ne843RchEntryRpff_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 9),
    _Ne843RchEntryRpff_Type()
)
ne843RchEntryRpff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRpff.setStatus("current")


class _Ne843RchEntryRpxj_Type(Integer32):
    """Custom type ne843RchEntryRpxj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRpxj_Type.__name__ = "Integer32"
_Ne843RchEntryRpxj_Object = MibTableColumn
ne843RchEntryRpxj = _Ne843RchEntryRpxj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 10),
    _Ne843RchEntryRpxj_Type()
)
ne843RchEntryRpxj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRpxj.setStatus("current")


class _Ne843RchEntryRpxn_Type(Integer32):
    """Custom type ne843RchEntryRpxn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRpxn_Type.__name__ = "Integer32"
_Ne843RchEntryRpxn_Object = MibTableColumn
ne843RchEntryRpxn = _Ne843RchEntryRpxn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 11),
    _Ne843RchEntryRpxn_Type()
)
ne843RchEntryRpxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRpxn.setStatus("current")


class _Ne843RchEntryRprl_Type(Integer32):
    """Custom type ne843RchEntryRprl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRprl_Type.__name__ = "Integer32"
_Ne843RchEntryRprl_Object = MibTableColumn
ne843RchEntryRprl = _Ne843RchEntryRprl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 12),
    _Ne843RchEntryRprl_Type()
)
ne843RchEntryRprl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRprl.setStatus("current")


class _Ne843RchEntryRpfj_Type(Integer32):
    """Custom type ne843RchEntryRpfj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRpfj_Type.__name__ = "Integer32"
_Ne843RchEntryRpfj_Object = MibTableColumn
ne843RchEntryRpfj = _Ne843RchEntryRpfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 13),
    _Ne843RchEntryRpfj_Type()
)
ne843RchEntryRpfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRpfj.setStatus("current")


class _Ne843RchEntryRcdp_Type(Integer32):
    """Custom type ne843RchEntryRcdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843RchEntryRcdp_Type.__name__ = "Integer32"
_Ne843RchEntryRcdp_Object = MibTableColumn
ne843RchEntryRcdp = _Ne843RchEntryRcdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 14),
    _Ne843RchEntryRcdp_Type()
)
ne843RchEntryRcdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryRcdp.setStatus("current")
_Ne843RchEntryPsn_Type = DisplayString
_Ne843RchEntryPsn_Object = MibTableColumn
ne843RchEntryPsn = _Ne843RchEntryPsn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 15),
    _Ne843RchEntryPsn_Type()
)
ne843RchEntryPsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryPsn.setStatus("current")
_Ne843RchEntryPtyp_Type = DisplayString
_Ne843RchEntryPtyp_Object = MibTableColumn
ne843RchEntryPtyp = _Ne843RchEntryPtyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 16),
    _Ne843RchEntryPtyp_Type()
)
ne843RchEntryPtyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryPtyp.setStatus("current")
_Ne843RchEntryPstt_Type = DisplayString
_Ne843RchEntryPstt_Object = MibTableColumn
ne843RchEntryPstt = _Ne843RchEntryPstt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 17),
    _Ne843RchEntryPstt_Type()
)
ne843RchEntryPstt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryPstt.setStatus("current")
_Ne843RchEntrySsn_Type = DisplayString
_Ne843RchEntrySsn_Object = MibTableColumn
ne843RchEntrySsn = _Ne843RchEntrySsn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 18),
    _Ne843RchEntrySsn_Type()
)
ne843RchEntrySsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntrySsn.setStatus("current")
_Ne843RchEntryStyp_Type = DisplayString
_Ne843RchEntryStyp_Object = MibTableColumn
ne843RchEntryStyp = _Ne843RchEntryStyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 19),
    _Ne843RchEntryStyp_Type()
)
ne843RchEntryStyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryStyp.setStatus("current")
_Ne843RchEntrySstt_Type = DisplayString
_Ne843RchEntrySstt_Object = MibTableColumn
ne843RchEntrySstt = _Ne843RchEntrySstt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 20),
    _Ne843RchEntrySstt_Type()
)
ne843RchEntrySstt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntrySstt.setStatus("current")
_Ne843RchEntryCap_Type = Integer32
_Ne843RchEntryCap_Object = MibTableColumn
ne843RchEntryCap = _Ne843RchEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 33, 1, 21),
    _Ne843RchEntryCap_Type()
)
ne843RchEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843RchEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    ne843RchEntryCap.setUnits("VA")
_Ne843AlarmTable_Object = MibTable
ne843AlarmTable = _Ne843AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34)
)
if mibBuilder.loadTexts:
    ne843AlarmTable.setStatus("current")
_Ne843AlarmEntry_Object = MibTableRow
ne843AlarmEntry = _Ne843AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1)
)
ne843AlarmEntry.setIndexNames(
    (0, "NE843-MIB", "ne843AlarmEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843AlarmEntry.setStatus("current")


class _Ne843AlarmEntryIndex_Type(Integer32):
    """Custom type ne843AlarmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843AlarmEntryIndex_Type.__name__ = "Integer32"
_Ne843AlarmEntryIndex_Object = MibTableColumn
ne843AlarmEntryIndex = _Ne843AlarmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 1),
    _Ne843AlarmEntryIndex_Type()
)
ne843AlarmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843AlarmEntryIndex.setStatus("current")
_Ne843AlarmEntryDes_Type = DisplayString
_Ne843AlarmEntryDes_Object = MibTableColumn
ne843AlarmEntryDes = _Ne843AlarmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 2),
    _Ne843AlarmEntryDes_Type()
)
ne843AlarmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryDes.setStatus("current")


class _Ne843AlarmEntryAst_Type(Integer32):
    """Custom type ne843AlarmEntryAst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843AlarmEntryAst_Type.__name__ = "Integer32"
_Ne843AlarmEntryAst_Object = MibTableColumn
ne843AlarmEntryAst = _Ne843AlarmEntryAst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 3),
    _Ne843AlarmEntryAst_Type()
)
ne843AlarmEntryAst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843AlarmEntryAst.setStatus("current")
_Ne843AlarmEntrySev_Type = DisplayString
_Ne843AlarmEntrySev_Object = MibTableColumn
ne843AlarmEntrySev = _Ne843AlarmEntrySev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 4),
    _Ne843AlarmEntrySev_Type()
)
ne843AlarmEntrySev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntrySev.setStatus("current")
_Ne843AlarmEntryAcc_Type = DisplayString
_Ne843AlarmEntryAcc_Object = MibTableColumn
ne843AlarmEntryAcc = _Ne843AlarmEntryAcc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 5),
    _Ne843AlarmEntryAcc_Type()
)
ne843AlarmEntryAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryAcc.setStatus("current")
_Ne843AlarmEntryThr_Type = DisplayString
_Ne843AlarmEntryThr_Object = MibTableColumn
ne843AlarmEntryThr = _Ne843AlarmEntryThr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 6),
    _Ne843AlarmEntryThr_Type()
)
ne843AlarmEntryThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryThr.setStatus("current")
_Ne843AlarmEntryFth_Type = Integer32
_Ne843AlarmEntryFth_Object = MibTableColumn
ne843AlarmEntryFth = _Ne843AlarmEntryFth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 7),
    _Ne843AlarmEntryFth_Type()
)
ne843AlarmEntryFth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryFth.setStatus("current")
if mibBuilder.loadTexts:
    ne843AlarmEntryFth.setUnits("mV")
_Ne843AlarmEntryBth_Type = Integer32
_Ne843AlarmEntryBth_Object = MibTableColumn
ne843AlarmEntryBth = _Ne843AlarmEntryBth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 8),
    _Ne843AlarmEntryBth_Type()
)
ne843AlarmEntryBth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryBth.setStatus("current")
if mibBuilder.loadTexts:
    ne843AlarmEntryBth.setUnits("mV")


class _Ne843AlarmEntryDly_Type(Integer32):
    """Custom type ne843AlarmEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 540),
    )


_Ne843AlarmEntryDly_Type.__name__ = "Integer32"
_Ne843AlarmEntryDly_Object = MibTableColumn
ne843AlarmEntryDly = _Ne843AlarmEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 9),
    _Ne843AlarmEntryDly_Type()
)
ne843AlarmEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryDly.setStatus("current")
if mibBuilder.loadTexts:
    ne843AlarmEntryDly.setUnits("Seconds")


class _Ne843AlarmEntryNoo_Type(Integer32):
    """Custom type ne843AlarmEntryNoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843AlarmEntryNoo_Type.__name__ = "Integer32"
_Ne843AlarmEntryNoo_Object = MibTableColumn
ne843AlarmEntryNoo = _Ne843AlarmEntryNoo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 10),
    _Ne843AlarmEntryNoo_Type()
)
ne843AlarmEntryNoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryNoo.setStatus("current")


class _Ne843AlarmEntryNor_Type(Integer32):
    """Custom type ne843AlarmEntryNor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843AlarmEntryNor_Type.__name__ = "Integer32"
_Ne843AlarmEntryNor_Object = MibTableColumn
ne843AlarmEntryNor = _Ne843AlarmEntryNor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 11),
    _Ne843AlarmEntryNor_Type()
)
ne843AlarmEntryNor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryNor.setStatus("current")


class _Ne843AlarmEntryNag_Type(Integer32):
    """Custom type ne843AlarmEntryNag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ne843AlarmEntryNag_Type.__name__ = "Integer32"
_Ne843AlarmEntryNag_Object = MibTableColumn
ne843AlarmEntryNag = _Ne843AlarmEntryNag_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 12),
    _Ne843AlarmEntryNag_Type()
)
ne843AlarmEntryNag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryNag.setStatus("current")
_Ne843AlarmEntryDst_Type = DisplayString
_Ne843AlarmEntryDst_Object = MibTableColumn
ne843AlarmEntryDst = _Ne843AlarmEntryDst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 34, 1, 13),
    _Ne843AlarmEntryDst_Type()
)
ne843AlarmEntryDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843AlarmEntryDst.setStatus("current")
_Ne843Trap_ObjectIdentity = ObjectIdentity
ne843Trap = _Ne843Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35)
)
_Ne843TrapInfo_ObjectIdentity = ObjectIdentity
ne843TrapInfo = _Ne843TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36)
)
_Ne843TrapDesc_Type = DisplayString
_Ne843TrapDesc_Object = MibScalar
ne843TrapDesc = _Ne843TrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36, 1),
    _Ne843TrapDesc_Type()
)
ne843TrapDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ne843TrapDesc.setStatus("current")


class _Ne843TrapSev_Type(Integer32):
    """Custom type ne843TrapSev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("retire", 0),
          ("record", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_Ne843TrapSev_Type.__name__ = "Integer32"
_Ne843TrapSev_Object = MibScalar
ne843TrapSev = _Ne843TrapSev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36, 2),
    _Ne843TrapSev_Type()
)
ne843TrapSev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ne843TrapSev.setStatus("current")
_Ne843TrapTime_Type = DisplayString
_Ne843TrapTime_Object = MibScalar
ne843TrapTime = _Ne843TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36, 3),
    _Ne843TrapTime_Type()
)
ne843TrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ne843TrapTime.setStatus("current")
_Ne843TrapDate_Type = DisplayString
_Ne843TrapDate_Object = MibScalar
ne843TrapDate = _Ne843TrapDate_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36, 4),
    _Ne843TrapDate_Type()
)
ne843TrapDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ne843TrapDate.setStatus("current")
_Ne843TrapPath_Type = DisplayString
_Ne843TrapPath_Object = MibScalar
ne843TrapPath = _Ne843TrapPath_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 36, 5),
    _Ne843TrapPath_Type()
)
ne843TrapPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ne843TrapPath.setStatus("current")
_Ne843Retire_ObjectIdentity = ObjectIdentity
ne843Retire = _Ne843Retire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37)
)
_Ne843Acd1_ObjectIdentity = ObjectIdentity
ne843Acd1 = _Ne843Acd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38)
)
_Ne843Acd1Ide_Type = DisplayString
_Ne843Acd1Ide_Object = MibScalar
ne843Acd1Ide = _Ne843Acd1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 1),
    _Ne843Acd1Ide_Type()
)
ne843Acd1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Ide.setStatus("current")
_Ne843Acd1Des_Type = DisplayString
_Ne843Acd1Des_Object = MibScalar
ne843Acd1Des = _Ne843Acd1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 2),
    _Ne843Acd1Des_Type()
)
ne843Acd1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Des.setStatus("current")
_Ne843Acd1Brc_Type = DisplayString
_Ne843Acd1Brc_Object = MibScalar
ne843Acd1Brc = _Ne843Acd1Brc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 3),
    _Ne843Acd1Brc_Type()
)
ne843Acd1Brc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Brc.setStatus("current")
_Ne843Acd1Sn_Type = DisplayString
_Ne843Acd1Sn_Object = MibScalar
ne843Acd1Sn = _Ne843Acd1Sn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 4),
    _Ne843Acd1Sn_Type()
)
ne843Acd1Sn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Sn.setStatus("current")
_Ne843Acd1Prd_Type = DisplayString
_Ne843Acd1Prd_Object = MibScalar
ne843Acd1Prd = _Ne843Acd1Prd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 5),
    _Ne843Acd1Prd_Type()
)
ne843Acd1Prd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Prd.setStatus("current")
_Ne843Acd1Psd_Type = DisplayString
_Ne843Acd1Psd_Object = MibScalar
ne843Acd1Psd = _Ne843Acd1Psd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 6),
    _Ne843Acd1Psd_Type()
)
ne843Acd1Psd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Psd.setStatus("current")
_Ne843Acd1Ptd_Type = DisplayString
_Ne843Acd1Ptd_Object = MibScalar
ne843Acd1Ptd = _Ne843Acd1Ptd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 7),
    _Ne843Acd1Ptd_Type()
)
ne843Acd1Ptd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Ptd.setStatus("current")
_Ne843Acd1Prv_Type = DisplayString
_Ne843Acd1Prv_Object = MibScalar
ne843Acd1Prv = _Ne843Acd1Prv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 8),
    _Ne843Acd1Prv_Type()
)
ne843Acd1Prv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Prv.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Prv.setUnits("Vrms")
_Ne843Acd1Psv_Type = DisplayString
_Ne843Acd1Psv_Object = MibScalar
ne843Acd1Psv = _Ne843Acd1Psv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 9),
    _Ne843Acd1Psv_Type()
)
ne843Acd1Psv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Psv.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Psv.setUnits("Vrms")
_Ne843Acd1Ptv_Type = DisplayString
_Ne843Acd1Ptv_Object = MibScalar
ne843Acd1Ptv = _Ne843Acd1Ptv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 10),
    _Ne843Acd1Ptv_Type()
)
ne843Acd1Ptv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Ptv.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Ptv.setUnits("Vrms")
_Ne843Acd1Pra_Type = DisplayString
_Ne843Acd1Pra_Object = MibScalar
ne843Acd1Pra = _Ne843Acd1Pra_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 11),
    _Ne843Acd1Pra_Type()
)
ne843Acd1Pra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Pra.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Pra.setUnits("Amps")
_Ne843Acd1Psa_Type = DisplayString
_Ne843Acd1Psa_Object = MibScalar
ne843Acd1Psa = _Ne843Acd1Psa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 12),
    _Ne843Acd1Psa_Type()
)
ne843Acd1Psa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Psa.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Psa.setUnits("Amps")
_Ne843Acd1Pta_Type = DisplayString
_Ne843Acd1Pta_Object = MibScalar
ne843Acd1Pta = _Ne843Acd1Pta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 13),
    _Ne843Acd1Pta_Type()
)
ne843Acd1Pta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Pta.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Pta.setUnits("Amps")
_Ne843Acd1Prf_Type = DisplayString
_Ne843Acd1Prf_Object = MibScalar
ne843Acd1Prf = _Ne843Acd1Prf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 14),
    _Ne843Acd1Prf_Type()
)
ne843Acd1Prf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Prf.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Prf.setUnits("Hz")
_Ne843Acd1Psf_Type = DisplayString
_Ne843Acd1Psf_Object = MibScalar
ne843Acd1Psf = _Ne843Acd1Psf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 15),
    _Ne843Acd1Psf_Type()
)
ne843Acd1Psf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Psf.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Psf.setUnits("Hz")
_Ne843Acd1Ptf_Type = DisplayString
_Ne843Acd1Ptf_Object = MibScalar
ne843Acd1Ptf = _Ne843Acd1Ptf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 16),
    _Ne843Acd1Ptf_Type()
)
ne843Acd1Ptf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Ptf.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Ptf.setUnits("Hz")
_Ne843Acd1Prk_Type = DisplayString
_Ne843Acd1Prk_Object = MibScalar
ne843Acd1Prk = _Ne843Acd1Prk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 17),
    _Ne843Acd1Prk_Type()
)
ne843Acd1Prk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Prk.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Prk.setUnits("kW")
_Ne843Acd1Psk_Type = DisplayString
_Ne843Acd1Psk_Object = MibScalar
ne843Acd1Psk = _Ne843Acd1Psk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 18),
    _Ne843Acd1Psk_Type()
)
ne843Acd1Psk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Psk.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Psk.setUnits("kW")
_Ne843Acd1Ptk_Type = DisplayString
_Ne843Acd1Ptk_Object = MibScalar
ne843Acd1Ptk = _Ne843Acd1Ptk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 19),
    _Ne843Acd1Ptk_Type()
)
ne843Acd1Ptk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Ptk.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Ptk.setUnits("kW")
_Ne843Acd1Syk_Type = DisplayString
_Ne843Acd1Syk_Object = MibScalar
ne843Acd1Syk = _Ne843Acd1Syk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 20),
    _Ne843Acd1Syk_Type()
)
ne843Acd1Syk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Acd1Syk.setStatus("current")
if mibBuilder.loadTexts:
    ne843Acd1Syk.setUnits("kW")
_Ne843Acd1Prx_Type = DisplayString
_Ne843Acd1Prx_Object = MibScalar
ne843Acd1Prx = _Ne843Acd1Prx_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 21),
    _Ne843Acd1Prx_Type()
)
ne843Acd1Prx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Prx.setStatus("current")
_Ne843Acd1Psx_Type = DisplayString
_Ne843Acd1Psx_Object = MibScalar
ne843Acd1Psx = _Ne843Acd1Psx_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 22),
    _Ne843Acd1Psx_Type()
)
ne843Acd1Psx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Psx.setStatus("current")
_Ne843Acd1Ptx_Type = DisplayString
_Ne843Acd1Ptx_Object = MibScalar
ne843Acd1Ptx = _Ne843Acd1Ptx_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 38, 23),
    _Ne843Acd1Ptx_Type()
)
ne843Acd1Ptx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Acd1Ptx.setStatus("current")
_Ne843Gn1_ObjectIdentity = ObjectIdentity
ne843Gn1 = _Ne843Gn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39)
)
_Ne843Gn1Ide_Type = DisplayString
_Ne843Gn1Ide_Object = MibScalar
ne843Gn1Ide = _Ne843Gn1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 1),
    _Ne843Gn1Ide_Type()
)
ne843Gn1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Ide.setStatus("current")
_Ne843Gn1Des_Type = DisplayString
_Ne843Gn1Des_Object = MibScalar
ne843Gn1Des = _Ne843Gn1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 2),
    _Ne843Gn1Des_Type()
)
ne843Gn1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Des.setStatus("current")
_Ne843Gn1Rt_Type = DisplayString
_Ne843Gn1Rt_Object = MibScalar
ne843Gn1Rt = _Ne843Gn1Rt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 3),
    _Ne843Gn1Rt_Type()
)
ne843Gn1Rt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Rt.setStatus("current")
_Ne843Gn1Trt_Type = DisplayString
_Ne843Gn1Trt_Object = MibScalar
ne843Gn1Trt = _Ne843Gn1Trt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 4),
    _Ne843Gn1Trt_Type()
)
ne843Gn1Trt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Trt.setStatus("current")
_Ne843Gn1Gnr_Type = DisplayString
_Ne843Gn1Gnr_Object = MibScalar
ne843Gn1Gnr = _Ne843Gn1Gnr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 5),
    _Ne843Gn1Gnr_Type()
)
ne843Gn1Gnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Gnr.setStatus("current")
_Ne843Gn1Gnm_Type = DisplayString
_Ne843Gn1Gnm_Object = MibScalar
ne843Gn1Gnm = _Ne843Gn1Gnm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 6),
    _Ne843Gn1Gnm_Type()
)
ne843Gn1Gnm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Gnm.setStatus("current")
_Ne843Gn1Gnf_Type = DisplayString
_Ne843Gn1Gnf_Object = MibScalar
ne843Gn1Gnf = _Ne843Gn1Gnf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 7),
    _Ne843Gn1Gnf_Type()
)
ne843Gn1Gnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Gnf.setStatus("current")


class _Ne843Gn1Clt_Type(Integer32):
    """Custom type ne843Gn1Clt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_Ne843Gn1Clt_Type.__name__ = "Integer32"
_Ne843Gn1Clt_Object = MibScalar
ne843Gn1Clt = _Ne843Gn1Clt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 8),
    _Ne843Gn1Clt_Type()
)
ne843Gn1Clt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Clt.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gn1Clt.setUnits("Amps")


class _Ne843Gn1Tv_Type(Integer32):
    """Custom type ne843Gn1Tv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 28),
        ValueRangeConstraint(40, 56),
    )


_Ne843Gn1Tv_Type.__name__ = "Integer32"
_Ne843Gn1Tv_Object = MibScalar
ne843Gn1Tv = _Ne843Gn1Tv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 9),
    _Ne843Gn1Tv_Type()
)
ne843Gn1Tv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tv.setStatus("current")
_Ne843Gn1Tvd_Type = DisplayString
_Ne843Gn1Tvd_Object = MibScalar
ne843Gn1Tvd = _Ne843Gn1Tvd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 10),
    _Ne843Gn1Tvd_Type()
)
ne843Gn1Tvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tvd.setStatus("current")


class _Ne843Gn1Tp_Type(Integer32):
    """Custom type ne843Gn1Tp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Ne843Gn1Tp_Type.__name__ = "Integer32"
_Ne843Gn1Tp_Object = MibScalar
ne843Gn1Tp = _Ne843Gn1Tp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 11),
    _Ne843Gn1Tp_Type()
)
ne843Gn1Tp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tp.setStatus("current")
_Ne843Gn1Tpd_Type = DisplayString
_Ne843Gn1Tpd_Object = MibScalar
ne843Gn1Tpd = _Ne843Gn1Tpd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 12),
    _Ne843Gn1Tpd_Type()
)
ne843Gn1Tpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tpd.setStatus("current")
_Ne843Gn1Tct_Type = Integer32
_Ne843Gn1Tct_Object = MibScalar
ne843Gn1Tct = _Ne843Gn1Tct_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 13),
    _Ne843Gn1Tct_Type()
)
ne843Gn1Tct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tct.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gn1Tct.setUnits("ambient")
_Ne843Gn1Tctd_Type = DisplayString
_Ne843Gn1Tctd_Object = MibScalar
ne843Gn1Tctd = _Ne843Gn1Tctd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 14),
    _Ne843Gn1Tctd_Type()
)
ne843Gn1Tctd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tctd.setStatus("current")
_Ne843Gn1Tht_Type = Integer32
_Ne843Gn1Tht_Object = MibScalar
ne843Gn1Tht = _Ne843Gn1Tht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 15),
    _Ne843Gn1Tht_Type()
)
ne843Gn1Tht.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tht.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gn1Tht.setUnits("ambient")
_Ne843Gn1Thtd_Type = DisplayString
_Ne843Gn1Thtd_Object = MibScalar
ne843Gn1Thtd = _Ne843Gn1Thtd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 16),
    _Ne843Gn1Thtd_Type()
)
ne843Gn1Thtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Thtd.setStatus("current")


class _Ne843Gn1Pv_Type(Integer32):
    """Custom type ne843Gn1Pv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 30),
        ValueRangeConstraint(46, 60),
    )


_Ne843Gn1Pv_Type.__name__ = "Integer32"
_Ne843Gn1Pv_Object = MibScalar
ne843Gn1Pv = _Ne843Gn1Pv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 17),
    _Ne843Gn1Pv_Type()
)
ne843Gn1Pv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pv.setStatus("current")
_Ne843Gn1Pvd_Type = DisplayString
_Ne843Gn1Pvd_Object = MibScalar
ne843Gn1Pvd = _Ne843Gn1Pvd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 18),
    _Ne843Gn1Pvd_Type()
)
ne843Gn1Pvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pvd.setStatus("current")


class _Ne843Gn1Pi_Type(Integer32):
    """Custom type ne843Gn1Pi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_Ne843Gn1Pi_Type.__name__ = "Integer32"
_Ne843Gn1Pi_Object = MibScalar
ne843Gn1Pi = _Ne843Gn1Pi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 19),
    _Ne843Gn1Pi_Type()
)
ne843Gn1Pi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pi.setStatus("current")
_Ne843Gn1Pid_Type = DisplayString
_Ne843Gn1Pid_Object = MibScalar
ne843Gn1Pid = _Ne843Gn1Pid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 20),
    _Ne843Gn1Pid_Type()
)
ne843Gn1Pid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pid.setStatus("current")


class _Ne843Gn1Pp_Type(Integer32):
    """Custom type ne843Gn1Pp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Ne843Gn1Pp_Type.__name__ = "Integer32"
_Ne843Gn1Pp_Object = MibScalar
ne843Gn1Pp = _Ne843Gn1Pp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 21),
    _Ne843Gn1Pp_Type()
)
ne843Gn1Pp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pp.setStatus("current")
_Ne843Gn1Ppd_Type = DisplayString
_Ne843Gn1Ppd_Object = MibScalar
ne843Gn1Ppd = _Ne843Gn1Ppd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 22),
    _Ne843Gn1Ppd_Type()
)
ne843Gn1Ppd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Ppd.setStatus("current")
_Ne843Gn1Pct_Type = Integer32
_Ne843Gn1Pct_Object = MibScalar
ne843Gn1Pct = _Ne843Gn1Pct_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 23),
    _Ne843Gn1Pct_Type()
)
ne843Gn1Pct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pct.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gn1Pct.setUnits("ambient")
_Ne843Gn1Pctd_Type = DisplayString
_Ne843Gn1Pctd_Object = MibScalar
ne843Gn1Pctd = _Ne843Gn1Pctd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 24),
    _Ne843Gn1Pctd_Type()
)
ne843Gn1Pctd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pctd.setStatus("current")
_Ne843Gn1Pht_Type = Integer32
_Ne843Gn1Pht_Object = MibScalar
ne843Gn1Pht = _Ne843Gn1Pht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 25),
    _Ne843Gn1Pht_Type()
)
ne843Gn1Pht.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pht.setStatus("current")
if mibBuilder.loadTexts:
    ne843Gn1Pht.setUnits("ambient")
_Ne843Gn1Phtd_Type = DisplayString
_Ne843Gn1Phtd_Object = MibScalar
ne843Gn1Phtd = _Ne843Gn1Phtd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 26),
    _Ne843Gn1Phtd_Type()
)
ne843Gn1Phtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Phtd.setStatus("current")
_Ne843Gn1Mrt_Type = DisplayString
_Ne843Gn1Mrt_Object = MibScalar
ne843Gn1Mrt = _Ne843Gn1Mrt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 27),
    _Ne843Gn1Mrt_Type()
)
ne843Gn1Mrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Mrt.setStatus("current")


class _Ne843Gn1Tve_Type(Integer32):
    """Custom type ne843Gn1Tve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Tve_Type.__name__ = "Integer32"
_Ne843Gn1Tve_Object = MibScalar
ne843Gn1Tve = _Ne843Gn1Tve_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 28),
    _Ne843Gn1Tve_Type()
)
ne843Gn1Tve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tve.setStatus("current")


class _Ne843Gn1Tpe_Type(Integer32):
    """Custom type ne843Gn1Tpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Tpe_Type.__name__ = "Integer32"
_Ne843Gn1Tpe_Object = MibScalar
ne843Gn1Tpe = _Ne843Gn1Tpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 29),
    _Ne843Gn1Tpe_Type()
)
ne843Gn1Tpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Tpe.setStatus("current")


class _Ne843Gn1Cte_Type(Integer32):
    """Custom type ne843Gn1Cte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Cte_Type.__name__ = "Integer32"
_Ne843Gn1Cte_Object = MibScalar
ne843Gn1Cte = _Ne843Gn1Cte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 30),
    _Ne843Gn1Cte_Type()
)
ne843Gn1Cte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Cte.setStatus("current")


class _Ne843Gn1Hte_Type(Integer32):
    """Custom type ne843Gn1Hte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Hte_Type.__name__ = "Integer32"
_Ne843Gn1Hte_Object = MibScalar
ne843Gn1Hte = _Ne843Gn1Hte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 31),
    _Ne843Gn1Hte_Type()
)
ne843Gn1Hte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Hte.setStatus("current")


class _Ne843Gn1Pve_Type(Integer32):
    """Custom type ne843Gn1Pve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Pve_Type.__name__ = "Integer32"
_Ne843Gn1Pve_Object = MibScalar
ne843Gn1Pve = _Ne843Gn1Pve_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 32),
    _Ne843Gn1Pve_Type()
)
ne843Gn1Pve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pve.setStatus("current")


class _Ne843Gn1Pie_Type(Integer32):
    """Custom type ne843Gn1Pie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Pie_Type.__name__ = "Integer32"
_Ne843Gn1Pie_Object = MibScalar
ne843Gn1Pie = _Ne843Gn1Pie_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 33),
    _Ne843Gn1Pie_Type()
)
ne843Gn1Pie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Pie.setStatus("current")


class _Ne843Gn1Ppe_Type(Integer32):
    """Custom type ne843Gn1Ppe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Ppe_Type.__name__ = "Integer32"
_Ne843Gn1Ppe_Object = MibScalar
ne843Gn1Ppe = _Ne843Gn1Ppe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 34),
    _Ne843Gn1Ppe_Type()
)
ne843Gn1Ppe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Ppe.setStatus("current")


class _Ne843Gn1Nv_Type(Integer32):
    """Custom type ne843Gn1Nv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Ne843Gn1Nv_Type.__name__ = "Integer32"
_Ne843Gn1Nv_Object = MibScalar
ne843Gn1Nv = _Ne843Gn1Nv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 35),
    _Ne843Gn1Nv_Type()
)
ne843Gn1Nv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Nv.setStatus("current")


class _Ne843Gn1Nva_Type(Integer32):
    """Custom type ne843Gn1Nva based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999000),
    )


_Ne843Gn1Nva_Type.__name__ = "Integer32"
_Ne843Gn1Nva_Object = MibScalar
ne843Gn1Nva = _Ne843Gn1Nva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 36),
    _Ne843Gn1Nva_Type()
)
ne843Gn1Nva.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Nva.setStatus("current")


class _Ne843Gn1Ode_Type(Integer32):
    """Custom type ne843Gn1Ode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Ode_Type.__name__ = "Integer32"
_Ne843Gn1Ode_Object = MibScalar
ne843Gn1Ode = _Ne843Gn1Ode_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 37),
    _Ne843Gn1Ode_Type()
)
ne843Gn1Ode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Ode.setStatus("current")
_Ne843Gn1Odr_Type = DisplayString
_Ne843Gn1Odr_Object = MibScalar
ne843Gn1Odr = _Ne843Gn1Odr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 38),
    _Ne843Gn1Odr_Type()
)
ne843Gn1Odr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Odr.setStatus("current")
_Ne843Gn1Ocd_Type = DisplayString
_Ne843Gn1Ocd_Object = MibScalar
ne843Gn1Ocd = _Ne843Gn1Ocd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 39),
    _Ne843Gn1Ocd_Type()
)
ne843Gn1Ocd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Ocd.setStatus("current")
_Ne843Gn1Gns_Type = DisplayString
_Ne843Gn1Gns_Object = MibScalar
ne843Gn1Gns = _Ne843Gn1Gns_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 40),
    _Ne843Gn1Gns_Type()
)
ne843Gn1Gns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Gns.setStatus("current")


class _Ne843Gn1Aue_Type(Integer32):
    """Custom type ne843Gn1Aue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Gn1Aue_Type.__name__ = "Integer32"
_Ne843Gn1Aue_Object = MibScalar
ne843Gn1Aue = _Ne843Gn1Aue_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 41),
    _Ne843Gn1Aue_Type()
)
ne843Gn1Aue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Aue.setStatus("current")
_Ne843Gn1Mod_Type = DisplayString
_Ne843Gn1Mod_Object = MibScalar
ne843Gn1Mod = _Ne843Gn1Mod_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 42),
    _Ne843Gn1Mod_Type()
)
ne843Gn1Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Gn1Mod.setStatus("current")
_Ne843Gn1Stt_Type = DisplayString
_Ne843Gn1Stt_Object = MibScalar
ne843Gn1Stt = _Ne843Gn1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 39, 43),
    _Ne843Gn1Stt_Type()
)
ne843Gn1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Gn1Stt.setStatus("current")
_Ne843BatTable_Object = MibTable
ne843BatTable = _Ne843BatTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40)
)
if mibBuilder.loadTexts:
    ne843BatTable.setStatus("current")
_Ne843BatEntry_Object = MibTableRow
ne843BatEntry = _Ne843BatEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1)
)
ne843BatEntry.setIndexNames(
    (0, "NE843-MIB", "ne843BatEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843BatEntry.setStatus("current")


class _Ne843BatEntryIndex_Type(Integer32):
    """Custom type ne843BatEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843BatEntryIndex_Type.__name__ = "Integer32"
_Ne843BatEntryIndex_Object = MibTableColumn
ne843BatEntryIndex = _Ne843BatEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 1),
    _Ne843BatEntryIndex_Type()
)
ne843BatEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryIndex.setStatus("current")
_Ne843BatEntryIde_Type = DisplayString
_Ne843BatEntryIde_Object = MibTableColumn
ne843BatEntryIde = _Ne843BatEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 2),
    _Ne843BatEntryIde_Type()
)
ne843BatEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryIde.setStatus("current")
_Ne843BatEntryDes_Type = DisplayString
_Ne843BatEntryDes_Object = MibTableColumn
ne843BatEntryDes = _Ne843BatEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 3),
    _Ne843BatEntryDes_Type()
)
ne843BatEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BatEntryDes.setStatus("current")
_Ne843BatEntryCon_Type = DisplayString
_Ne843BatEntryCon_Object = MibTableColumn
ne843BatEntryCon = _Ne843BatEntryCon_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 4),
    _Ne843BatEntryCon_Type()
)
ne843BatEntryCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BatEntryCon.setStatus("current")
_Ne843BatEntryStt_Type = DisplayString
_Ne843BatEntryStt_Object = MibTableColumn
ne843BatEntryStt = _Ne843BatEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 5),
    _Ne843BatEntryStt_Type()
)
ne843BatEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryStt.setStatus("current")
_Ne843BatEntryNst_Type = DisplayString
_Ne843BatEntryNst_Object = MibTableColumn
ne843BatEntryNst = _Ne843BatEntryNst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 6),
    _Ne843BatEntryNst_Type()
)
ne843BatEntryNst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843BatEntryNst.setStatus("current")
_Ne843BatEntryBty_Type = DisplayString
_Ne843BatEntryBty_Object = MibTableColumn
ne843BatEntryBty = _Ne843BatEntryBty_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 7),
    _Ne843BatEntryBty_Type()
)
ne843BatEntryBty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryBty.setStatus("current")
_Ne843BatEntryCap_Type = DisplayString
_Ne843BatEntryCap_Object = MibTableColumn
ne843BatEntryCap = _Ne843BatEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 8),
    _Ne843BatEntryCap_Type()
)
ne843BatEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryCap.setStatus("current")
_Ne843BatEntryDat_Type = DisplayString
_Ne843BatEntryDat_Object = MibTableColumn
ne843BatEntryDat = _Ne843BatEntryDat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 9),
    _Ne843BatEntryDat_Type()
)
ne843BatEntryDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryDat.setStatus("current")
_Ne843BatEntryMpv_Type = DisplayString
_Ne843BatEntryMpv_Object = MibTableColumn
ne843BatEntryMpv = _Ne843BatEntryMpv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 10),
    _Ne843BatEntryMpv_Type()
)
ne843BatEntryMpv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryMpv.setStatus("current")
if mibBuilder.loadTexts:
    ne843BatEntryMpv.setUnits("Volts")
_Ne843BatEntryAdc_Type = DisplayString
_Ne843BatEntryAdc_Object = MibTableColumn
ne843BatEntryAdc = _Ne843BatEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 40, 1, 11),
    _Ne843BatEntryAdc_Type()
)
ne843BatEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843BatEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843BatEntryAdc.setUnits("Amps")
_Ne843Eco1_ObjectIdentity = ObjectIdentity
ne843Eco1 = _Ne843Eco1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41)
)
_Ne843Eco1Ide_Type = DisplayString
_Ne843Eco1Ide_Object = MibScalar
ne843Eco1Ide = _Ne843Eco1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 1),
    _Ne843Eco1Ide_Type()
)
ne843Eco1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Ide.setStatus("current")
_Ne843Eco1Des_Type = DisplayString
_Ne843Eco1Des_Object = MibScalar
ne843Eco1Des = _Ne843Eco1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 2),
    _Ne843Eco1Des_Type()
)
ne843Eco1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Eco1Des.setStatus("current")
_Ne843Eco1Sofs_Type = DisplayString
_Ne843Eco1Sofs_Object = MibScalar
ne843Eco1Sofs = _Ne843Eco1Sofs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 3),
    _Ne843Eco1Sofs_Type()
)
ne843Eco1Sofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Eco1Sofs.setStatus("current")
_Ne843Eco1Ntrd_Type = DisplayString
_Ne843Eco1Ntrd_Object = MibScalar
ne843Eco1Ntrd = _Ne843Eco1Ntrd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 4),
    _Ne843Eco1Ntrd_Type()
)
ne843Eco1Ntrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Ntrd.setStatus("current")
_Ne843Eco1Strd_Type = DisplayString
_Ne843Eco1Strd_Object = MibScalar
ne843Eco1Strd = _Ne843Eco1Strd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 5),
    _Ne843Eco1Strd_Type()
)
ne843Eco1Strd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Strd.setStatus("current")
_Ne843Eco1Nkwh_Type = DisplayString
_Ne843Eco1Nkwh_Object = MibScalar
ne843Eco1Nkwh = _Ne843Eco1Nkwh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 6),
    _Ne843Eco1Nkwh_Type()
)
ne843Eco1Nkwh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Nkwh.setStatus("current")
_Ne843Eco1Skwh_Type = DisplayString
_Ne843Eco1Skwh_Object = MibScalar
ne843Eco1Skwh = _Ne843Eco1Skwh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 7),
    _Ne843Eco1Skwh_Type()
)
ne843Eco1Skwh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Skwh.setStatus("current")
_Ne843Eco1Ncap_Type = DisplayString
_Ne843Eco1Ncap_Object = MibScalar
ne843Eco1Ncap = _Ne843Eco1Ncap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 8),
    _Ne843Eco1Ncap_Type()
)
ne843Eco1Ncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Ncap.setStatus("current")
_Ne843Eco1Nocap_Type = DisplayString
_Ne843Eco1Nocap_Object = MibScalar
ne843Eco1Nocap = _Ne843Eco1Nocap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 41, 9),
    _Ne843Eco1Nocap_Type()
)
ne843Eco1Nocap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Eco1Nocap.setStatus("current")
_Ne843Ivp1_ObjectIdentity = ObjectIdentity
ne843Ivp1 = _Ne843Ivp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42)
)
_Ne843Ivp1Ide_Type = DisplayString
_Ne843Ivp1Ide_Object = MibScalar
ne843Ivp1Ide = _Ne843Ivp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 1),
    _Ne843Ivp1Ide_Type()
)
ne843Ivp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ide.setStatus("current")
_Ne843Ivp1Des_Type = DisplayString
_Ne843Ivp1Des_Object = MibScalar
ne843Ivp1Des = _Ne843Ivp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 2),
    _Ne843Ivp1Des_Type()
)
ne843Ivp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Des.setStatus("current")
_Ne843Ivp1Cap_Type = Integer32
_Ne843Ivp1Cap_Object = MibScalar
ne843Ivp1Cap = _Ne843Ivp1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 3),
    _Ne843Ivp1Cap_Type()
)
ne843Ivp1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Cap.setStatus("current")
if mibBuilder.loadTexts:
    ne843Ivp1Cap.setUnits("Amps")
_Ne843Ivp1Irm_Type = Integer32
_Ne843Ivp1Irm_Object = MibScalar
ne843Ivp1Irm = _Ne843Ivp1Irm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 4),
    _Ne843Ivp1Irm_Type()
)
ne843Ivp1Irm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Irm.setStatus("current")
_Ne843Ivp1Vac_Type = Integer32
_Ne843Ivp1Vac_Object = MibScalar
ne843Ivp1Vac = _Ne843Ivp1Vac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 5),
    _Ne843Ivp1Vac_Type()
)
ne843Ivp1Vac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Vac.setStatus("current")
_Ne843Ivp1Adc_Type = Integer32
_Ne843Ivp1Adc_Object = MibScalar
ne843Ivp1Adc = _Ne843Ivp1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 6),
    _Ne843Ivp1Adc_Type()
)
ne843Ivp1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Adc.setStatus("current")
_Ne843Ivp1Vdc_Type = Integer32
_Ne843Ivp1Vdc_Object = MibScalar
ne843Ivp1Vdc = _Ne843Ivp1Vdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 7),
    _Ne843Ivp1Vdc_Type()
)
ne843Ivp1Vdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Vdc.setStatus("current")
_Ne843Ivp1Frq_Type = Integer32
_Ne843Ivp1Frq_Object = MibScalar
ne843Ivp1Frq = _Ne843Ivp1Frq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 8),
    _Ne843Ivp1Frq_Type()
)
ne843Ivp1Frq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Frq.setStatus("current")
_Ne843Ivp1Lst_Type = Integer32
_Ne843Ivp1Lst_Object = MibScalar
ne843Ivp1Lst = _Ne843Ivp1Lst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 9),
    _Ne843Ivp1Lst_Type()
)
ne843Ivp1Lst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Lst.setStatus("current")


class _Ne843Ivp1Ste_Type(Integer32):
    """Custom type ne843Ivp1Ste based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Ste_Type.__name__ = "Integer32"
_Ne843Ivp1Ste_Object = MibScalar
ne843Ivp1Ste = _Ne843Ivp1Ste_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 10),
    _Ne843Ivp1Ste_Type()
)
ne843Ivp1Ste.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Ste.setStatus("current")


class _Ne843Ivp1Rlse_Type(Integer32):
    """Custom type ne843Ivp1Rlse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Rlse_Type.__name__ = "Integer32"
_Ne843Ivp1Rlse_Object = MibScalar
ne843Ivp1Rlse = _Ne843Ivp1Rlse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 11),
    _Ne843Ivp1Rlse_Type()
)
ne843Ivp1Rlse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Rlse.setStatus("current")


class _Ne843Ivp1Dth_Type(Integer32):
    """Custom type ne843Ivp1Dth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 25),
        ValueRangeConstraint(40, 50),
    )


_Ne843Ivp1Dth_Type.__name__ = "Integer32"
_Ne843Ivp1Dth_Object = MibScalar
ne843Ivp1Dth = _Ne843Ivp1Dth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 12),
    _Ne843Ivp1Dth_Type()
)
ne843Ivp1Dth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Dth.setStatus("current")


class _Ne843Ivp1Rth_Type(Integer32):
    """Custom type ne843Ivp1Rth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 27),
        ValueRangeConstraint(44, 54),
    )


_Ne843Ivp1Rth_Type.__name__ = "Integer32"
_Ne843Ivp1Rth_Object = MibScalar
ne843Ivp1Rth = _Ne843Ivp1Rth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 13),
    _Ne843Ivp1Rth_Type()
)
ne843Ivp1Rth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Rth.setStatus("current")


class _Ne843Ivp1Lvd_Type(Integer32):
    """Custom type ne843Ivp1Lvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Lvd_Type.__name__ = "Integer32"
_Ne843Ivp1Lvd_Object = MibScalar
ne843Ivp1Lvd = _Ne843Ivp1Lvd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 14),
    _Ne843Ivp1Lvd_Type()
)
ne843Ivp1Lvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Lvd.setStatus("current")


class _Ne843Ivp1Hce_Type(Integer32):
    """Custom type ne843Ivp1Hce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Hce_Type.__name__ = "Integer32"
_Ne843Ivp1Hce_Object = MibScalar
ne843Ivp1Hce = _Ne843Ivp1Hce_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 15),
    _Ne843Ivp1Hce_Type()
)
ne843Ivp1Hce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Hce.setStatus("current")


class _Ne843Ivp1Hipe_Type(Integer32):
    """Custom type ne843Ivp1Hipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Hipe_Type.__name__ = "Integer32"
_Ne843Ivp1Hipe_Object = MibScalar
ne843Ivp1Hipe = _Ne843Ivp1Hipe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 16),
    _Ne843Ivp1Hipe_Type()
)
ne843Ivp1Hipe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Hipe.setStatus("current")


class _Ne843Ivp1Hrme_Type(Integer32):
    """Custom type ne843Ivp1Hrme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Ivp1Hrme_Type.__name__ = "Integer32"
_Ne843Ivp1Hrme_Object = MibScalar
ne843Ivp1Hrme = _Ne843Ivp1Hrme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 17),
    _Ne843Ivp1Hrme_Type()
)
ne843Ivp1Hrme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Ivp1Hrme.setStatus("current")
_Ne843Ivp1Ilvi_Type = DisplayString
_Ne843Ivp1Ilvi_Object = MibScalar
ne843Ivp1Ilvi = _Ne843Ivp1Ilvi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 18),
    _Ne843Ivp1Ilvi_Type()
)
ne843Ivp1Ilvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ilvi.setStatus("current")
_Ne843Ivp1Ihvi_Type = DisplayString
_Ne843Ivp1Ihvi_Object = MibScalar
ne843Ivp1Ihvi = _Ne843Ivp1Ihvi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 19),
    _Ne843Ivp1Ihvi_Type()
)
ne843Ivp1Ihvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ihvi.setStatus("current")
_Ne843Ivp1Ita_Type = DisplayString
_Ne843Ivp1Ita_Object = MibScalar
ne843Ivp1Ita = _Ne843Ivp1Ita_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 20),
    _Ne843Ivp1Ita_Type()
)
ne843Ivp1Ita.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ita.setStatus("current")
_Ne843Ivp1If_Type = DisplayString
_Ne843Ivp1If_Object = MibScalar
ne843Ivp1If = _Ne843Ivp1If_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 21),
    _Ne843Ivp1If_Type()
)
ne843Ivp1If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1If.setStatus("current")
_Ne843Ivp1Ilv_Type = DisplayString
_Ne843Ivp1Ilv_Object = MibScalar
ne843Ivp1Ilv = _Ne843Ivp1Ilv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 22),
    _Ne843Ivp1Ilv_Type()
)
ne843Ivp1Ilv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ilv.setStatus("current")
_Ne843Ivp1Ifa_Type = DisplayString
_Ne843Ivp1Ifa_Object = MibScalar
ne843Ivp1Ifa = _Ne843Ivp1Ifa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 23),
    _Ne843Ivp1Ifa_Type()
)
ne843Ivp1Ifa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ifa.setStatus("current")
_Ne843Ivp1Ihv_Type = DisplayString
_Ne843Ivp1Ihv_Object = MibScalar
ne843Ivp1Ihv = _Ne843Ivp1Ihv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 24),
    _Ne843Ivp1Ihv_Type()
)
ne843Ivp1Ihv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ihv.setStatus("current")
_Ne843Ivp1Ida_Type = DisplayString
_Ne843Ivp1Ida_Object = MibScalar
ne843Ivp1Ida = _Ne843Ivp1Ida_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 25),
    _Ne843Ivp1Ida_Type()
)
ne843Ivp1Ida.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Ida.setStatus("current")
_Ne843Ivp1Iof_Type = DisplayString
_Ne843Ivp1Iof_Object = MibScalar
ne843Ivp1Iof = _Ne843Ivp1Iof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 26),
    _Ne843Ivp1Iof_Type()
)
ne843Ivp1Iof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Iof.setStatus("current")
_Ne843Ivp1Idid_Type = DisplayString
_Ne843Ivp1Idid_Object = MibScalar
ne843Ivp1Idid = _Ne843Ivp1Idid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 27),
    _Ne843Ivp1Idid_Type()
)
ne843Ivp1Idid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Idid.setStatus("current")
_Ne843Ivp1Iirm_Type = DisplayString
_Ne843Ivp1Iirm_Object = MibScalar
ne843Ivp1Iirm = _Ne843Ivp1Iirm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 28),
    _Ne843Ivp1Iirm_Type()
)
ne843Ivp1Iirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Iirm.setStatus("current")
_Ne843Ivp1Iipk_Type = DisplayString
_Ne843Ivp1Iipk_Object = MibScalar
ne843Ivp1Iipk = _Ne843Ivp1Iipk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 29),
    _Ne843Ivp1Iipk_Type()
)
ne843Ivp1Iipk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Iipk.setStatus("current")
_Ne843Ivp1Icf_Type = DisplayString
_Ne843Ivp1Icf_Object = MibScalar
ne843Ivp1Icf = _Ne843Ivp1Icf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 30),
    _Ne843Ivp1Icf_Type()
)
ne843Ivp1Icf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Icf.setStatus("current")
_Ne843Ivp1Mif_Type = DisplayString
_Ne843Ivp1Mif_Object = MibScalar
ne843Ivp1Mif = _Ne843Ivp1Mif_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 31),
    _Ne843Ivp1Mif_Type()
)
ne843Ivp1Mif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Mif.setStatus("current")
_Ne843Ivp1Irls_Type = DisplayString
_Ne843Ivp1Irls_Object = MibScalar
ne843Ivp1Irls = _Ne843Ivp1Irls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 32),
    _Ne843Ivp1Irls_Type()
)
ne843Ivp1Irls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Irls.setStatus("current")
_Ne843Ivp1Milv_Type = DisplayString
_Ne843Ivp1Milv_Object = MibScalar
ne843Ivp1Milv = _Ne843Ivp1Milv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 42, 33),
    _Ne843Ivp1Milv_Type()
)
ne843Ivp1Milv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Ivp1Milv.setStatus("current")
_Ne843InvTable_Object = MibTable
ne843InvTable = _Ne843InvTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43)
)
if mibBuilder.loadTexts:
    ne843InvTable.setStatus("current")
_Ne843InvEntry_Object = MibTableRow
ne843InvEntry = _Ne843InvEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1)
)
ne843InvEntry.setIndexNames(
    (0, "NE843-MIB", "ne843InvEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843InvEntry.setStatus("current")


class _Ne843InvEntryIndex_Type(Integer32):
    """Custom type ne843InvEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843InvEntryIndex_Type.__name__ = "Integer32"
_Ne843InvEntryIndex_Object = MibTableColumn
ne843InvEntryIndex = _Ne843InvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 1),
    _Ne843InvEntryIndex_Type()
)
ne843InvEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIndex.setStatus("current")
_Ne843InvEntryIde_Type = DisplayString
_Ne843InvEntryIde_Object = MibTableColumn
ne843InvEntryIde = _Ne843InvEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 2),
    _Ne843InvEntryIde_Type()
)
ne843InvEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIde.setStatus("current")
_Ne843InvEntryDes_Type = DisplayString
_Ne843InvEntryDes_Object = MibTableColumn
ne843InvEntryDes = _Ne843InvEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 3),
    _Ne843InvEntryDes_Type()
)
ne843InvEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InvEntryDes.setStatus("current")
_Ne843InvEntryTyp_Type = DisplayString
_Ne843InvEntryTyp_Object = MibTableColumn
ne843InvEntryTyp = _Ne843InvEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 4),
    _Ne843InvEntryTyp_Type()
)
ne843InvEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InvEntryTyp.setStatus("current")
_Ne843InvEntrySn_Type = DisplayString
_Ne843InvEntrySn_Object = MibTableColumn
ne843InvEntrySn = _Ne843InvEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 5),
    _Ne843InvEntrySn_Type()
)
ne843InvEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntrySn.setStatus("current")
_Ne843InvEntryAdc_Type = Integer32
_Ne843InvEntryAdc_Object = MibTableColumn
ne843InvEntryAdc = _Ne843InvEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 6),
    _Ne843InvEntryAdc_Type()
)
ne843InvEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843InvEntryAdc.setUnits("Amps")
_Ne843InvEntryVdc_Type = Integer32
_Ne843InvEntryVdc_Object = MibTableColumn
ne843InvEntryVdc = _Ne843InvEntryVdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 7),
    _Ne843InvEntryVdc_Type()
)
ne843InvEntryVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryVdc.setStatus("current")
_Ne843InvEntryVac_Type = Integer32
_Ne843InvEntryVac_Object = MibTableColumn
ne843InvEntryVac = _Ne843InvEntryVac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 8),
    _Ne843InvEntryVac_Type()
)
ne843InvEntryVac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryVac.setStatus("current")
if mibBuilder.loadTexts:
    ne843InvEntryVac.setUnits("Volts")
_Ne843InvEntryStt_Type = DisplayString
_Ne843InvEntryStt_Object = MibTableColumn
ne843InvEntryStt = _Ne843InvEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 9),
    _Ne843InvEntryStt_Type()
)
ne843InvEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InvEntryStt.setStatus("current")
_Ne843InvEntryCap_Type = Integer32
_Ne843InvEntryCap_Object = MibTableColumn
ne843InvEntryCap = _Ne843InvEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 10),
    _Ne843InvEntryCap_Type()
)
ne843InvEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    ne843InvEntryCap.setUnits("Amps")
_Ne843InvEntryCva_Type = Integer32
_Ne843InvEntryCva_Object = MibTableColumn
ne843InvEntryCva = _Ne843InvEntryCva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 11),
    _Ne843InvEntryCva_Type()
)
ne843InvEntryCva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryCva.setStatus("current")
_Ne843InvEntryIpk_Type = Integer32
_Ne843InvEntryIpk_Object = MibTableColumn
ne843InvEntryIpk = _Ne843InvEntryIpk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 12),
    _Ne843InvEntryIpk_Type()
)
ne843InvEntryIpk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIpk.setStatus("current")
_Ne843InvEntryIrm_Type = Integer32
_Ne843InvEntryIrm_Object = MibTableColumn
ne843InvEntryIrm = _Ne843InvEntryIrm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 13),
    _Ne843InvEntryIrm_Type()
)
ne843InvEntryIrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIrm.setStatus("current")
_Ne843InvEntryFrq_Type = Integer32
_Ne843InvEntryFrq_Object = MibTableColumn
ne843InvEntryFrq = _Ne843InvEntryFrq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 14),
    _Ne843InvEntryFrq_Type()
)
ne843InvEntryFrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryFrq.setStatus("current")
_Ne843InvEntryCf_Type = Integer32
_Ne843InvEntryCf_Object = MibTableColumn
ne843InvEntryCf = _Ne843InvEntryCf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 15),
    _Ne843InvEntryCf_Type()
)
ne843InvEntryCf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryCf.setStatus("current")
_Ne843InvEntryPwr_Type = Integer32
_Ne843InvEntryPwr_Object = MibTableColumn
ne843InvEntryPwr = _Ne843InvEntryPwr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 16),
    _Ne843InvEntryPwr_Type()
)
ne843InvEntryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryPwr.setStatus("current")
_Ne843InvEntryVnom_Type = Integer32
_Ne843InvEntryVnom_Object = MibTableColumn
ne843InvEntryVnom = _Ne843InvEntryVnom_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 17),
    _Ne843InvEntryVnom_Type()
)
ne843InvEntryVnom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryVnom.setStatus("current")


class _Ne843InvEntryNcl_Type(Integer32):
    """Custom type ne843InvEntryNcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843InvEntryNcl_Type.__name__ = "Integer32"
_Ne843InvEntryNcl_Object = MibTableColumn
ne843InvEntryNcl = _Ne843InvEntryNcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 18),
    _Ne843InvEntryNcl_Type()
)
ne843InvEntryNcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843InvEntryNcl.setStatus("current")
if mibBuilder.loadTexts:
    ne843InvEntryNcl.setUnits("for LVD")
_Ne843InvEntryIlvi_Type = DisplayString
_Ne843InvEntryIlvi_Object = MibTableColumn
ne843InvEntryIlvi = _Ne843InvEntryIlvi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 19),
    _Ne843InvEntryIlvi_Type()
)
ne843InvEntryIlvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIlvi.setStatus("current")
_Ne843InvEntryIta_Type = DisplayString
_Ne843InvEntryIta_Object = MibTableColumn
ne843InvEntryIta = _Ne843InvEntryIta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 20),
    _Ne843InvEntryIta_Type()
)
ne843InvEntryIta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIta.setStatus("current")
_Ne843InvEntryIf_Type = DisplayString
_Ne843InvEntryIf_Object = MibTableColumn
ne843InvEntryIf = _Ne843InvEntryIf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 21),
    _Ne843InvEntryIf_Type()
)
ne843InvEntryIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIf.setStatus("current")
_Ne843InvEntryIlv_Type = DisplayString
_Ne843InvEntryIlv_Object = MibTableColumn
ne843InvEntryIlv = _Ne843InvEntryIlv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 22),
    _Ne843InvEntryIlv_Type()
)
ne843InvEntryIlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIlv.setStatus("current")
_Ne843InvEntryIfa_Type = DisplayString
_Ne843InvEntryIfa_Object = MibTableColumn
ne843InvEntryIfa = _Ne843InvEntryIfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 23),
    _Ne843InvEntryIfa_Type()
)
ne843InvEntryIfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIfa.setStatus("current")
_Ne843InvEntryDid_Type = DisplayString
_Ne843InvEntryDid_Object = MibTableColumn
ne843InvEntryDid = _Ne843InvEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 24),
    _Ne843InvEntryDid_Type()
)
ne843InvEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryDid.setStatus("current")
_Ne843InvEntryIcmf_Type = DisplayString
_Ne843InvEntryIcmf_Object = MibTableColumn
ne843InvEntryIcmf = _Ne843InvEntryIcmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 25),
    _Ne843InvEntryIcmf_Type()
)
ne843InvEntryIcmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIcmf.setStatus("current")
_Ne843InvEntryIcf_Type = DisplayString
_Ne843InvEntryIcf_Object = MibTableColumn
ne843InvEntryIcf = _Ne843InvEntryIcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 26),
    _Ne843InvEntryIcf_Type()
)
ne843InvEntryIcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIcf.setStatus("current")
_Ne843InvEntryIda_Type = DisplayString
_Ne843InvEntryIda_Object = MibTableColumn
ne843InvEntryIda = _Ne843InvEntryIda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 27),
    _Ne843InvEntryIda_Type()
)
ne843InvEntryIda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIda.setStatus("current")
_Ne843InvEntryIhv_Type = DisplayString
_Ne843InvEntryIhv_Object = MibTableColumn
ne843InvEntryIhv = _Ne843InvEntryIhv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 28),
    _Ne843InvEntryIhv_Type()
)
ne843InvEntryIhv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIhv.setStatus("current")
_Ne843InvEntryIhvi_Type = DisplayString
_Ne843InvEntryIhvi_Object = MibTableColumn
ne843InvEntryIhvi = _Ne843InvEntryIhvi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 29),
    _Ne843InvEntryIhvi_Type()
)
ne843InvEntryIhvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIhvi.setStatus("current")
_Ne843InvEntryIipk_Type = DisplayString
_Ne843InvEntryIipk_Object = MibTableColumn
ne843InvEntryIipk = _Ne843InvEntryIipk_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 30),
    _Ne843InvEntryIipk_Type()
)
ne843InvEntryIipk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIipk.setStatus("current")
_Ne843InvEntryIirm_Type = DisplayString
_Ne843InvEntryIirm_Object = MibTableColumn
ne843InvEntryIirm = _Ne843InvEntryIirm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 31),
    _Ne843InvEntryIirm_Type()
)
ne843InvEntryIirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIirm.setStatus("current")
_Ne843InvEntryIof_Type = DisplayString
_Ne843InvEntryIof_Object = MibTableColumn
ne843InvEntryIof = _Ne843InvEntryIof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 32),
    _Ne843InvEntryIof_Type()
)
ne843InvEntryIof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIof.setStatus("current")


class _Ne843InvEntryIlvi1_Type(Integer32):
    """Custom type ne843InvEntryIlvi1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIlvi1_Type.__name__ = "Integer32"
_Ne843InvEntryIlvi1_Object = MibTableColumn
ne843InvEntryIlvi1 = _Ne843InvEntryIlvi1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 33),
    _Ne843InvEntryIlvi1_Type()
)
ne843InvEntryIlvi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIlvi1.setStatus("current")


class _Ne843InvEntryIta1_Type(Integer32):
    """Custom type ne843InvEntryIta1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIta1_Type.__name__ = "Integer32"
_Ne843InvEntryIta1_Object = MibTableColumn
ne843InvEntryIta1 = _Ne843InvEntryIta1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 34),
    _Ne843InvEntryIta1_Type()
)
ne843InvEntryIta1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIta1.setStatus("current")


class _Ne843InvEntryIf1_Type(Integer32):
    """Custom type ne843InvEntryIf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIf1_Type.__name__ = "Integer32"
_Ne843InvEntryIf1_Object = MibTableColumn
ne843InvEntryIf1 = _Ne843InvEntryIf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 35),
    _Ne843InvEntryIf1_Type()
)
ne843InvEntryIf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIf1.setStatus("current")


class _Ne843InvEntryIlv1_Type(Integer32):
    """Custom type ne843InvEntryIlv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIlv1_Type.__name__ = "Integer32"
_Ne843InvEntryIlv1_Object = MibTableColumn
ne843InvEntryIlv1 = _Ne843InvEntryIlv1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 36),
    _Ne843InvEntryIlv1_Type()
)
ne843InvEntryIlv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIlv1.setStatus("current")


class _Ne843InvEntryIfa1_Type(Integer32):
    """Custom type ne843InvEntryIfa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIfa1_Type.__name__ = "Integer32"
_Ne843InvEntryIfa1_Object = MibTableColumn
ne843InvEntryIfa1 = _Ne843InvEntryIfa1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 37),
    _Ne843InvEntryIfa1_Type()
)
ne843InvEntryIfa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIfa1.setStatus("current")


class _Ne843InvEntryDid1_Type(Integer32):
    """Custom type ne843InvEntryDid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryDid1_Type.__name__ = "Integer32"
_Ne843InvEntryDid1_Object = MibTableColumn
ne843InvEntryDid1 = _Ne843InvEntryDid1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 38),
    _Ne843InvEntryDid1_Type()
)
ne843InvEntryDid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryDid1.setStatus("current")


class _Ne843InvEntryIcmf1_Type(Integer32):
    """Custom type ne843InvEntryIcmf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIcmf1_Type.__name__ = "Integer32"
_Ne843InvEntryIcmf1_Object = MibTableColumn
ne843InvEntryIcmf1 = _Ne843InvEntryIcmf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 39),
    _Ne843InvEntryIcmf1_Type()
)
ne843InvEntryIcmf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIcmf1.setStatus("current")


class _Ne843InvEntryIcf1_Type(Integer32):
    """Custom type ne843InvEntryIcf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIcf1_Type.__name__ = "Integer32"
_Ne843InvEntryIcf1_Object = MibTableColumn
ne843InvEntryIcf1 = _Ne843InvEntryIcf1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 40),
    _Ne843InvEntryIcf1_Type()
)
ne843InvEntryIcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIcf1.setStatus("current")


class _Ne843InvEntryIda1_Type(Integer32):
    """Custom type ne843InvEntryIda1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIda1_Type.__name__ = "Integer32"
_Ne843InvEntryIda1_Object = MibTableColumn
ne843InvEntryIda1 = _Ne843InvEntryIda1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 41),
    _Ne843InvEntryIda1_Type()
)
ne843InvEntryIda1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIda1.setStatus("current")


class _Ne843InvEntryIhv1_Type(Integer32):
    """Custom type ne843InvEntryIhv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIhv1_Type.__name__ = "Integer32"
_Ne843InvEntryIhv1_Object = MibTableColumn
ne843InvEntryIhv1 = _Ne843InvEntryIhv1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 42),
    _Ne843InvEntryIhv1_Type()
)
ne843InvEntryIhv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIhv1.setStatus("current")


class _Ne843InvEntryIhvi1_Type(Integer32):
    """Custom type ne843InvEntryIhvi1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIhvi1_Type.__name__ = "Integer32"
_Ne843InvEntryIhvi1_Object = MibTableColumn
ne843InvEntryIhvi1 = _Ne843InvEntryIhvi1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 43),
    _Ne843InvEntryIhvi1_Type()
)
ne843InvEntryIhvi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIhvi1.setStatus("current")


class _Ne843InvEntryIipk1_Type(Integer32):
    """Custom type ne843InvEntryIipk1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIipk1_Type.__name__ = "Integer32"
_Ne843InvEntryIipk1_Object = MibTableColumn
ne843InvEntryIipk1 = _Ne843InvEntryIipk1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 44),
    _Ne843InvEntryIipk1_Type()
)
ne843InvEntryIipk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIipk1.setStatus("current")


class _Ne843InvEntryIirm1_Type(Integer32):
    """Custom type ne843InvEntryIirm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIirm1_Type.__name__ = "Integer32"
_Ne843InvEntryIirm1_Object = MibTableColumn
ne843InvEntryIirm1 = _Ne843InvEntryIirm1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 45),
    _Ne843InvEntryIirm1_Type()
)
ne843InvEntryIirm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIirm1.setStatus("current")


class _Ne843InvEntryIof1_Type(Integer32):
    """Custom type ne843InvEntryIof1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Ne843InvEntryIof1_Type.__name__ = "Integer32"
_Ne843InvEntryIof1_Object = MibTableColumn
ne843InvEntryIof1 = _Ne843InvEntryIof1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 43, 1, 46),
    _Ne843InvEntryIof1_Type()
)
ne843InvEntryIof1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843InvEntryIof1.setStatus("current")
_Ne843Rpt1_ObjectIdentity = ObjectIdentity
ne843Rpt1 = _Ne843Rpt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44)
)
_Ne843Rpt1Ide_Type = DisplayString
_Ne843Rpt1Ide_Object = MibScalar
ne843Rpt1Ide = _Ne843Rpt1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 1),
    _Ne843Rpt1Ide_Type()
)
ne843Rpt1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843Rpt1Ide.setStatus("current")
_Ne843Rpt1Des_Type = DisplayString
_Ne843Rpt1Des_Object = MibScalar
ne843Rpt1Des = _Ne843Rpt1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 2),
    _Ne843Rpt1Des_Type()
)
ne843Rpt1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1Des.setStatus("current")


class _Ne843Rpt1Ena_Type(Integer32):
    """Custom type ne843Rpt1Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843Rpt1Ena_Type.__name__ = "Integer32"
_Ne843Rpt1Ena_Object = MibScalar
ne843Rpt1Ena = _Ne843Rpt1Ena_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 3),
    _Ne843Rpt1Ena_Type()
)
ne843Rpt1Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1Ena.setStatus("current")


class _Ne843Rpt1Int_Type(Integer32):
    """Custom type ne843Rpt1Int based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Ne843Rpt1Int_Type.__name__ = "Integer32"
_Ne843Rpt1Int_Object = MibScalar
ne843Rpt1Int = _Ne843Rpt1Int_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 4),
    _Ne843Rpt1Int_Type()
)
ne843Rpt1Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1Int.setStatus("current")
if mibBuilder.loadTexts:
    ne843Rpt1Int.setUnits("minutes")
_Ne843Rpt1D001_Type = DisplayString
_Ne843Rpt1D001_Object = MibScalar
ne843Rpt1D001 = _Ne843Rpt1D001_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 5),
    _Ne843Rpt1D001_Type()
)
ne843Rpt1D001.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D001.setStatus("current")
_Ne843Rpt1D002_Type = DisplayString
_Ne843Rpt1D002_Object = MibScalar
ne843Rpt1D002 = _Ne843Rpt1D002_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 6),
    _Ne843Rpt1D002_Type()
)
ne843Rpt1D002.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D002.setStatus("current")
_Ne843Rpt1D003_Type = DisplayString
_Ne843Rpt1D003_Object = MibScalar
ne843Rpt1D003 = _Ne843Rpt1D003_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 7),
    _Ne843Rpt1D003_Type()
)
ne843Rpt1D003.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D003.setStatus("current")
_Ne843Rpt1D004_Type = DisplayString
_Ne843Rpt1D004_Object = MibScalar
ne843Rpt1D004 = _Ne843Rpt1D004_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 8),
    _Ne843Rpt1D004_Type()
)
ne843Rpt1D004.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D004.setStatus("current")
_Ne843Rpt1D005_Type = DisplayString
_Ne843Rpt1D005_Object = MibScalar
ne843Rpt1D005 = _Ne843Rpt1D005_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 9),
    _Ne843Rpt1D005_Type()
)
ne843Rpt1D005.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D005.setStatus("current")
_Ne843Rpt1D006_Type = DisplayString
_Ne843Rpt1D006_Object = MibScalar
ne843Rpt1D006 = _Ne843Rpt1D006_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 10),
    _Ne843Rpt1D006_Type()
)
ne843Rpt1D006.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D006.setStatus("current")
_Ne843Rpt1D007_Type = DisplayString
_Ne843Rpt1D007_Object = MibScalar
ne843Rpt1D007 = _Ne843Rpt1D007_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 11),
    _Ne843Rpt1D007_Type()
)
ne843Rpt1D007.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D007.setStatus("current")
_Ne843Rpt1D008_Type = DisplayString
_Ne843Rpt1D008_Object = MibScalar
ne843Rpt1D008 = _Ne843Rpt1D008_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 12),
    _Ne843Rpt1D008_Type()
)
ne843Rpt1D008.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D008.setStatus("current")
_Ne843Rpt1D009_Type = DisplayString
_Ne843Rpt1D009_Object = MibScalar
ne843Rpt1D009 = _Ne843Rpt1D009_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 13),
    _Ne843Rpt1D009_Type()
)
ne843Rpt1D009.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D009.setStatus("current")
_Ne843Rpt1D010_Type = DisplayString
_Ne843Rpt1D010_Object = MibScalar
ne843Rpt1D010 = _Ne843Rpt1D010_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 14),
    _Ne843Rpt1D010_Type()
)
ne843Rpt1D010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D010.setStatus("current")
_Ne843Rpt1D011_Type = DisplayString
_Ne843Rpt1D011_Object = MibScalar
ne843Rpt1D011 = _Ne843Rpt1D011_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 15),
    _Ne843Rpt1D011_Type()
)
ne843Rpt1D011.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D011.setStatus("current")
_Ne843Rpt1D012_Type = DisplayString
_Ne843Rpt1D012_Object = MibScalar
ne843Rpt1D012 = _Ne843Rpt1D012_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 16),
    _Ne843Rpt1D012_Type()
)
ne843Rpt1D012.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D012.setStatus("current")
_Ne843Rpt1D013_Type = DisplayString
_Ne843Rpt1D013_Object = MibScalar
ne843Rpt1D013 = _Ne843Rpt1D013_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 17),
    _Ne843Rpt1D013_Type()
)
ne843Rpt1D013.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D013.setStatus("current")
_Ne843Rpt1D014_Type = DisplayString
_Ne843Rpt1D014_Object = MibScalar
ne843Rpt1D014 = _Ne843Rpt1D014_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 18),
    _Ne843Rpt1D014_Type()
)
ne843Rpt1D014.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D014.setStatus("current")
_Ne843Rpt1D015_Type = DisplayString
_Ne843Rpt1D015_Object = MibScalar
ne843Rpt1D015 = _Ne843Rpt1D015_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 19),
    _Ne843Rpt1D015_Type()
)
ne843Rpt1D015.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D015.setStatus("current")
_Ne843Rpt1D016_Type = DisplayString
_Ne843Rpt1D016_Object = MibScalar
ne843Rpt1D016 = _Ne843Rpt1D016_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 20),
    _Ne843Rpt1D016_Type()
)
ne843Rpt1D016.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D016.setStatus("current")
_Ne843Rpt1D017_Type = DisplayString
_Ne843Rpt1D017_Object = MibScalar
ne843Rpt1D017 = _Ne843Rpt1D017_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 21),
    _Ne843Rpt1D017_Type()
)
ne843Rpt1D017.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D017.setStatus("current")
_Ne843Rpt1D018_Type = DisplayString
_Ne843Rpt1D018_Object = MibScalar
ne843Rpt1D018 = _Ne843Rpt1D018_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 22),
    _Ne843Rpt1D018_Type()
)
ne843Rpt1D018.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D018.setStatus("current")
_Ne843Rpt1D019_Type = DisplayString
_Ne843Rpt1D019_Object = MibScalar
ne843Rpt1D019 = _Ne843Rpt1D019_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 23),
    _Ne843Rpt1D019_Type()
)
ne843Rpt1D019.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D019.setStatus("current")
_Ne843Rpt1D020_Type = DisplayString
_Ne843Rpt1D020_Object = MibScalar
ne843Rpt1D020 = _Ne843Rpt1D020_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 24),
    _Ne843Rpt1D020_Type()
)
ne843Rpt1D020.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D020.setStatus("current")
_Ne843Rpt1D021_Type = DisplayString
_Ne843Rpt1D021_Object = MibScalar
ne843Rpt1D021 = _Ne843Rpt1D021_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 25),
    _Ne843Rpt1D021_Type()
)
ne843Rpt1D021.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D021.setStatus("current")
_Ne843Rpt1D022_Type = DisplayString
_Ne843Rpt1D022_Object = MibScalar
ne843Rpt1D022 = _Ne843Rpt1D022_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 26),
    _Ne843Rpt1D022_Type()
)
ne843Rpt1D022.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D022.setStatus("current")
_Ne843Rpt1D023_Type = DisplayString
_Ne843Rpt1D023_Object = MibScalar
ne843Rpt1D023 = _Ne843Rpt1D023_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 27),
    _Ne843Rpt1D023_Type()
)
ne843Rpt1D023.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D023.setStatus("current")
_Ne843Rpt1D024_Type = DisplayString
_Ne843Rpt1D024_Object = MibScalar
ne843Rpt1D024 = _Ne843Rpt1D024_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 28),
    _Ne843Rpt1D024_Type()
)
ne843Rpt1D024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D024.setStatus("current")
_Ne843Rpt1D025_Type = DisplayString
_Ne843Rpt1D025_Object = MibScalar
ne843Rpt1D025 = _Ne843Rpt1D025_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 29),
    _Ne843Rpt1D025_Type()
)
ne843Rpt1D025.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D025.setStatus("current")
_Ne843Rpt1D026_Type = DisplayString
_Ne843Rpt1D026_Object = MibScalar
ne843Rpt1D026 = _Ne843Rpt1D026_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 30),
    _Ne843Rpt1D026_Type()
)
ne843Rpt1D026.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D026.setStatus("current")
_Ne843Rpt1D027_Type = DisplayString
_Ne843Rpt1D027_Object = MibScalar
ne843Rpt1D027 = _Ne843Rpt1D027_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 31),
    _Ne843Rpt1D027_Type()
)
ne843Rpt1D027.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D027.setStatus("current")
_Ne843Rpt1D028_Type = DisplayString
_Ne843Rpt1D028_Object = MibScalar
ne843Rpt1D028 = _Ne843Rpt1D028_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 32),
    _Ne843Rpt1D028_Type()
)
ne843Rpt1D028.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D028.setStatus("current")
_Ne843Rpt1D029_Type = DisplayString
_Ne843Rpt1D029_Object = MibScalar
ne843Rpt1D029 = _Ne843Rpt1D029_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 33),
    _Ne843Rpt1D029_Type()
)
ne843Rpt1D029.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D029.setStatus("current")
_Ne843Rpt1D030_Type = DisplayString
_Ne843Rpt1D030_Object = MibScalar
ne843Rpt1D030 = _Ne843Rpt1D030_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 34),
    _Ne843Rpt1D030_Type()
)
ne843Rpt1D030.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D030.setStatus("current")
_Ne843Rpt1D031_Type = DisplayString
_Ne843Rpt1D031_Object = MibScalar
ne843Rpt1D031 = _Ne843Rpt1D031_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 35),
    _Ne843Rpt1D031_Type()
)
ne843Rpt1D031.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D031.setStatus("current")
_Ne843Rpt1D032_Type = DisplayString
_Ne843Rpt1D032_Object = MibScalar
ne843Rpt1D032 = _Ne843Rpt1D032_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 36),
    _Ne843Rpt1D032_Type()
)
ne843Rpt1D032.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D032.setStatus("current")
_Ne843Rpt1D033_Type = DisplayString
_Ne843Rpt1D033_Object = MibScalar
ne843Rpt1D033 = _Ne843Rpt1D033_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 37),
    _Ne843Rpt1D033_Type()
)
ne843Rpt1D033.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D033.setStatus("current")
_Ne843Rpt1D034_Type = DisplayString
_Ne843Rpt1D034_Object = MibScalar
ne843Rpt1D034 = _Ne843Rpt1D034_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 38),
    _Ne843Rpt1D034_Type()
)
ne843Rpt1D034.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D034.setStatus("current")
_Ne843Rpt1D035_Type = DisplayString
_Ne843Rpt1D035_Object = MibScalar
ne843Rpt1D035 = _Ne843Rpt1D035_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 39),
    _Ne843Rpt1D035_Type()
)
ne843Rpt1D035.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D035.setStatus("current")
_Ne843Rpt1D036_Type = DisplayString
_Ne843Rpt1D036_Object = MibScalar
ne843Rpt1D036 = _Ne843Rpt1D036_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 40),
    _Ne843Rpt1D036_Type()
)
ne843Rpt1D036.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D036.setStatus("current")
_Ne843Rpt1D037_Type = DisplayString
_Ne843Rpt1D037_Object = MibScalar
ne843Rpt1D037 = _Ne843Rpt1D037_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 41),
    _Ne843Rpt1D037_Type()
)
ne843Rpt1D037.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D037.setStatus("current")
_Ne843Rpt1D038_Type = DisplayString
_Ne843Rpt1D038_Object = MibScalar
ne843Rpt1D038 = _Ne843Rpt1D038_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 42),
    _Ne843Rpt1D038_Type()
)
ne843Rpt1D038.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D038.setStatus("current")
_Ne843Rpt1D039_Type = DisplayString
_Ne843Rpt1D039_Object = MibScalar
ne843Rpt1D039 = _Ne843Rpt1D039_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 43),
    _Ne843Rpt1D039_Type()
)
ne843Rpt1D039.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D039.setStatus("current")
_Ne843Rpt1D040_Type = DisplayString
_Ne843Rpt1D040_Object = MibScalar
ne843Rpt1D040 = _Ne843Rpt1D040_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 44),
    _Ne843Rpt1D040_Type()
)
ne843Rpt1D040.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D040.setStatus("current")
_Ne843Rpt1D041_Type = DisplayString
_Ne843Rpt1D041_Object = MibScalar
ne843Rpt1D041 = _Ne843Rpt1D041_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 45),
    _Ne843Rpt1D041_Type()
)
ne843Rpt1D041.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D041.setStatus("current")
_Ne843Rpt1D042_Type = DisplayString
_Ne843Rpt1D042_Object = MibScalar
ne843Rpt1D042 = _Ne843Rpt1D042_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 46),
    _Ne843Rpt1D042_Type()
)
ne843Rpt1D042.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D042.setStatus("current")
_Ne843Rpt1D043_Type = DisplayString
_Ne843Rpt1D043_Object = MibScalar
ne843Rpt1D043 = _Ne843Rpt1D043_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 47),
    _Ne843Rpt1D043_Type()
)
ne843Rpt1D043.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D043.setStatus("current")
_Ne843Rpt1D044_Type = DisplayString
_Ne843Rpt1D044_Object = MibScalar
ne843Rpt1D044 = _Ne843Rpt1D044_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 48),
    _Ne843Rpt1D044_Type()
)
ne843Rpt1D044.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D044.setStatus("current")
_Ne843Rpt1D045_Type = DisplayString
_Ne843Rpt1D045_Object = MibScalar
ne843Rpt1D045 = _Ne843Rpt1D045_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 49),
    _Ne843Rpt1D045_Type()
)
ne843Rpt1D045.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D045.setStatus("current")
_Ne843Rpt1D046_Type = DisplayString
_Ne843Rpt1D046_Object = MibScalar
ne843Rpt1D046 = _Ne843Rpt1D046_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 50),
    _Ne843Rpt1D046_Type()
)
ne843Rpt1D046.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D046.setStatus("current")
_Ne843Rpt1D047_Type = DisplayString
_Ne843Rpt1D047_Object = MibScalar
ne843Rpt1D047 = _Ne843Rpt1D047_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 51),
    _Ne843Rpt1D047_Type()
)
ne843Rpt1D047.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D047.setStatus("current")
_Ne843Rpt1D048_Type = DisplayString
_Ne843Rpt1D048_Object = MibScalar
ne843Rpt1D048 = _Ne843Rpt1D048_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 52),
    _Ne843Rpt1D048_Type()
)
ne843Rpt1D048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D048.setStatus("current")
_Ne843Rpt1D049_Type = DisplayString
_Ne843Rpt1D049_Object = MibScalar
ne843Rpt1D049 = _Ne843Rpt1D049_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 53),
    _Ne843Rpt1D049_Type()
)
ne843Rpt1D049.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D049.setStatus("current")
_Ne843Rpt1D050_Type = DisplayString
_Ne843Rpt1D050_Object = MibScalar
ne843Rpt1D050 = _Ne843Rpt1D050_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 54),
    _Ne843Rpt1D050_Type()
)
ne843Rpt1D050.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D050.setStatus("current")
_Ne843Rpt1D051_Type = DisplayString
_Ne843Rpt1D051_Object = MibScalar
ne843Rpt1D051 = _Ne843Rpt1D051_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 55),
    _Ne843Rpt1D051_Type()
)
ne843Rpt1D051.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D051.setStatus("current")
_Ne843Rpt1D052_Type = DisplayString
_Ne843Rpt1D052_Object = MibScalar
ne843Rpt1D052 = _Ne843Rpt1D052_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 56),
    _Ne843Rpt1D052_Type()
)
ne843Rpt1D052.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D052.setStatus("current")
_Ne843Rpt1D053_Type = DisplayString
_Ne843Rpt1D053_Object = MibScalar
ne843Rpt1D053 = _Ne843Rpt1D053_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 57),
    _Ne843Rpt1D053_Type()
)
ne843Rpt1D053.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D053.setStatus("current")
_Ne843Rpt1D054_Type = DisplayString
_Ne843Rpt1D054_Object = MibScalar
ne843Rpt1D054 = _Ne843Rpt1D054_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 58),
    _Ne843Rpt1D054_Type()
)
ne843Rpt1D054.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D054.setStatus("current")
_Ne843Rpt1D055_Type = DisplayString
_Ne843Rpt1D055_Object = MibScalar
ne843Rpt1D055 = _Ne843Rpt1D055_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 59),
    _Ne843Rpt1D055_Type()
)
ne843Rpt1D055.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D055.setStatus("current")
_Ne843Rpt1D056_Type = DisplayString
_Ne843Rpt1D056_Object = MibScalar
ne843Rpt1D056 = _Ne843Rpt1D056_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 60),
    _Ne843Rpt1D056_Type()
)
ne843Rpt1D056.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D056.setStatus("current")
_Ne843Rpt1D057_Type = DisplayString
_Ne843Rpt1D057_Object = MibScalar
ne843Rpt1D057 = _Ne843Rpt1D057_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 61),
    _Ne843Rpt1D057_Type()
)
ne843Rpt1D057.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D057.setStatus("current")
_Ne843Rpt1D058_Type = DisplayString
_Ne843Rpt1D058_Object = MibScalar
ne843Rpt1D058 = _Ne843Rpt1D058_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 62),
    _Ne843Rpt1D058_Type()
)
ne843Rpt1D058.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D058.setStatus("current")
_Ne843Rpt1D059_Type = DisplayString
_Ne843Rpt1D059_Object = MibScalar
ne843Rpt1D059 = _Ne843Rpt1D059_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 63),
    _Ne843Rpt1D059_Type()
)
ne843Rpt1D059.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D059.setStatus("current")
_Ne843Rpt1D060_Type = DisplayString
_Ne843Rpt1D060_Object = MibScalar
ne843Rpt1D060 = _Ne843Rpt1D060_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 64),
    _Ne843Rpt1D060_Type()
)
ne843Rpt1D060.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D060.setStatus("current")
_Ne843Rpt1D061_Type = DisplayString
_Ne843Rpt1D061_Object = MibScalar
ne843Rpt1D061 = _Ne843Rpt1D061_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 65),
    _Ne843Rpt1D061_Type()
)
ne843Rpt1D061.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D061.setStatus("current")
_Ne843Rpt1D062_Type = DisplayString
_Ne843Rpt1D062_Object = MibScalar
ne843Rpt1D062 = _Ne843Rpt1D062_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 66),
    _Ne843Rpt1D062_Type()
)
ne843Rpt1D062.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D062.setStatus("current")
_Ne843Rpt1D063_Type = DisplayString
_Ne843Rpt1D063_Object = MibScalar
ne843Rpt1D063 = _Ne843Rpt1D063_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 67),
    _Ne843Rpt1D063_Type()
)
ne843Rpt1D063.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D063.setStatus("current")
_Ne843Rpt1D064_Type = DisplayString
_Ne843Rpt1D064_Object = MibScalar
ne843Rpt1D064 = _Ne843Rpt1D064_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 68),
    _Ne843Rpt1D064_Type()
)
ne843Rpt1D064.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D064.setStatus("current")
_Ne843Rpt1D065_Type = DisplayString
_Ne843Rpt1D065_Object = MibScalar
ne843Rpt1D065 = _Ne843Rpt1D065_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 69),
    _Ne843Rpt1D065_Type()
)
ne843Rpt1D065.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D065.setStatus("current")
_Ne843Rpt1D066_Type = DisplayString
_Ne843Rpt1D066_Object = MibScalar
ne843Rpt1D066 = _Ne843Rpt1D066_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 70),
    _Ne843Rpt1D066_Type()
)
ne843Rpt1D066.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D066.setStatus("current")
_Ne843Rpt1D067_Type = DisplayString
_Ne843Rpt1D067_Object = MibScalar
ne843Rpt1D067 = _Ne843Rpt1D067_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 71),
    _Ne843Rpt1D067_Type()
)
ne843Rpt1D067.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D067.setStatus("current")
_Ne843Rpt1D068_Type = DisplayString
_Ne843Rpt1D068_Object = MibScalar
ne843Rpt1D068 = _Ne843Rpt1D068_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 72),
    _Ne843Rpt1D068_Type()
)
ne843Rpt1D068.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D068.setStatus("current")
_Ne843Rpt1D069_Type = DisplayString
_Ne843Rpt1D069_Object = MibScalar
ne843Rpt1D069 = _Ne843Rpt1D069_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 73),
    _Ne843Rpt1D069_Type()
)
ne843Rpt1D069.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D069.setStatus("current")
_Ne843Rpt1D070_Type = DisplayString
_Ne843Rpt1D070_Object = MibScalar
ne843Rpt1D070 = _Ne843Rpt1D070_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 74),
    _Ne843Rpt1D070_Type()
)
ne843Rpt1D070.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D070.setStatus("current")
_Ne843Rpt1D071_Type = DisplayString
_Ne843Rpt1D071_Object = MibScalar
ne843Rpt1D071 = _Ne843Rpt1D071_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 75),
    _Ne843Rpt1D071_Type()
)
ne843Rpt1D071.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D071.setStatus("current")
_Ne843Rpt1D072_Type = DisplayString
_Ne843Rpt1D072_Object = MibScalar
ne843Rpt1D072 = _Ne843Rpt1D072_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 76),
    _Ne843Rpt1D072_Type()
)
ne843Rpt1D072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D072.setStatus("current")
_Ne843Rpt1D073_Type = DisplayString
_Ne843Rpt1D073_Object = MibScalar
ne843Rpt1D073 = _Ne843Rpt1D073_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 77),
    _Ne843Rpt1D073_Type()
)
ne843Rpt1D073.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D073.setStatus("current")
_Ne843Rpt1D074_Type = DisplayString
_Ne843Rpt1D074_Object = MibScalar
ne843Rpt1D074 = _Ne843Rpt1D074_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 78),
    _Ne843Rpt1D074_Type()
)
ne843Rpt1D074.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D074.setStatus("current")
_Ne843Rpt1D075_Type = DisplayString
_Ne843Rpt1D075_Object = MibScalar
ne843Rpt1D075 = _Ne843Rpt1D075_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 79),
    _Ne843Rpt1D075_Type()
)
ne843Rpt1D075.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D075.setStatus("current")
_Ne843Rpt1D076_Type = DisplayString
_Ne843Rpt1D076_Object = MibScalar
ne843Rpt1D076 = _Ne843Rpt1D076_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 80),
    _Ne843Rpt1D076_Type()
)
ne843Rpt1D076.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D076.setStatus("current")
_Ne843Rpt1D077_Type = DisplayString
_Ne843Rpt1D077_Object = MibScalar
ne843Rpt1D077 = _Ne843Rpt1D077_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 81),
    _Ne843Rpt1D077_Type()
)
ne843Rpt1D077.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D077.setStatus("current")
_Ne843Rpt1D078_Type = DisplayString
_Ne843Rpt1D078_Object = MibScalar
ne843Rpt1D078 = _Ne843Rpt1D078_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 82),
    _Ne843Rpt1D078_Type()
)
ne843Rpt1D078.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D078.setStatus("current")
_Ne843Rpt1D079_Type = DisplayString
_Ne843Rpt1D079_Object = MibScalar
ne843Rpt1D079 = _Ne843Rpt1D079_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 83),
    _Ne843Rpt1D079_Type()
)
ne843Rpt1D079.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D079.setStatus("current")
_Ne843Rpt1D080_Type = DisplayString
_Ne843Rpt1D080_Object = MibScalar
ne843Rpt1D080 = _Ne843Rpt1D080_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 84),
    _Ne843Rpt1D080_Type()
)
ne843Rpt1D080.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D080.setStatus("current")
_Ne843Rpt1D081_Type = DisplayString
_Ne843Rpt1D081_Object = MibScalar
ne843Rpt1D081 = _Ne843Rpt1D081_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 85),
    _Ne843Rpt1D081_Type()
)
ne843Rpt1D081.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D081.setStatus("current")
_Ne843Rpt1D082_Type = DisplayString
_Ne843Rpt1D082_Object = MibScalar
ne843Rpt1D082 = _Ne843Rpt1D082_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 86),
    _Ne843Rpt1D082_Type()
)
ne843Rpt1D082.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D082.setStatus("current")
_Ne843Rpt1D083_Type = DisplayString
_Ne843Rpt1D083_Object = MibScalar
ne843Rpt1D083 = _Ne843Rpt1D083_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 87),
    _Ne843Rpt1D083_Type()
)
ne843Rpt1D083.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D083.setStatus("current")
_Ne843Rpt1D084_Type = DisplayString
_Ne843Rpt1D084_Object = MibScalar
ne843Rpt1D084 = _Ne843Rpt1D084_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 88),
    _Ne843Rpt1D084_Type()
)
ne843Rpt1D084.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D084.setStatus("current")
_Ne843Rpt1D085_Type = DisplayString
_Ne843Rpt1D085_Object = MibScalar
ne843Rpt1D085 = _Ne843Rpt1D085_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 89),
    _Ne843Rpt1D085_Type()
)
ne843Rpt1D085.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D085.setStatus("current")
_Ne843Rpt1D086_Type = DisplayString
_Ne843Rpt1D086_Object = MibScalar
ne843Rpt1D086 = _Ne843Rpt1D086_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 90),
    _Ne843Rpt1D086_Type()
)
ne843Rpt1D086.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D086.setStatus("current")
_Ne843Rpt1D087_Type = DisplayString
_Ne843Rpt1D087_Object = MibScalar
ne843Rpt1D087 = _Ne843Rpt1D087_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 91),
    _Ne843Rpt1D087_Type()
)
ne843Rpt1D087.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D087.setStatus("current")
_Ne843Rpt1D088_Type = DisplayString
_Ne843Rpt1D088_Object = MibScalar
ne843Rpt1D088 = _Ne843Rpt1D088_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 92),
    _Ne843Rpt1D088_Type()
)
ne843Rpt1D088.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D088.setStatus("current")
_Ne843Rpt1D089_Type = DisplayString
_Ne843Rpt1D089_Object = MibScalar
ne843Rpt1D089 = _Ne843Rpt1D089_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 93),
    _Ne843Rpt1D089_Type()
)
ne843Rpt1D089.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D089.setStatus("current")
_Ne843Rpt1D090_Type = DisplayString
_Ne843Rpt1D090_Object = MibScalar
ne843Rpt1D090 = _Ne843Rpt1D090_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 94),
    _Ne843Rpt1D090_Type()
)
ne843Rpt1D090.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D090.setStatus("current")
_Ne843Rpt1D091_Type = DisplayString
_Ne843Rpt1D091_Object = MibScalar
ne843Rpt1D091 = _Ne843Rpt1D091_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 95),
    _Ne843Rpt1D091_Type()
)
ne843Rpt1D091.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D091.setStatus("current")
_Ne843Rpt1D092_Type = DisplayString
_Ne843Rpt1D092_Object = MibScalar
ne843Rpt1D092 = _Ne843Rpt1D092_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 96),
    _Ne843Rpt1D092_Type()
)
ne843Rpt1D092.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D092.setStatus("current")
_Ne843Rpt1D093_Type = DisplayString
_Ne843Rpt1D093_Object = MibScalar
ne843Rpt1D093 = _Ne843Rpt1D093_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 97),
    _Ne843Rpt1D093_Type()
)
ne843Rpt1D093.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D093.setStatus("current")
_Ne843Rpt1D094_Type = DisplayString
_Ne843Rpt1D094_Object = MibScalar
ne843Rpt1D094 = _Ne843Rpt1D094_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 98),
    _Ne843Rpt1D094_Type()
)
ne843Rpt1D094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D094.setStatus("current")
_Ne843Rpt1D095_Type = DisplayString
_Ne843Rpt1D095_Object = MibScalar
ne843Rpt1D095 = _Ne843Rpt1D095_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 99),
    _Ne843Rpt1D095_Type()
)
ne843Rpt1D095.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D095.setStatus("current")
_Ne843Rpt1D096_Type = DisplayString
_Ne843Rpt1D096_Object = MibScalar
ne843Rpt1D096 = _Ne843Rpt1D096_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 100),
    _Ne843Rpt1D096_Type()
)
ne843Rpt1D096.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D096.setStatus("current")
_Ne843Rpt1D097_Type = DisplayString
_Ne843Rpt1D097_Object = MibScalar
ne843Rpt1D097 = _Ne843Rpt1D097_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 101),
    _Ne843Rpt1D097_Type()
)
ne843Rpt1D097.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D097.setStatus("current")
_Ne843Rpt1D098_Type = DisplayString
_Ne843Rpt1D098_Object = MibScalar
ne843Rpt1D098 = _Ne843Rpt1D098_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 102),
    _Ne843Rpt1D098_Type()
)
ne843Rpt1D098.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D098.setStatus("current")
_Ne843Rpt1D099_Type = DisplayString
_Ne843Rpt1D099_Object = MibScalar
ne843Rpt1D099 = _Ne843Rpt1D099_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 103),
    _Ne843Rpt1D099_Type()
)
ne843Rpt1D099.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D099.setStatus("current")
_Ne843Rpt1D100_Type = DisplayString
_Ne843Rpt1D100_Object = MibScalar
ne843Rpt1D100 = _Ne843Rpt1D100_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 104),
    _Ne843Rpt1D100_Type()
)
ne843Rpt1D100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D100.setStatus("current")
_Ne843Rpt1D101_Type = DisplayString
_Ne843Rpt1D101_Object = MibScalar
ne843Rpt1D101 = _Ne843Rpt1D101_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 105),
    _Ne843Rpt1D101_Type()
)
ne843Rpt1D101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D101.setStatus("current")
_Ne843Rpt1D102_Type = DisplayString
_Ne843Rpt1D102_Object = MibScalar
ne843Rpt1D102 = _Ne843Rpt1D102_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 106),
    _Ne843Rpt1D102_Type()
)
ne843Rpt1D102.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D102.setStatus("current")
_Ne843Rpt1D103_Type = DisplayString
_Ne843Rpt1D103_Object = MibScalar
ne843Rpt1D103 = _Ne843Rpt1D103_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 107),
    _Ne843Rpt1D103_Type()
)
ne843Rpt1D103.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D103.setStatus("current")
_Ne843Rpt1D104_Type = DisplayString
_Ne843Rpt1D104_Object = MibScalar
ne843Rpt1D104 = _Ne843Rpt1D104_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 108),
    _Ne843Rpt1D104_Type()
)
ne843Rpt1D104.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D104.setStatus("current")
_Ne843Rpt1D105_Type = DisplayString
_Ne843Rpt1D105_Object = MibScalar
ne843Rpt1D105 = _Ne843Rpt1D105_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 109),
    _Ne843Rpt1D105_Type()
)
ne843Rpt1D105.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D105.setStatus("current")
_Ne843Rpt1D106_Type = DisplayString
_Ne843Rpt1D106_Object = MibScalar
ne843Rpt1D106 = _Ne843Rpt1D106_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 110),
    _Ne843Rpt1D106_Type()
)
ne843Rpt1D106.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D106.setStatus("current")
_Ne843Rpt1D107_Type = DisplayString
_Ne843Rpt1D107_Object = MibScalar
ne843Rpt1D107 = _Ne843Rpt1D107_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 111),
    _Ne843Rpt1D107_Type()
)
ne843Rpt1D107.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D107.setStatus("current")
_Ne843Rpt1D108_Type = DisplayString
_Ne843Rpt1D108_Object = MibScalar
ne843Rpt1D108 = _Ne843Rpt1D108_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 112),
    _Ne843Rpt1D108_Type()
)
ne843Rpt1D108.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D108.setStatus("current")
_Ne843Rpt1D109_Type = DisplayString
_Ne843Rpt1D109_Object = MibScalar
ne843Rpt1D109 = _Ne843Rpt1D109_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 113),
    _Ne843Rpt1D109_Type()
)
ne843Rpt1D109.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D109.setStatus("current")
_Ne843Rpt1D110_Type = DisplayString
_Ne843Rpt1D110_Object = MibScalar
ne843Rpt1D110 = _Ne843Rpt1D110_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 114),
    _Ne843Rpt1D110_Type()
)
ne843Rpt1D110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D110.setStatus("current")
_Ne843Rpt1D111_Type = DisplayString
_Ne843Rpt1D111_Object = MibScalar
ne843Rpt1D111 = _Ne843Rpt1D111_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 115),
    _Ne843Rpt1D111_Type()
)
ne843Rpt1D111.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D111.setStatus("current")
_Ne843Rpt1D112_Type = DisplayString
_Ne843Rpt1D112_Object = MibScalar
ne843Rpt1D112 = _Ne843Rpt1D112_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 116),
    _Ne843Rpt1D112_Type()
)
ne843Rpt1D112.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D112.setStatus("current")
_Ne843Rpt1D113_Type = DisplayString
_Ne843Rpt1D113_Object = MibScalar
ne843Rpt1D113 = _Ne843Rpt1D113_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 117),
    _Ne843Rpt1D113_Type()
)
ne843Rpt1D113.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D113.setStatus("current")
_Ne843Rpt1D114_Type = DisplayString
_Ne843Rpt1D114_Object = MibScalar
ne843Rpt1D114 = _Ne843Rpt1D114_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 118),
    _Ne843Rpt1D114_Type()
)
ne843Rpt1D114.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D114.setStatus("current")
_Ne843Rpt1D115_Type = DisplayString
_Ne843Rpt1D115_Object = MibScalar
ne843Rpt1D115 = _Ne843Rpt1D115_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 119),
    _Ne843Rpt1D115_Type()
)
ne843Rpt1D115.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D115.setStatus("current")
_Ne843Rpt1D116_Type = DisplayString
_Ne843Rpt1D116_Object = MibScalar
ne843Rpt1D116 = _Ne843Rpt1D116_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 120),
    _Ne843Rpt1D116_Type()
)
ne843Rpt1D116.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D116.setStatus("current")
_Ne843Rpt1D117_Type = DisplayString
_Ne843Rpt1D117_Object = MibScalar
ne843Rpt1D117 = _Ne843Rpt1D117_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 121),
    _Ne843Rpt1D117_Type()
)
ne843Rpt1D117.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D117.setStatus("current")
_Ne843Rpt1D118_Type = DisplayString
_Ne843Rpt1D118_Object = MibScalar
ne843Rpt1D118 = _Ne843Rpt1D118_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 122),
    _Ne843Rpt1D118_Type()
)
ne843Rpt1D118.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D118.setStatus("current")
_Ne843Rpt1D119_Type = DisplayString
_Ne843Rpt1D119_Object = MibScalar
ne843Rpt1D119 = _Ne843Rpt1D119_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 123),
    _Ne843Rpt1D119_Type()
)
ne843Rpt1D119.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D119.setStatus("current")
_Ne843Rpt1D120_Type = DisplayString
_Ne843Rpt1D120_Object = MibScalar
ne843Rpt1D120 = _Ne843Rpt1D120_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 124),
    _Ne843Rpt1D120_Type()
)
ne843Rpt1D120.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D120.setStatus("current")
_Ne843Rpt1D121_Type = DisplayString
_Ne843Rpt1D121_Object = MibScalar
ne843Rpt1D121 = _Ne843Rpt1D121_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 125),
    _Ne843Rpt1D121_Type()
)
ne843Rpt1D121.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D121.setStatus("current")
_Ne843Rpt1D122_Type = DisplayString
_Ne843Rpt1D122_Object = MibScalar
ne843Rpt1D122 = _Ne843Rpt1D122_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 126),
    _Ne843Rpt1D122_Type()
)
ne843Rpt1D122.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D122.setStatus("current")
_Ne843Rpt1D123_Type = DisplayString
_Ne843Rpt1D123_Object = MibScalar
ne843Rpt1D123 = _Ne843Rpt1D123_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 127),
    _Ne843Rpt1D123_Type()
)
ne843Rpt1D123.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D123.setStatus("current")
_Ne843Rpt1D124_Type = DisplayString
_Ne843Rpt1D124_Object = MibScalar
ne843Rpt1D124 = _Ne843Rpt1D124_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 128),
    _Ne843Rpt1D124_Type()
)
ne843Rpt1D124.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D124.setStatus("current")
_Ne843Rpt1D125_Type = DisplayString
_Ne843Rpt1D125_Object = MibScalar
ne843Rpt1D125 = _Ne843Rpt1D125_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 129),
    _Ne843Rpt1D125_Type()
)
ne843Rpt1D125.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D125.setStatus("current")
_Ne843Rpt1D126_Type = DisplayString
_Ne843Rpt1D126_Object = MibScalar
ne843Rpt1D126 = _Ne843Rpt1D126_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 130),
    _Ne843Rpt1D126_Type()
)
ne843Rpt1D126.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D126.setStatus("current")
_Ne843Rpt1D127_Type = DisplayString
_Ne843Rpt1D127_Object = MibScalar
ne843Rpt1D127 = _Ne843Rpt1D127_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 131),
    _Ne843Rpt1D127_Type()
)
ne843Rpt1D127.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D127.setStatus("current")
_Ne843Rpt1D128_Type = DisplayString
_Ne843Rpt1D128_Object = MibScalar
ne843Rpt1D128 = _Ne843Rpt1D128_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 132),
    _Ne843Rpt1D128_Type()
)
ne843Rpt1D128.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D128.setStatus("current")
_Ne843Rpt1D129_Type = DisplayString
_Ne843Rpt1D129_Object = MibScalar
ne843Rpt1D129 = _Ne843Rpt1D129_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 133),
    _Ne843Rpt1D129_Type()
)
ne843Rpt1D129.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D129.setStatus("current")
_Ne843Rpt1D130_Type = DisplayString
_Ne843Rpt1D130_Object = MibScalar
ne843Rpt1D130 = _Ne843Rpt1D130_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 134),
    _Ne843Rpt1D130_Type()
)
ne843Rpt1D130.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D130.setStatus("current")
_Ne843Rpt1D131_Type = DisplayString
_Ne843Rpt1D131_Object = MibScalar
ne843Rpt1D131 = _Ne843Rpt1D131_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 135),
    _Ne843Rpt1D131_Type()
)
ne843Rpt1D131.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D131.setStatus("current")
_Ne843Rpt1D132_Type = DisplayString
_Ne843Rpt1D132_Object = MibScalar
ne843Rpt1D132 = _Ne843Rpt1D132_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 136),
    _Ne843Rpt1D132_Type()
)
ne843Rpt1D132.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D132.setStatus("current")
_Ne843Rpt1D133_Type = DisplayString
_Ne843Rpt1D133_Object = MibScalar
ne843Rpt1D133 = _Ne843Rpt1D133_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 137),
    _Ne843Rpt1D133_Type()
)
ne843Rpt1D133.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D133.setStatus("current")
_Ne843Rpt1D134_Type = DisplayString
_Ne843Rpt1D134_Object = MibScalar
ne843Rpt1D134 = _Ne843Rpt1D134_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 138),
    _Ne843Rpt1D134_Type()
)
ne843Rpt1D134.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D134.setStatus("current")
_Ne843Rpt1D135_Type = DisplayString
_Ne843Rpt1D135_Object = MibScalar
ne843Rpt1D135 = _Ne843Rpt1D135_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 139),
    _Ne843Rpt1D135_Type()
)
ne843Rpt1D135.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D135.setStatus("current")
_Ne843Rpt1D136_Type = DisplayString
_Ne843Rpt1D136_Object = MibScalar
ne843Rpt1D136 = _Ne843Rpt1D136_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 140),
    _Ne843Rpt1D136_Type()
)
ne843Rpt1D136.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D136.setStatus("current")
_Ne843Rpt1D137_Type = DisplayString
_Ne843Rpt1D137_Object = MibScalar
ne843Rpt1D137 = _Ne843Rpt1D137_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 141),
    _Ne843Rpt1D137_Type()
)
ne843Rpt1D137.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D137.setStatus("current")
_Ne843Rpt1D138_Type = DisplayString
_Ne843Rpt1D138_Object = MibScalar
ne843Rpt1D138 = _Ne843Rpt1D138_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 142),
    _Ne843Rpt1D138_Type()
)
ne843Rpt1D138.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D138.setStatus("current")
_Ne843Rpt1D139_Type = DisplayString
_Ne843Rpt1D139_Object = MibScalar
ne843Rpt1D139 = _Ne843Rpt1D139_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 143),
    _Ne843Rpt1D139_Type()
)
ne843Rpt1D139.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D139.setStatus("current")
_Ne843Rpt1D140_Type = DisplayString
_Ne843Rpt1D140_Object = MibScalar
ne843Rpt1D140 = _Ne843Rpt1D140_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 144),
    _Ne843Rpt1D140_Type()
)
ne843Rpt1D140.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D140.setStatus("current")
_Ne843Rpt1D141_Type = DisplayString
_Ne843Rpt1D141_Object = MibScalar
ne843Rpt1D141 = _Ne843Rpt1D141_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 145),
    _Ne843Rpt1D141_Type()
)
ne843Rpt1D141.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D141.setStatus("current")
_Ne843Rpt1D142_Type = DisplayString
_Ne843Rpt1D142_Object = MibScalar
ne843Rpt1D142 = _Ne843Rpt1D142_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 146),
    _Ne843Rpt1D142_Type()
)
ne843Rpt1D142.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D142.setStatus("current")
_Ne843Rpt1D143_Type = DisplayString
_Ne843Rpt1D143_Object = MibScalar
ne843Rpt1D143 = _Ne843Rpt1D143_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 147),
    _Ne843Rpt1D143_Type()
)
ne843Rpt1D143.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D143.setStatus("current")
_Ne843Rpt1D144_Type = DisplayString
_Ne843Rpt1D144_Object = MibScalar
ne843Rpt1D144 = _Ne843Rpt1D144_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 148),
    _Ne843Rpt1D144_Type()
)
ne843Rpt1D144.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D144.setStatus("current")
_Ne843Rpt1D145_Type = DisplayString
_Ne843Rpt1D145_Object = MibScalar
ne843Rpt1D145 = _Ne843Rpt1D145_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 149),
    _Ne843Rpt1D145_Type()
)
ne843Rpt1D145.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D145.setStatus("current")
_Ne843Rpt1D146_Type = DisplayString
_Ne843Rpt1D146_Object = MibScalar
ne843Rpt1D146 = _Ne843Rpt1D146_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 150),
    _Ne843Rpt1D146_Type()
)
ne843Rpt1D146.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D146.setStatus("current")
_Ne843Rpt1D147_Type = DisplayString
_Ne843Rpt1D147_Object = MibScalar
ne843Rpt1D147 = _Ne843Rpt1D147_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 151),
    _Ne843Rpt1D147_Type()
)
ne843Rpt1D147.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D147.setStatus("current")
_Ne843Rpt1D148_Type = DisplayString
_Ne843Rpt1D148_Object = MibScalar
ne843Rpt1D148 = _Ne843Rpt1D148_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 152),
    _Ne843Rpt1D148_Type()
)
ne843Rpt1D148.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D148.setStatus("current")
_Ne843Rpt1D149_Type = DisplayString
_Ne843Rpt1D149_Object = MibScalar
ne843Rpt1D149 = _Ne843Rpt1D149_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 153),
    _Ne843Rpt1D149_Type()
)
ne843Rpt1D149.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D149.setStatus("current")
_Ne843Rpt1D150_Type = DisplayString
_Ne843Rpt1D150_Object = MibScalar
ne843Rpt1D150 = _Ne843Rpt1D150_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 44, 154),
    _Ne843Rpt1D150_Type()
)
ne843Rpt1D150.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843Rpt1D150.setStatus("current")
_Ne843PicTable_Object = MibTable
ne843PicTable = _Ne843PicTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45)
)
if mibBuilder.loadTexts:
    ne843PicTable.setStatus("current")
_Ne843PicEntry_Object = MibTableRow
ne843PicEntry = _Ne843PicEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1)
)
ne843PicEntry.setIndexNames(
    (0, "NE843-MIB", "ne843PicEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843PicEntry.setStatus("current")


class _Ne843PicEntryIndex_Type(Integer32):
    """Custom type ne843PicEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843PicEntryIndex_Type.__name__ = "Integer32"
_Ne843PicEntryIndex_Object = MibTableColumn
ne843PicEntryIndex = _Ne843PicEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 1),
    _Ne843PicEntryIndex_Type()
)
ne843PicEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryIndex.setStatus("current")
_Ne843PicEntryIde_Type = DisplayString
_Ne843PicEntryIde_Object = MibTableColumn
ne843PicEntryIde = _Ne843PicEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 2),
    _Ne843PicEntryIde_Type()
)
ne843PicEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryIde.setStatus("current")
_Ne843PicEntryDes_Type = DisplayString
_Ne843PicEntryDes_Object = MibTableColumn
ne843PicEntryDes = _Ne843PicEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 3),
    _Ne843PicEntryDes_Type()
)
ne843PicEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryDes.setStatus("current")
_Ne843PicEntrySn_Type = DisplayString
_Ne843PicEntrySn_Object = MibTableColumn
ne843PicEntrySn = _Ne843PicEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 4),
    _Ne843PicEntrySn_Type()
)
ne843PicEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntrySn.setStatus("current")
_Ne843PicEntryCc_Type = DisplayString
_Ne843PicEntryCc_Object = MibTableColumn
ne843PicEntryCc = _Ne843PicEntryCc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 5),
    _Ne843PicEntryCc_Type()
)
ne843PicEntryCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryCc.setStatus("current")
_Ne843PicEntrySer_Type = DisplayString
_Ne843PicEntrySer_Object = MibTableColumn
ne843PicEntrySer = _Ne843PicEntrySer_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 6),
    _Ne843PicEntrySer_Type()
)
ne843PicEntrySer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntrySer.setStatus("current")
_Ne843PicEntryClei_Type = DisplayString
_Ne843PicEntryClei_Object = MibTableColumn
ne843PicEntryClei = _Ne843PicEntryClei_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 7),
    _Ne843PicEntryClei_Type()
)
ne843PicEntryClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryClei.setStatus("current")
_Ne843PicEntryCustpn2_Type = DisplayString
_Ne843PicEntryCustpn2_Object = MibTableColumn
ne843PicEntryCustpn2 = _Ne843PicEntryCustpn2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 8),
    _Ne843PicEntryCustpn2_Type()
)
ne843PicEntryCustpn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryCustpn2.setStatus("current")
_Ne843PicEntryAsstag2_Type = DisplayString
_Ne843PicEntryAsstag2_Object = MibTableColumn
ne843PicEntryAsstag2 = _Ne843PicEntryAsstag2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 9),
    _Ne843PicEntryAsstag2_Type()
)
ne843PicEntryAsstag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryAsstag2.setStatus("current")
_Ne843PicEntryStt_Type = DisplayString
_Ne843PicEntryStt_Object = MibTableColumn
ne843PicEntryStt = _Ne843PicEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 10),
    _Ne843PicEntryStt_Type()
)
ne843PicEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryStt.setStatus("current")
_Ne843PicEntryTyp_Type = DisplayString
_Ne843PicEntryTyp_Object = MibTableColumn
ne843PicEntryTyp = _Ne843PicEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 11),
    _Ne843PicEntryTyp_Type()
)
ne843PicEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryTyp.setStatus("current")
_Ne843PicEntryNst_Type = Integer32
_Ne843PicEntryNst_Object = MibTableColumn
ne843PicEntryNst = _Ne843PicEntryNst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 12),
    _Ne843PicEntryNst_Type()
)
ne843PicEntryNst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryNst.setStatus("current")
_Ne843PicEntryNvt_Type = Integer32
_Ne843PicEntryNvt_Object = MibTableColumn
ne843PicEntryNvt = _Ne843PicEntryNvt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 13),
    _Ne843PicEntryNvt_Type()
)
ne843PicEntryNvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryNvt.setStatus("current")
_Ne843PicEntryVera_Type = DisplayString
_Ne843PicEntryVera_Object = MibTableColumn
ne843PicEntryVera = _Ne843PicEntryVera_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 14),
    _Ne843PicEntryVera_Type()
)
ne843PicEntryVera.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryVera.setStatus("current")
_Ne843PicEntryPid_Type = DisplayString
_Ne843PicEntryPid_Object = MibTableColumn
ne843PicEntryPid = _Ne843PicEntryPid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 15),
    _Ne843PicEntryPid_Type()
)
ne843PicEntryPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryPid.setStatus("current")
_Ne843PicEntryPcf_Type = DisplayString
_Ne843PicEntryPcf_Object = MibTableColumn
ne843PicEntryPcf = _Ne843PicEntryPcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 16),
    _Ne843PicEntryPcf_Type()
)
ne843PicEntryPcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryPcf.setStatus("current")
_Ne843PicEntryNumslot_Type = Integer32
_Ne843PicEntryNumslot_Object = MibTableColumn
ne843PicEntryNumslot = _Ne843PicEntryNumslot_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 17),
    _Ne843PicEntryNumslot_Type()
)
ne843PicEntryNumslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PicEntryNumslot.setStatus("current")
_Ne843PicEntryCbf_Type = DisplayString
_Ne843PicEntryCbf_Object = MibTableColumn
ne843PicEntryCbf = _Ne843PicEntryCbf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 18),
    _Ne843PicEntryCbf_Type()
)
ne843PicEntryCbf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryCbf.setStatus("current")


class _Ne843PicEntryFajae_Type(Integer32):
    """Custom type ne843PicEntryFajae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryFajae_Type.__name__ = "Integer32"
_Ne843PicEntryFajae_Object = MibTableColumn
ne843PicEntryFajae = _Ne843PicEntryFajae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 19),
    _Ne843PicEntryFajae_Type()
)
ne843PicEntryFajae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryFajae.setStatus("current")
_Ne843PicEntryFajrly_Type = DisplayString
_Ne843PicEntryFajrly_Object = MibTableColumn
ne843PicEntryFajrly = _Ne843PicEntryFajrly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 20),
    _Ne843PicEntryFajrly_Type()
)
ne843PicEntryFajrly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryFajrly.setStatus("current")


class _Ne843PicEntryOsae_Type(Integer32):
    """Custom type ne843PicEntryOsae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryOsae_Type.__name__ = "Integer32"
_Ne843PicEntryOsae_Object = MibTableColumn
ne843PicEntryOsae = _Ne843PicEntryOsae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 21),
    _Ne843PicEntryOsae_Type()
)
ne843PicEntryOsae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOsae.setStatus("current")
_Ne843PicEntryOsarly_Type = DisplayString
_Ne843PicEntryOsarly_Object = MibTableColumn
ne843PicEntryOsarly = _Ne843PicEntryOsarly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 22),
    _Ne843PicEntryOsarly_Type()
)
ne843PicEntryOsarly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOsarly.setStatus("current")


class _Ne843PicEntryTmpe_Type(Integer32):
    """Custom type ne843PicEntryTmpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryTmpe_Type.__name__ = "Integer32"
_Ne843PicEntryTmpe_Object = MibTableColumn
ne843PicEntryTmpe = _Ne843PicEntryTmpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 23),
    _Ne843PicEntryTmpe_Type()
)
ne843PicEntryTmpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryTmpe.setStatus("current")
_Ne843PicEntryTmprly_Type = DisplayString
_Ne843PicEntryTmprly_Object = MibTableColumn
ne843PicEntryTmprly = _Ne843PicEntryTmprly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 24),
    _Ne843PicEntryTmprly_Type()
)
ne843PicEntryTmprly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryTmprly.setStatus("current")
_Ne843PicEntryVlvs_Type = DisplayString
_Ne843PicEntryVlvs_Object = MibTableColumn
ne843PicEntryVlvs = _Ne843PicEntryVlvs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 25),
    _Ne843PicEntryVlvs_Type()
)
ne843PicEntryVlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvs.setStatus("current")
_Ne843PicEntryVlvlat_Type = DisplayString
_Ne843PicEntryVlvlat_Object = MibTableColumn
ne843PicEntryVlvlat = _Ne843PicEntryVlvlat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 26),
    _Ne843PicEntryVlvlat_Type()
)
ne843PicEntryVlvlat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvlat.setStatus("current")


class _Ne843PicEntryVlvae_Type(Integer32):
    """Custom type ne843PicEntryVlvae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryVlvae_Type.__name__ = "Integer32"
_Ne843PicEntryVlvae_Object = MibTableColumn
ne843PicEntryVlvae = _Ne843PicEntryVlvae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 27),
    _Ne843PicEntryVlvae_Type()
)
ne843PicEntryVlvae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvae.setStatus("current")
_Ne843PicEntryVlvath_Type = Integer32
_Ne843PicEntryVlvath_Object = MibTableColumn
ne843PicEntryVlvath = _Ne843PicEntryVlvath_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 28),
    _Ne843PicEntryVlvath_Type()
)
ne843PicEntryVlvath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvath.setStatus("current")


class _Ne843PicEntryVlvbe_Type(Integer32):
    """Custom type ne843PicEntryVlvbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryVlvbe_Type.__name__ = "Integer32"
_Ne843PicEntryVlvbe_Object = MibTableColumn
ne843PicEntryVlvbe = _Ne843PicEntryVlvbe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 29),
    _Ne843PicEntryVlvbe_Type()
)
ne843PicEntryVlvbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvbe.setStatus("current")
_Ne843PicEntryVlvbth_Type = Integer32
_Ne843PicEntryVlvbth_Object = MibTableColumn
ne843PicEntryVlvbth = _Ne843PicEntryVlvbth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 30),
    _Ne843PicEntryVlvbth_Type()
)
ne843PicEntryVlvbth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvbth.setStatus("current")
_Ne843PicEntryVlvrly_Type = DisplayString
_Ne843PicEntryVlvrly_Object = MibTableColumn
ne843PicEntryVlvrly = _Ne843PicEntryVlvrly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 31),
    _Ne843PicEntryVlvrly_Type()
)
ne843PicEntryVlvrly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryVlvrly.setStatus("current")
_Ne843PicEntryOvls_Type = DisplayString
_Ne843PicEntryOvls_Object = MibTableColumn
ne843PicEntryOvls = _Ne843PicEntryOvls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 32),
    _Ne843PicEntryOvls_Type()
)
ne843PicEntryOvls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvls.setStatus("current")
_Ne843PicEntryOlvlat_Type = DisplayString
_Ne843PicEntryOlvlat_Object = MibTableColumn
ne843PicEntryOlvlat = _Ne843PicEntryOlvlat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 33),
    _Ne843PicEntryOlvlat_Type()
)
ne843PicEntryOlvlat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOlvlat.setStatus("current")


class _Ne843PicEntryOvlae_Type(Integer32):
    """Custom type ne843PicEntryOvlae based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryOvlae_Type.__name__ = "Integer32"
_Ne843PicEntryOvlae_Object = MibTableColumn
ne843PicEntryOvlae = _Ne843PicEntryOvlae_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 34),
    _Ne843PicEntryOvlae_Type()
)
ne843PicEntryOvlae.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvlae.setStatus("current")
_Ne843PicEntryOvlath_Type = Integer32
_Ne843PicEntryOvlath_Object = MibTableColumn
ne843PicEntryOvlath = _Ne843PicEntryOvlath_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 35),
    _Ne843PicEntryOvlath_Type()
)
ne843PicEntryOvlath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvlath.setStatus("current")


class _Ne843PicEntryOvlbe_Type(Integer32):
    """Custom type ne843PicEntryOvlbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryOvlbe_Type.__name__ = "Integer32"
_Ne843PicEntryOvlbe_Object = MibTableColumn
ne843PicEntryOvlbe = _Ne843PicEntryOvlbe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 36),
    _Ne843PicEntryOvlbe_Type()
)
ne843PicEntryOvlbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvlbe.setStatus("current")
_Ne843PicEntryOvlbth_Type = Integer32
_Ne843PicEntryOvlbth_Object = MibTableColumn
ne843PicEntryOvlbth = _Ne843PicEntryOvlbth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 37),
    _Ne843PicEntryOvlbth_Type()
)
ne843PicEntryOvlbth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvlbth.setStatus("current")
_Ne843PicEntryOvlrly_Type = DisplayString
_Ne843PicEntryOvlrly_Object = MibTableColumn
ne843PicEntryOvlrly = _Ne843PicEntryOvlrly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 38),
    _Ne843PicEntryOvlrly_Type()
)
ne843PicEntryOvlrly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryOvlrly.setStatus("current")


class _Ne843PicEntryEpoe_Type(Integer32):
    """Custom type ne843PicEntryEpoe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryEpoe_Type.__name__ = "Integer32"
_Ne843PicEntryEpoe_Object = MibTableColumn
ne843PicEntryEpoe = _Ne843PicEntryEpoe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 39),
    _Ne843PicEntryEpoe_Type()
)
ne843PicEntryEpoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryEpoe.setStatus("current")
_Ne843PicEntryEporly_Type = DisplayString
_Ne843PicEntryEporly_Object = MibTableColumn
ne843PicEntryEporly = _Ne843PicEntryEporly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 40),
    _Ne843PicEntryEporly_Type()
)
ne843PicEntryEporly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryEporly.setStatus("current")


class _Ne843PicEntryPcauxe_Type(Integer32):
    """Custom type ne843PicEntryPcauxe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntryPcauxe_Type.__name__ = "Integer32"
_Ne843PicEntryPcauxe_Object = MibTableColumn
ne843PicEntryPcauxe = _Ne843PicEntryPcauxe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 41),
    _Ne843PicEntryPcauxe_Type()
)
ne843PicEntryPcauxe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPcauxe.setStatus("current")
_Ne843PicEntryPcauxr_Type = DisplayString
_Ne843PicEntryPcauxr_Object = MibTableColumn
ne843PicEntryPcauxr = _Ne843PicEntryPcauxr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 42),
    _Ne843PicEntryPcauxr_Type()
)
ne843PicEntryPcauxr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPcauxr.setStatus("current")


class _Ne843PicEntrySlote_Type(Integer32):
    """Custom type ne843PicEntrySlote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843PicEntrySlote_Type.__name__ = "Integer32"
_Ne843PicEntrySlote_Object = MibTableColumn
ne843PicEntrySlote = _Ne843PicEntrySlote_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 43),
    _Ne843PicEntrySlote_Type()
)
ne843PicEntrySlote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntrySlote.setStatus("current")
_Ne843PicEntrySlotrly_Type = DisplayString
_Ne843PicEntrySlotrly_Object = MibTableColumn
ne843PicEntrySlotrly = _Ne843PicEntrySlotrly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 44),
    _Ne843PicEntrySlotrly_Type()
)
ne843PicEntrySlotrly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntrySlotrly.setStatus("current")
_Ne843PicEntryDpmode_Type = DisplayString
_Ne843PicEntryDpmode_Object = MibTableColumn
ne843PicEntryDpmode = _Ne843PicEntryDpmode_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 45),
    _Ne843PicEntryDpmode_Type()
)
ne843PicEntryDpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryDpmode.setStatus("current")
_Ne843PicEntryPnldes_Type = DisplayString
_Ne843PicEntryPnldes_Object = MibTableColumn
ne843PicEntryPnldes = _Ne843PicEntryPnldes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 46),
    _Ne843PicEntryPnldes_Type()
)
ne843PicEntryPnldes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnldes.setStatus("current")
_Ne843PicEntryMdl_Type = DisplayString
_Ne843PicEntryMdl_Object = MibTableColumn
ne843PicEntryMdl = _Ne843PicEntryMdl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 47),
    _Ne843PicEntryMdl_Type()
)
ne843PicEntryMdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryMdl.setStatus("current")
_Ne843PicEntryPnlsn_Type = DisplayString
_Ne843PicEntryPnlsn_Object = MibTableColumn
ne843PicEntryPnlsn = _Ne843PicEntryPnlsn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 48),
    _Ne843PicEntryPnlsn_Type()
)
ne843PicEntryPnlsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnlsn.setStatus("current")
_Ne843PicEntryPnlcc_Type = DisplayString
_Ne843PicEntryPnlcc_Object = MibTableColumn
ne843PicEntryPnlcc = _Ne843PicEntryPnlcc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 49),
    _Ne843PicEntryPnlcc_Type()
)
ne843PicEntryPnlcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnlcc.setStatus("current")
_Ne843PicEntryPnlser_Type = DisplayString
_Ne843PicEntryPnlser_Object = MibTableColumn
ne843PicEntryPnlser = _Ne843PicEntryPnlser_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 50),
    _Ne843PicEntryPnlser_Type()
)
ne843PicEntryPnlser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnlser.setStatus("current")
_Ne843PicEntryPnlclei_Type = DisplayString
_Ne843PicEntryPnlclei_Object = MibTableColumn
ne843PicEntryPnlclei = _Ne843PicEntryPnlclei_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 51),
    _Ne843PicEntryPnlclei_Type()
)
ne843PicEntryPnlclei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnlclei.setStatus("current")
_Ne843PicEntryCustpn1_Type = DisplayString
_Ne843PicEntryCustpn1_Object = MibTableColumn
ne843PicEntryCustpn1 = _Ne843PicEntryCustpn1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 52),
    _Ne843PicEntryCustpn1_Type()
)
ne843PicEntryCustpn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryCustpn1.setStatus("current")
_Ne843PicEntryAsstag1_Type = DisplayString
_Ne843PicEntryAsstag1_Object = MibTableColumn
ne843PicEntryAsstag1 = _Ne843PicEntryAsstag1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 53),
    _Ne843PicEntryAsstag1_Type()
)
ne843PicEntryAsstag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryAsstag1.setStatus("current")
_Ne843PicEntryRtng_Type = DisplayString
_Ne843PicEntryRtng_Object = MibTableColumn
ne843PicEntryRtng = _Ne843PicEntryRtng_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 54),
    _Ne843PicEntryRtng_Type()
)
ne843PicEntryRtng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryRtng.setStatus("current")
_Ne843PicEntryPnlsize_Type = DisplayString
_Ne843PicEntryPnlsize_Object = MibTableColumn
ne843PicEntryPnlsize = _Ne843PicEntryPnlsize_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 45, 1, 55),
    _Ne843PicEntryPnlsize_Type()
)
ne843PicEntryPnlsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PicEntryPnlsize.setStatus("current")
_Ne843PcmTable_Object = MibTable
ne843PcmTable = _Ne843PcmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46)
)
if mibBuilder.loadTexts:
    ne843PcmTable.setStatus("current")
_Ne843PcmEntry_Object = MibTableRow
ne843PcmEntry = _Ne843PcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1)
)
ne843PcmEntry.setIndexNames(
    (0, "NE843-MIB", "ne843PcmEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843PcmEntry.setStatus("current")


class _Ne843PcmEntryIndex_Type(Integer32):
    """Custom type ne843PcmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843PcmEntryIndex_Type.__name__ = "Integer32"
_Ne843PcmEntryIndex_Object = MibTableColumn
ne843PcmEntryIndex = _Ne843PcmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 1),
    _Ne843PcmEntryIndex_Type()
)
ne843PcmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcmEntryIndex.setStatus("current")
_Ne843PcmEntryIde_Type = DisplayString
_Ne843PcmEntryIde_Object = MibTableColumn
ne843PcmEntryIde = _Ne843PcmEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 2),
    _Ne843PcmEntryIde_Type()
)
ne843PcmEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcmEntryIde.setStatus("current")
_Ne843PcmEntryDes_Type = DisplayString
_Ne843PcmEntryDes_Object = MibTableColumn
ne843PcmEntryDes = _Ne843PcmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 3),
    _Ne843PcmEntryDes_Type()
)
ne843PcmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcmEntryDes.setStatus("current")
_Ne843PcmEntryVal_Type = DisplayString
_Ne843PcmEntryVal_Object = MibTableColumn
ne843PcmEntryVal = _Ne843PcmEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 4),
    _Ne843PcmEntryVal_Type()
)
ne843PcmEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcmEntryVal.setStatus("current")
_Ne843PcmEntrySht_Type = DisplayString
_Ne843PcmEntrySht_Object = MibTableColumn
ne843PcmEntrySht = _Ne843PcmEntrySht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 5),
    _Ne843PcmEntrySht_Type()
)
ne843PcmEntrySht.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcmEntrySht.setStatus("current")
_Ne843PcmEntrySha_Type = Integer32
_Ne843PcmEntrySha_Object = MibTableColumn
ne843PcmEntrySha = _Ne843PcmEntrySha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 6),
    _Ne843PcmEntrySha_Type()
)
ne843PcmEntrySha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcmEntrySha.setStatus("current")


class _Ne843PcmEntryShv_Type(Integer32):
    """Custom type ne843PcmEntryShv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_Ne843PcmEntryShv_Type.__name__ = "Integer32"
_Ne843PcmEntryShv_Object = MibTableColumn
ne843PcmEntryShv = _Ne843PcmEntryShv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 46, 1, 7),
    _Ne843PcmEntryShv_Type()
)
ne843PcmEntryShv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcmEntryShv.setStatus("current")
_Ne843PvmTable_Object = MibTable
ne843PvmTable = _Ne843PvmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47)
)
if mibBuilder.loadTexts:
    ne843PvmTable.setStatus("current")
_Ne843PvmEntry_Object = MibTableRow
ne843PvmEntry = _Ne843PvmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47, 1)
)
ne843PvmEntry.setIndexNames(
    (0, "NE843-MIB", "ne843PvmEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843PvmEntry.setStatus("current")


class _Ne843PvmEntryIndex_Type(Integer32):
    """Custom type ne843PvmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843PvmEntryIndex_Type.__name__ = "Integer32"
_Ne843PvmEntryIndex_Object = MibTableColumn
ne843PvmEntryIndex = _Ne843PvmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47, 1, 1),
    _Ne843PvmEntryIndex_Type()
)
ne843PvmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PvmEntryIndex.setStatus("current")
_Ne843PvmEntryIde_Type = DisplayString
_Ne843PvmEntryIde_Object = MibTableColumn
ne843PvmEntryIde = _Ne843PvmEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47, 1, 2),
    _Ne843PvmEntryIde_Type()
)
ne843PvmEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PvmEntryIde.setStatus("current")
_Ne843PvmEntryDes_Type = DisplayString
_Ne843PvmEntryDes_Object = MibTableColumn
ne843PvmEntryDes = _Ne843PvmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47, 1, 3),
    _Ne843PvmEntryDes_Type()
)
ne843PvmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PvmEntryDes.setStatus("current")
_Ne843PvmEntryVal_Type = Integer32
_Ne843PvmEntryVal_Object = MibTableColumn
ne843PvmEntryVal = _Ne843PvmEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 47, 1, 4),
    _Ne843PvmEntryVal_Type()
)
ne843PvmEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PvmEntryVal.setStatus("current")
_Ne843PtmTable_Object = MibTable
ne843PtmTable = _Ne843PtmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48)
)
if mibBuilder.loadTexts:
    ne843PtmTable.setStatus("current")
_Ne843PtmEntry_Object = MibTableRow
ne843PtmEntry = _Ne843PtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1)
)
ne843PtmEntry.setIndexNames(
    (0, "NE843-MIB", "ne843PtmEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843PtmEntry.setStatus("current")


class _Ne843PtmEntryIndex_Type(Integer32):
    """Custom type ne843PtmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843PtmEntryIndex_Type.__name__ = "Integer32"
_Ne843PtmEntryIndex_Object = MibTableColumn
ne843PtmEntryIndex = _Ne843PtmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 1),
    _Ne843PtmEntryIndex_Type()
)
ne843PtmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryIndex.setStatus("current")
_Ne843PtmEntryIde_Type = DisplayString
_Ne843PtmEntryIde_Object = MibTableColumn
ne843PtmEntryIde = _Ne843PtmEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 2),
    _Ne843PtmEntryIde_Type()
)
ne843PtmEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryIde.setStatus("current")
_Ne843PtmEntryDes_Type = DisplayString
_Ne843PtmEntryDes_Object = MibTableColumn
ne843PtmEntryDes = _Ne843PtmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 3),
    _Ne843PtmEntryDes_Type()
)
ne843PtmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PtmEntryDes.setStatus("current")
_Ne843PtmEntryBamt_Type = Integer32
_Ne843PtmEntryBamt_Object = MibTableColumn
ne843PtmEntryBamt = _Ne843PtmEntryBamt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 4),
    _Ne843PtmEntryBamt_Type()
)
ne843PtmEntryBamt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryBamt.setStatus("current")
_Ne843PtmEntryNat_Type = Integer32
_Ne843PtmEntryNat_Object = MibTableColumn
ne843PtmEntryNat = _Ne843PtmEntryNat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 5),
    _Ne843PtmEntryNat_Type()
)
ne843PtmEntryNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryNat.setStatus("current")
_Ne843PtmEntryHamt_Type = Integer32
_Ne843PtmEntryHamt_Object = MibTableColumn
ne843PtmEntryHamt = _Ne843PtmEntryHamt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 6),
    _Ne843PtmEntryHamt_Type()
)
ne843PtmEntryHamt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryHamt.setStatus("current")
_Ne843PtmEntryLamt_Type = Integer32
_Ne843PtmEntryLamt_Object = MibTableColumn
ne843PtmEntryLamt = _Ne843PtmEntryLamt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 7),
    _Ne843PtmEntryLamt_Type()
)
ne843PtmEntryLamt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryLamt.setStatus("current")
_Ne843PtmEntryNtm_Type = Integer32
_Ne843PtmEntryNtm_Object = MibTableColumn
ne843PtmEntryNtm = _Ne843PtmEntryNtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 8),
    _Ne843PtmEntryNtm_Type()
)
ne843PtmEntryNtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryNtm.setStatus("current")
_Ne843PtmEntryHbt_Type = Integer32
_Ne843PtmEntryHbt_Object = MibTableColumn
ne843PtmEntryHbt = _Ne843PtmEntryHbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 9),
    _Ne843PtmEntryHbt_Type()
)
ne843PtmEntryHbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryHbt.setStatus("current")
_Ne843PtmEntryLbt_Type = Integer32
_Ne843PtmEntryLbt_Object = MibTableColumn
ne843PtmEntryLbt = _Ne843PtmEntryLbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 10),
    _Ne843PtmEntryLbt_Type()
)
ne843PtmEntryLbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryLbt.setStatus("current")
_Ne843PtmEntryNbut_Type = Integer32
_Ne843PtmEntryNbut_Object = MibTableColumn
ne843PtmEntryNbut = _Ne843PtmEntryNbut_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 11),
    _Ne843PtmEntryNbut_Type()
)
ne843PtmEntryNbut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryNbut.setStatus("current")
_Ne843PtmEntryHbut_Type = Integer32
_Ne843PtmEntryHbut_Object = MibTableColumn
ne843PtmEntryHbut = _Ne843PtmEntryHbut_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 12),
    _Ne843PtmEntryHbut_Type()
)
ne843PtmEntryHbut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryHbut.setStatus("current")
_Ne843PtmEntryLbut_Type = Integer32
_Ne843PtmEntryLbut_Object = MibTableColumn
ne843PtmEntryLbut = _Ne843PtmEntryLbut_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 48, 1, 13),
    _Ne843PtmEntryLbut_Type()
)
ne843PtmEntryLbut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PtmEntryLbut.setStatus("current")
_Ne843PcsTable_Object = MibTable
ne843PcsTable = _Ne843PcsTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49)
)
if mibBuilder.loadTexts:
    ne843PcsTable.setStatus("current")
_Ne843PcsEntry_Object = MibTableRow
ne843PcsEntry = _Ne843PcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1)
)
ne843PcsEntry.setIndexNames(
    (0, "NE843-MIB", "ne843PcsEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843PcsEntry.setStatus("current")


class _Ne843PcsEntryIndex_Type(Integer32):
    """Custom type ne843PcsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843PcsEntryIndex_Type.__name__ = "Integer32"
_Ne843PcsEntryIndex_Object = MibTableColumn
ne843PcsEntryIndex = _Ne843PcsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 1),
    _Ne843PcsEntryIndex_Type()
)
ne843PcsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcsEntryIndex.setStatus("current")
_Ne843PcsEntryIde_Type = DisplayString
_Ne843PcsEntryIde_Object = MibTableColumn
ne843PcsEntryIde = _Ne843PcsEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 2),
    _Ne843PcsEntryIde_Type()
)
ne843PcsEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcsEntryIde.setStatus("current")
_Ne843PcsEntryDes_Type = DisplayString
_Ne843PcsEntryDes_Object = MibTableColumn
ne843PcsEntryDes = _Ne843PcsEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 3),
    _Ne843PcsEntryDes_Type()
)
ne843PcsEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryDes.setStatus("current")
_Ne843PcsEntryStt_Type = DisplayString
_Ne843PcsEntryStt_Object = MibTableColumn
ne843PcsEntryStt = _Ne843PcsEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 4),
    _Ne843PcsEntryStt_Type()
)
ne843PcsEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843PcsEntryStt.setStatus("current")
_Ne843PcsEntryTyp_Type = DisplayString
_Ne843PcsEntryTyp_Object = MibTableColumn
ne843PcsEntryTyp = _Ne843PcsEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 5),
    _Ne843PcsEntryTyp_Type()
)
ne843PcsEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryTyp.setStatus("current")
_Ne843PcsEntryPole_Type = Integer32
_Ne843PcsEntryPole_Object = MibTableColumn
ne843PcsEntryPole = _Ne843PcsEntryPole_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 6),
    _Ne843PcsEntryPole_Type()
)
ne843PcsEntryPole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryPole.setStatus("current")
_Ne843PcsEntryPolp_Type = Integer32
_Ne843PcsEntryPolp_Object = MibTableColumn
ne843PcsEntryPolp = _Ne843PcsEntryPolp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 7),
    _Ne843PcsEntryPolp_Type()
)
ne843PcsEntryPolp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryPolp.setStatus("current")
_Ne843PcsEntryPopn_Type = DisplayString
_Ne843PcsEntryPopn_Object = MibTableColumn
ne843PcsEntryPopn = _Ne843PcsEntryPopn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 8),
    _Ne843PcsEntryPopn_Type()
)
ne843PcsEntryPopn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryPopn.setStatus("current")


class _Ne843PcsEntryTrp_Type(Integer32):
    """Custom type ne843PcsEntryTrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843PcsEntryTrp_Type.__name__ = "Integer32"
_Ne843PcsEntryTrp_Object = MibTableColumn
ne843PcsEntryTrp = _Ne843PcsEntryTrp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 9),
    _Ne843PcsEntryTrp_Type()
)
ne843PcsEntryTrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryTrp.setStatus("current")


class _Ne843PcsEntryBad_Type(Integer32):
    """Custom type ne843PcsEntryBad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843PcsEntryBad_Type.__name__ = "Integer32"
_Ne843PcsEntryBad_Object = MibTableColumn
ne843PcsEntryBad = _Ne843PcsEntryBad_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 10),
    _Ne843PcsEntryBad_Type()
)
ne843PcsEntryBad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryBad.setStatus("current")
_Ne843PcsEntryCbf_Type = DisplayString
_Ne843PcsEntryCbf_Object = MibTableColumn
ne843PcsEntryCbf = _Ne843PcsEntryCbf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 11),
    _Ne843PcsEntryCbf_Type()
)
ne843PcsEntryCbf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryCbf.setStatus("current")


class _Ne843PcsEntrySlv_Type(Integer32):
    """Custom type ne843PcsEntrySlv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ne843PcsEntrySlv_Type.__name__ = "Integer32"
_Ne843PcsEntrySlv_Object = MibTableColumn
ne843PcsEntrySlv = _Ne843PcsEntrySlv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 12),
    _Ne843PcsEntrySlv_Type()
)
ne843PcsEntrySlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntrySlv.setStatus("current")
_Ne843PcsEntryRtng_Type = Integer32
_Ne843PcsEntryRtng_Object = MibTableColumn
ne843PcsEntryRtng = _Ne843PcsEntryRtng_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 49, 1, 13),
    _Ne843PcsEntryRtng_Type()
)
ne843PcsEntryRtng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843PcsEntryRtng.setStatus("current")
_Ne843DbyTable_Object = MibTable
ne843DbyTable = _Ne843DbyTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50)
)
if mibBuilder.loadTexts:
    ne843DbyTable.setStatus("current")
_Ne843DbyEntry_Object = MibTableRow
ne843DbyEntry = _Ne843DbyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1)
)
ne843DbyEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DbyEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DbyEntry.setStatus("current")


class _Ne843DbyEntryIndex_Type(Integer32):
    """Custom type ne843DbyEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DbyEntryIndex_Type.__name__ = "Integer32"
_Ne843DbyEntryIndex_Object = MibTableColumn
ne843DbyEntryIndex = _Ne843DbyEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 1),
    _Ne843DbyEntryIndex_Type()
)
ne843DbyEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntryIndex.setStatus("current")
_Ne843DbyEntryIde_Type = DisplayString
_Ne843DbyEntryIde_Object = MibTableColumn
ne843DbyEntryIde = _Ne843DbyEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 2),
    _Ne843DbyEntryIde_Type()
)
ne843DbyEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntryIde.setStatus("current")
_Ne843DbyEntryDes_Type = DisplayString
_Ne843DbyEntryDes_Object = MibTableColumn
ne843DbyEntryDes = _Ne843DbyEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 3),
    _Ne843DbyEntryDes_Type()
)
ne843DbyEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryDes.setStatus("current")
_Ne843DbyEntrySn_Type = DisplayString
_Ne843DbyEntrySn_Object = MibTableColumn
ne843DbyEntrySn = _Ne843DbyEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 4),
    _Ne843DbyEntrySn_Type()
)
ne843DbyEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntrySn.setStatus("current")
_Ne843DbyEntryStt_Type = DisplayString
_Ne843DbyEntryStt_Object = MibTableColumn
ne843DbyEntryStt = _Ne843DbyEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 5),
    _Ne843DbyEntryStt_Type()
)
ne843DbyEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntryStt.setStatus("current")


class _Ne843DbyEntrySha_Type(Integer32):
    """Custom type ne843DbyEntrySha based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_Ne843DbyEntrySha_Type.__name__ = "Integer32"
_Ne843DbyEntrySha_Object = MibTableColumn
ne843DbyEntrySha = _Ne843DbyEntrySha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 6),
    _Ne843DbyEntrySha_Type()
)
ne843DbyEntrySha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntrySha.setStatus("current")
if mibBuilder.loadTexts:
    ne843DbyEntrySha.setUnits("Amps")


class _Ne843DbyEntryNpl_Type(Integer32):
    """Custom type ne843DbyEntryNpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ne843DbyEntryNpl_Type.__name__ = "Integer32"
_Ne843DbyEntryNpl_Object = MibTableColumn
ne843DbyEntryNpl = _Ne843DbyEntryNpl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 7),
    _Ne843DbyEntryNpl_Type()
)
ne843DbyEntryNpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryNpl.setStatus("current")
_Ne843DbyEntryPmt_Type = DisplayString
_Ne843DbyEntryPmt_Object = MibTableColumn
ne843DbyEntryPmt = _Ne843DbyEntryPmt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 8),
    _Ne843DbyEntryPmt_Type()
)
ne843DbyEntryPmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryPmt.setStatus("current")
_Ne843DbyEntryIds_Type = DisplayString
_Ne843DbyEntryIds_Object = MibTableColumn
ne843DbyEntryIds = _Ne843DbyEntryIds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 9),
    _Ne843DbyEntryIds_Type()
)
ne843DbyEntryIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryIds.setStatus("current")


class _Ne843DbyEntryBze_Type(Integer32):
    """Custom type ne843DbyEntryBze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843DbyEntryBze_Type.__name__ = "Integer32"
_Ne843DbyEntryBze_Object = MibTableColumn
ne843DbyEntryBze = _Ne843DbyEntryBze_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 10),
    _Ne843DbyEntryBze_Type()
)
ne843DbyEntryBze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryBze.setStatus("current")


class _Ne843DbyEntryOle_Type(Integer32):
    """Custom type ne843DbyEntryOle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843DbyEntryOle_Type.__name__ = "Integer32"
_Ne843DbyEntryOle_Object = MibTableColumn
ne843DbyEntryOle = _Ne843DbyEntryOle_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 11),
    _Ne843DbyEntryOle_Type()
)
ne843DbyEntryOle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryOle.setStatus("current")
_Ne843DbyEntryOri_Type = DisplayString
_Ne843DbyEntryOri_Object = MibTableColumn
ne843DbyEntryOri = _Ne843DbyEntryOri_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 12),
    _Ne843DbyEntryOri_Type()
)
ne843DbyEntryOri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryOri.setStatus("current")


class _Ne843DbyEntryCmb_Type(Integer32):
    """Custom type ne843DbyEntryCmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843DbyEntryCmb_Type.__name__ = "Integer32"
_Ne843DbyEntryCmb_Object = MibTableColumn
ne843DbyEntryCmb = _Ne843DbyEntryCmb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 13),
    _Ne843DbyEntryCmb_Type()
)
ne843DbyEntryCmb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DbyEntryCmb.setStatus("current")
_Ne843DbyEntrySmw_Type = DisplayString
_Ne843DbyEntrySmw_Object = MibTableColumn
ne843DbyEntrySmw = _Ne843DbyEntrySmw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 14),
    _Ne843DbyEntrySmw_Type()
)
ne843DbyEntrySmw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntrySmw.setStatus("current")
_Ne843DbyEntryCca_Type = DisplayString
_Ne843DbyEntryCca_Object = MibTableColumn
ne843DbyEntryCca = _Ne843DbyEntryCca_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 50, 1, 15),
    _Ne843DbyEntryCca_Type()
)
ne843DbyEntryCca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DbyEntryCca.setStatus("current")
_Ne843DpnTable_Object = MibTable
ne843DpnTable = _Ne843DpnTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51)
)
if mibBuilder.loadTexts:
    ne843DpnTable.setStatus("current")
_Ne843DpnEntry_Object = MibTableRow
ne843DpnEntry = _Ne843DpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1)
)
ne843DpnEntry.setIndexNames(
    (0, "NE843-MIB", "ne843DpnEntryIndex"),
)
if mibBuilder.loadTexts:
    ne843DpnEntry.setStatus("current")


class _Ne843DpnEntryIndex_Type(Integer32):
    """Custom type ne843DpnEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ne843DpnEntryIndex_Type.__name__ = "Integer32"
_Ne843DpnEntryIndex_Object = MibTableColumn
ne843DpnEntryIndex = _Ne843DpnEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 1),
    _Ne843DpnEntryIndex_Type()
)
ne843DpnEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryIndex.setStatus("current")
_Ne843DpnEntryIde_Type = DisplayString
_Ne843DpnEntryIde_Object = MibTableColumn
ne843DpnEntryIde = _Ne843DpnEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 2),
    _Ne843DpnEntryIde_Type()
)
ne843DpnEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryIde.setStatus("current")
_Ne843DpnEntryDes_Type = DisplayString
_Ne843DpnEntryDes_Object = MibTableColumn
ne843DpnEntryDes = _Ne843DpnEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 3),
    _Ne843DpnEntryDes_Type()
)
ne843DpnEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryDes.setStatus("current")
_Ne843DpnEntryAdc_Type = Integer32
_Ne843DpnEntryAdc_Object = MibTableColumn
ne843DpnEntryAdc = _Ne843DpnEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 4),
    _Ne843DpnEntryAdc_Type()
)
ne843DpnEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843DpnEntryAdc.setUnits("Amps")
_Ne843DpnEntryVdc_Type = Integer32
_Ne843DpnEntryVdc_Object = MibTableColumn
ne843DpnEntryVdc = _Ne843DpnEntryVdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 5),
    _Ne843DpnEntryVdc_Type()
)
ne843DpnEntryVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryVdc.setStatus("current")
if mibBuilder.loadTexts:
    ne843DpnEntryVdc.setUnits("mV")
_Ne843DpnEntryStt_Type = DisplayString
_Ne843DpnEntryStt_Object = MibTableColumn
ne843DpnEntryStt = _Ne843DpnEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 6),
    _Ne843DpnEntryStt_Type()
)
ne843DpnEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryStt.setStatus("current")


class _Ne843DpnEntryPid_Type(Integer32):
    """Custom type ne843DpnEntryPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ne843DpnEntryPid_Type.__name__ = "Integer32"
_Ne843DpnEntryPid_Object = MibTableColumn
ne843DpnEntryPid = _Ne843DpnEntryPid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 7),
    _Ne843DpnEntryPid_Type()
)
ne843DpnEntryPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryPid.setStatus("current")


class _Ne843DpnEntryEna_Type(Integer32):
    """Custom type ne843DpnEntryEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843DpnEntryEna_Type.__name__ = "Integer32"
_Ne843DpnEntryEna_Object = MibTableColumn
ne843DpnEntryEna = _Ne843DpnEntryEna_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 8),
    _Ne843DpnEntryEna_Type()
)
ne843DpnEntryEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryEna.setStatus("current")


class _Ne843DpnEntryOld_Type(Integer32):
    """Custom type ne843DpnEntryOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Ne843DpnEntryOld_Type.__name__ = "Integer32"
_Ne843DpnEntryOld_Object = MibTableColumn
ne843DpnEntryOld = _Ne843DpnEntryOld_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 9),
    _Ne843DpnEntryOld_Type()
)
ne843DpnEntryOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryOld.setStatus("current")
if mibBuilder.loadTexts:
    ne843DpnEntryOld.setUnits("Seconds")


class _Ne843DpnEntryOlt_Type(Integer32):
    """Custom type ne843DpnEntryOlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_Ne843DpnEntryOlt_Type.__name__ = "Integer32"
_Ne843DpnEntryOlt_Object = MibTableColumn
ne843DpnEntryOlt = _Ne843DpnEntryOlt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 10),
    _Ne843DpnEntryOlt_Type()
)
ne843DpnEntryOlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryOlt.setStatus("current")
if mibBuilder.loadTexts:
    ne843DpnEntryOlt.setUnits("amps")


class _Ne843DpnEntryOlr_Type(Integer32):
    """Custom type ne843DpnEntryOlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ne843DpnEntryOlr_Type.__name__ = "Integer32"
_Ne843DpnEntryOlr_Object = MibTableColumn
ne843DpnEntryOlr = _Ne843DpnEntryOlr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 11),
    _Ne843DpnEntryOlr_Type()
)
ne843DpnEntryOlr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryOlr.setStatus("current")


class _Ne843DpnEntryPlt_Type(Integer32):
    """Custom type ne843DpnEntryPlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40000, 60000),
    )


_Ne843DpnEntryPlt_Type.__name__ = "Integer32"
_Ne843DpnEntryPlt_Object = MibTableColumn
ne843DpnEntryPlt = _Ne843DpnEntryPlt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 12),
    _Ne843DpnEntryPlt_Type()
)
ne843DpnEntryPlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryPlt.setStatus("current")
if mibBuilder.loadTexts:
    ne843DpnEntryPlt.setUnits("mV")


class _Ne843DpnEntryCct_Type(Integer32):
    """Custom type ne843DpnEntryCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ne843DpnEntryCct_Type.__name__ = "Integer32"
_Ne843DpnEntryCct_Object = MibTableColumn
ne843DpnEntryCct = _Ne843DpnEntryCct_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 13),
    _Ne843DpnEntryCct_Type()
)
ne843DpnEntryCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ne843DpnEntryCct.setStatus("current")
_Ne843DpnEntryVlv_Type = DisplayString
_Ne843DpnEntryVlv_Object = MibTableColumn
ne843DpnEntryVlv = _Ne843DpnEntryVlv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 14),
    _Ne843DpnEntryVlv_Type()
)
ne843DpnEntryVlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryVlv.setStatus("current")
_Ne843DpnEntryOvl_Type = DisplayString
_Ne843DpnEntryOvl_Object = MibTableColumn
ne843DpnEntryOvl = _Ne843DpnEntryOvl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 15),
    _Ne843DpnEntryOvl_Type()
)
ne843DpnEntryOvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryOvl.setStatus("current")
_Ne843DpnEntryFaja_Type = DisplayString
_Ne843DpnEntryFaja_Object = MibTableColumn
ne843DpnEntryFaja = _Ne843DpnEntryFaja_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 16),
    _Ne843DpnEntryFaja_Type()
)
ne843DpnEntryFaja.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryFaja.setStatus("current")
_Ne843DpnEntryFajb_Type = DisplayString
_Ne843DpnEntryFajb_Object = MibTableColumn
ne843DpnEntryFajb = _Ne843DpnEntryFajb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 51, 1, 17),
    _Ne843DpnEntryFajb_Type()
)
ne843DpnEntryFajb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ne843DpnEntryFajb.setStatus("current")
_Prototypes_ObjectIdentity = ObjectIdentity
prototypes = _Prototypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 2)
)

# Managed Objects groups


# Notification objects

ne843TrapDc1Amj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 1)
)
ne843TrapDc1Amj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Amj.setStatus(
        "current"
    )

ne843TrapDc1Vsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 2)
)
ne843TrapDc1Vsf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Vsf.setStatus(
        "current"
    )

ne843TrapDc1Osa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 3)
)
ne843TrapDc1Osa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Osa.setStatus(
        "current"
    )

ne843TrapDc1Zid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 4)
)
ne843TrapDc1Zid.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Zid.setStatus(
        "current"
    )

ne843TrapDc1Tpa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 5)
)
ne843TrapDc1Tpa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Tpa.setStatus(
        "current"
    )

ne843TrapDc1Vmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 6)
)
ne843TrapDc1Vmf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Vmf.setStatus(
        "current"
    )

ne843TrapDc1Cma = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 7)
)
ne843TrapDc1Cma.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Cma.setStatus(
        "current"
    )

ne843TrapDc1Mcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 8)
)
ne843TrapDc1Mcm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Mcm.setStatus(
        "current"
    )

ne843TrapDc1Epo = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 9)
)
ne843TrapDc1Epo.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Epo.setStatus(
        "current"
    )

ne843TrapDc1Icr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 10)
)
ne843TrapDc1Icr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Icr.setStatus(
        "current"
    )

ne843TrapDc1Rfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 11)
)
ne843TrapDc1Rfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rfa.setStatus(
        "current"
    )

ne843TrapDc1Acf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 12)
)
ne843TrapDc1Acf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Acf.setStatus(
        "current"
    )

ne843TrapDc1Man = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 13)
)
ne843TrapDc1Man.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Man.setStatus(
        "current"
    )

ne843TrapDc1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 14)
)
ne843TrapDc1Did.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Did.setStatus(
        "current"
    )

ne843TrapDc1Clm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 15)
)
ne843TrapDc1Clm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Clm.setStatus(
        "current"
    )

ne843TrapDc1Rfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 16)
)
ne843TrapDc1Rfn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rfn.setStatus(
        "current"
    )

ne843TrapDc1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 17)
)
ne843TrapDc1Vla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Vla.setStatus(
        "current"
    )

ne843TrapDc1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 18)
)
ne843TrapDc1Mfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Mfa.setStatus(
        "current"
    )

ne843TrapDc1Rtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 19)
)
ne843TrapDc1Rtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rtl.setStatus(
        "current"
    )

ne843TrapDc1Rrtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 20)
)
ne843TrapDc1Rrtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rrtl.setStatus(
        "current"
    )

ne843TrapDc1Rls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 21)
)
ne843TrapDc1Rls.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rls.setStatus(
        "current"
    )

ne843TrapDc1Mman = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 22)
)
ne843TrapDc1Mman.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Mman.setStatus(
        "current"
    )

ne843TrapDc1Macf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 23)
)
ne843TrapDc1Macf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Macf.setStatus(
        "current"
    )

ne843TrapDc1Bda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 24)
)
ne843TrapDc1Bda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Bda.setStatus(
        "current"
    )

ne843TrapDc1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 25)
)
ne843TrapDc1Hva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Hva.setStatus(
        "current"
    )

ne843TrapDc1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 26)
)
ne843TrapDc1Hfv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Hfv.setStatus(
        "current"
    )

ne843TrapPs1Epr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 27)
)
ne843TrapPs1Epr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Epr.setStatus(
        "current"
    )

ne843TrapPs1Pfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 28)
)
ne843TrapPs1Pfd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Pfd.setStatus(
        "current"
    )

ne843TrapPs1Exl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 29)
)
ne843TrapPs1Exl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Exl.setStatus(
        "current"
    )

ne843TrapPs1Bbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 30)
)
ne843TrapPs1Bbl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Bbl.setStatus(
        "current"
    )

ne843TrapPs1Clc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 31)
)
ne843TrapPs1Clc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Clc.setStatus(
        "current"
    )

ne843TrapPs1Stf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 32)
)
ne843TrapPs1Stf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Stf.setStatus(
        "current"
    )

ne843TrapPs1Pgi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 33)
)
ne843TrapPs1Pgi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Pgi.setStatus(
        "current"
    )

ne843TrapPs1Cch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 34)
)
ne843TrapPs1Cch.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Cch.setStatus(
        "current"
    )

ne843TrapPs1Hcl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 35)
)
ne843TrapPs1Hcl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Hcl.setStatus(
        "current"
    )

ne843TrapPs1Ax1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 36)
)
ne843TrapPs1Ax1.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax1.setStatus(
        "current"
    )

ne843TrapPs1Ax2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 37)
)
ne843TrapPs1Ax2.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax2.setStatus(
        "current"
    )

ne843TrapPs1Ax3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 38)
)
ne843TrapPs1Ax3.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax3.setStatus(
        "current"
    )

ne843TrapPs1Ax4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 39)
)
ne843TrapPs1Ax4.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax4.setStatus(
        "current"
    )

ne843TrapPs1Ax5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 40)
)
ne843TrapPs1Ax5.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax5.setStatus(
        "current"
    )

ne843TrapPs1Ax6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 41)
)
ne843TrapPs1Ax6.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax6.setStatus(
        "current"
    )

ne843TrapPs1Fan24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 42)
)
ne843TrapPs1Fan24.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Fan24.setStatus(
        "current"
    )

ne843TrapPs1Fan48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 43)
)
ne843TrapPs1Fan48.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Fan48.setStatus(
        "current"
    )

ne843TrapPs1Faj24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 44)
)
ne843TrapPs1Faj24.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Faj24.setStatus(
        "current"
    )

ne843TrapPs1Faj48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 45)
)
ne843TrapPs1Faj48.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Faj48.setStatus(
        "current"
    )

ne843TrapAt1Ata = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 46)
)
ne843TrapAt1Ata.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapAt1Ata.setStatus(
        "current"
    )

ne843TrapAt1Atb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 47)
)
ne843TrapAt1Atb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapAt1Atb.setStatus(
        "current"
    )

ne843TrapCp1Cfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 48)
)
ne843TrapCp1Cfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Cfa.setStatus(
        "current"
    )

ne843TrapCp1Cfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 49)
)
ne843TrapCp1Cfn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Cfn.setStatus(
        "current"
    )

ne843TrapCp1Cfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 50)
)
ne843TrapCp1Cfj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Cfj.setStatus(
        "current"
    )

ne843TrapCp1Dfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 51)
)
ne843TrapCp1Dfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Dfa.setStatus(
        "current"
    )

ne843TrapCp1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 52)
)
ne843TrapCp1Did.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Did.setStatus(
        "current"
    )

ne843TrapCp1Icc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 53)
)
ne843TrapCp1Icc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Icc.setStatus(
        "current"
    )

ne843TrapCp1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 54)
)
ne843TrapCp1Mfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Mfa.setStatus(
        "current"
    )

ne843TrapCp1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 55)
)
ne843TrapCp1Hva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Hva.setStatus(
        "current"
    )

ne843TrapCp1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 56)
)
ne843TrapCp1Hfv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Hfv.setStatus(
        "current"
    )

ne843TrapCp1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 57)
)
ne843TrapCp1Vla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Vla.setStatus(
        "current"
    )

ne843TrapCp1Rl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 58)
)
ne843TrapCp1Rl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Rl.setStatus(
        "current"
    )

ne843TrapBr1Bta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 59)
)
ne843TrapBr1Bta.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Bta.setStatus(
        "current"
    )

ne843TrapBr1Bfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 60)
)
ne843TrapBr1Bfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Bfa.setStatus(
        "current"
    )

ne843TrapBr1Scda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 61)
)
ne843TrapBr1Scda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Scda.setStatus(
        "current"
    )

ne843TrapBr1Isda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 62)
)
ne843TrapBr1Isda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Isda.setStatus(
        "current"
    )

ne843TrapBr1Mdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 63)
)
ne843TrapBr1Mdp.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Mdp.setStatus(
        "current"
    )

ne843TrapBr1Mzd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 64)
)
ne843TrapBr1Mzd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Mzd.setStatus(
        "current"
    )

ne843TrapBr1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 65)
)
ne843TrapBr1Btha.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Btha.setStatus(
        "current"
    )

ne843TrapCn1Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 66)
)
ne843TrapCn1Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn1Cno.setStatus(
        "current"
    )

ne843TrapCn1Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 67)
)
ne843TrapCn1Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn1Cnf.setStatus(
        "current"
    )

ne843TrapCn2Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 68)
)
ne843TrapCn2Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn2Cno.setStatus(
        "current"
    )

ne843TrapCn2Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 69)
)
ne843TrapCn2Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn2Cnf.setStatus(
        "current"
    )

ne843TrapCn3Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 70)
)
ne843TrapCn3Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn3Cno.setStatus(
        "current"
    )

ne843TrapCn3Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 71)
)
ne843TrapCn3Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn3Cnf.setStatus(
        "current"
    )

ne843TrapCn4Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 72)
)
ne843TrapCn4Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn4Cno.setStatus(
        "current"
    )

ne843TrapCn4Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 73)
)
ne843TrapCn4Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCn4Cnf.setStatus(
        "current"
    )

ne843TrapCm1Cof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 74)
)
ne843TrapCm1Cof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCm1Cof.setStatus(
        "current"
    )

ne843TrapCm1Cor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 75)
)
ne843TrapCm1Cor.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCm1Cor.setStatus(
        "current"
    )

ne843TrapCm1Nnc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 76)
)
ne843TrapCm1Nnc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCm1Nnc.setStatus(
        "current"
    )

ne843TrapPo1Por = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 77)
)
ne843TrapPo1Por.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPo1Por.setStatus(
        "current"
    )

ne843TrapRp1Rf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 78)
)
ne843TrapRp1Rf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rf.setStatus(
        "current"
    )

ne843TrapRp1Rpff = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 79)
)
ne843TrapRp1Rpff.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rpff.setStatus(
        "current"
    )

ne843TrapRp1Rprl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 80)
)
ne843TrapRp1Rprl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rprl.setStatus(
        "current"
    )

ne843TrapRp1Rpfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 81)
)
ne843TrapRp1Rpfj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rpfj.setStatus(
        "current"
    )

ne843TrapRp1Rpxj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 82)
)
ne843TrapRp1Rpxj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rpxj.setStatus(
        "current"
    )

ne843TrapRp1Rpxn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 83)
)
ne843TrapRp1Rpxn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rpxn.setStatus(
        "current"
    )

ne843TrapRp1Rcdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 84)
)
ne843TrapRp1Rcdp.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapRp1Rcdp.setStatus(
        "current"
    )

ne843TrapUserDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 85)
)
ne843TrapUserDefined.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapUserDefined.setStatus(
        "current"
    )

ne843TrapDc1Emd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 86)
)
ne843TrapDc1Emd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Emd.setStatus(
        "current"
    )

ne843TrapDc1Pfs = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 87)
)
ne843TrapDc1Pfs.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Pfs.setStatus(
        "current"
    )

ne843TrapDc1Rif = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 88)
)
ne843TrapDc1Rif.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Rif.setStatus(
        "current"
    )

ne843TrapDc1Lsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 89)
)
ne843TrapDc1Lsf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Lsf.setStatus(
        "current"
    )

ne843TrapPs1Ax7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 90)
)
ne843TrapPs1Ax7.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax7.setStatus(
        "current"
    )

ne843TrapPs1Ax8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 91)
)
ne843TrapPs1Ax8.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax8.setStatus(
        "current"
    )

ne843TrapPs1Ax9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 92)
)
ne843TrapPs1Ax9.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax9.setStatus(
        "current"
    )

ne843TrapPs1Ax10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 93)
)
ne843TrapPs1Ax10.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax10.setStatus(
        "current"
    )

ne843TrapPs1Ax11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 94)
)
ne843TrapPs1Ax11.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax11.setStatus(
        "current"
    )

ne843TrapPs1Ax12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 95)
)
ne843TrapPs1Ax12.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Ax12.setStatus(
        "current"
    )

ne843TrapBr1Btla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 96)
)
ne843TrapBr1Btla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Btla.setStatus(
        "current"
    )

ne843TrapBr1Btvh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 97)
)
ne843TrapBr1Btvh.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Btvh.setStatus(
        "current"
    )

ne843TrapBr1Btvl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 98)
)
ne843TrapBr1Btvl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Btvl.setStatus(
        "current"
    )

ne843TrapGn1Gnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 99)
)
ne843TrapGn1Gnr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapGn1Gnr.setStatus(
        "current"
    )

ne843TrapGn1Gnm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 100)
)
ne843TrapGn1Gnm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapGn1Gnm.setStatus(
        "current"
    )

ne843TrapGn1Gnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 101)
)
ne843TrapGn1Gnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapGn1Gnf.setStatus(
        "current"
    )

ne843TrapPs1Amtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 102)
)
ne843TrapPs1Amtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Amtl.setStatus(
        "current"
    )

ne843TrapPs1Amth = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 103)
)
ne843TrapPs1Amth.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Amth.setStatus(
        "current"
    )

ne843TrapAco1Aac = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 104)
)
ne843TrapAco1Aac.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapAco1Aac.setStatus(
        "current"
    )

ne843TrapBr1Rba = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 105)
)
ne843TrapBr1Rba.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapBr1Rba.setStatus(
        "current"
    )

ne843TrapCp1Cin = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 106)
)
ne843TrapCp1Cin.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapCp1Cin.setStatus(
        "current"
    )

ne843TrapDc1Bof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 107)
)
ne843TrapDc1Bof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Bof.setStatus(
        "current"
    )

ne843TrapDc1Sof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 108)
)
ne843TrapDc1Sof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Sof.setStatus(
        "current"
    )

ne843TrapDc1Der = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 109)
)
ne843TrapDc1Der.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Der.setStatus(
        "current"
    )

ne843TrapGn1Gns = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 110)
)
ne843TrapGn1Gns.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapGn1Gns.setStatus(
        "current"
    )

ne843TrapIvp1Ilvi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 111)
)
ne843TrapIvp1Ilvi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ilvi.setStatus(
        "current"
    )

ne843TrapIvp1Ihvi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 112)
)
ne843TrapIvp1Ihvi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ihvi.setStatus(
        "current"
    )

ne843TrapIvp1Ita = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 113)
)
ne843TrapIvp1Ita.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ita.setStatus(
        "current"
    )

ne843TrapIvp1If = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 114)
)
ne843TrapIvp1If.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1If.setStatus(
        "current"
    )

ne843TrapIvp1Ilv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 115)
)
ne843TrapIvp1Ilv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ilv.setStatus(
        "current"
    )

ne843TrapIvp1Ifa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 116)
)
ne843TrapIvp1Ifa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ifa.setStatus(
        "current"
    )

ne843TrapIvp1Ihv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 117)
)
ne843TrapIvp1Ihv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ihv.setStatus(
        "current"
    )

ne843TrapIvp1Ida = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 118)
)
ne843TrapIvp1Ida.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Ida.setStatus(
        "current"
    )

ne843TrapIvp1Iof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 119)
)
ne843TrapIvp1Iof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Iof.setStatus(
        "current"
    )

ne843TrapIvp1Idid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 120)
)
ne843TrapIvp1Idid.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Idid.setStatus(
        "current"
    )

ne843TrapIvp1Iirm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 121)
)
ne843TrapIvp1Iirm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Iirm.setStatus(
        "current"
    )

ne843TrapIvp1Iipk = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 122)
)
ne843TrapIvp1Iipk.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Iipk.setStatus(
        "current"
    )

ne843TrapIvp1Icf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 123)
)
ne843TrapIvp1Icf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Icf.setStatus(
        "current"
    )

ne843TrapIvp1Mif = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 124)
)
ne843TrapIvp1Mif.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Mif.setStatus(
        "current"
    )

ne843TrapIvp1Irls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 125)
)
ne843TrapIvp1Irls.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Irls.setStatus(
        "current"
    )

ne843TrapDc1Pmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 126)
)
ne843TrapDc1Pmf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Pmf.setStatus(
        "current"
    )

ne843TrapPs1Crt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 127)
)
ne843TrapPs1Crt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapPs1Crt.setStatus(
        "current"
    )

ne843TrapIvp1Milv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 128)
)
ne843TrapIvp1Milv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapIvp1Milv.setStatus(
        "current"
    )

ne843TrapDc1Faja = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 129)
)
ne843TrapDc1Faja.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Faja.setStatus(
        "current"
    )

ne843TrapDc1Buht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 130)
)
ne843TrapDc1Buht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Buht.setStatus(
        "current"
    )

ne843TrapDc1Buvht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 131)
)
ne843TrapDc1Buvht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Buvht.setStatus(
        "current"
    )

ne843TrapDc1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 132)
)
ne843TrapDc1Btha.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Btha.setStatus(
        "current"
    )

ne843TrapDc1Btvh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 133)
)
ne843TrapDc1Btvh.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Btvh.setStatus(
        "current"
    )

ne843TrapDc1Btla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 134)
)
ne843TrapDc1Btla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Btla.setStatus(
        "current"
    )

ne843TrapDc1Btvl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 135)
)
ne843TrapDc1Btvl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Btvl.setStatus(
        "current"
    )

ne843TrapDc1Laht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 136)
)
ne843TrapDc1Laht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Laht.setStatus(
        "current"
    )

ne843TrapDc1Lalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 137)
)
ne843TrapDc1Lalt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Lalt.setStatus(
        "current"
    )

ne843TrapDc1Raht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 138)
)
ne843TrapDc1Raht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Raht.setStatus(
        "current"
    )

ne843TrapDc1Ravht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 139)
)
ne843TrapDc1Ravht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Ravht.setStatus(
        "current"
    )

ne843TrapDc1Ralt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 140)
)
ne843TrapDc1Ralt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Ralt.setStatus(
        "current"
    )

ne843TrapDc1Vlva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 141)
)
ne843TrapDc1Vlva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Vlva.setStatus(
        "current"
    )

ne843TrapDc1Vlvb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 142)
)
ne843TrapDc1Vlvb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Vlvb.setStatus(
        "current"
    )

ne843TrapDc1Ovla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 143)
)
ne843TrapDc1Ovla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Ovla.setStatus(
        "current"
    )

ne843TrapDc1Ovlb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 144)
)
ne843TrapDc1Ovlb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Ovlb.setStatus(
        "current"
    )

ne843TrapDc1Pcaux = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 145)
)
ne843TrapDc1Pcaux.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Pcaux.setStatus(
        "current"
    )

ne843TrapDc1Slot = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 146)
)
ne843TrapDc1Slot.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Slot.setStatus(
        "current"
    )

ne843TrapDc1Fajb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 147)
)
ne843TrapDc1Fajb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Fajb.setStatus(
        "current"
    )

ne843TrapDc1Smw = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 148)
)
ne843TrapDc1Smw.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Smw.setStatus(
        "current"
    )

ne843TrapDc1Cca = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 35, 149)
)
ne843TrapDc1Cca.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843TrapDc1Cca.setStatus(
        "current"
    )

ne843RetireDc1Amj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 1)
)
ne843RetireDc1Amj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Amj.setStatus(
        "current"
    )

ne843RetireDc1Vsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 2)
)
ne843RetireDc1Vsf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Vsf.setStatus(
        "current"
    )

ne843RetireDc1Osa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 3)
)
ne843RetireDc1Osa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Osa.setStatus(
        "current"
    )

ne843RetireDc1Zid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 4)
)
ne843RetireDc1Zid.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Zid.setStatus(
        "current"
    )

ne843RetireDc1Tpa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 5)
)
ne843RetireDc1Tpa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Tpa.setStatus(
        "current"
    )

ne843RetireDc1Vmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 6)
)
ne843RetireDc1Vmf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Vmf.setStatus(
        "current"
    )

ne843RetireDc1Cma = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 7)
)
ne843RetireDc1Cma.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Cma.setStatus(
        "current"
    )

ne843RetireDc1Mcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 8)
)
ne843RetireDc1Mcm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Mcm.setStatus(
        "current"
    )

ne843RetireDc1Epo = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 9)
)
ne843RetireDc1Epo.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Epo.setStatus(
        "current"
    )

ne843RetireDc1Icr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 10)
)
ne843RetireDc1Icr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Icr.setStatus(
        "current"
    )

ne843RetireDc1Rfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 11)
)
ne843RetireDc1Rfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rfa.setStatus(
        "current"
    )

ne843RetireDc1Acf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 12)
)
ne843RetireDc1Acf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Acf.setStatus(
        "current"
    )

ne843RetireDc1Man = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 13)
)
ne843RetireDc1Man.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Man.setStatus(
        "current"
    )

ne843RetireDc1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 14)
)
ne843RetireDc1Did.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Did.setStatus(
        "current"
    )

ne843RetireDc1Clm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 15)
)
ne843RetireDc1Clm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Clm.setStatus(
        "current"
    )

ne843RetireDc1Rfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 16)
)
ne843RetireDc1Rfn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rfn.setStatus(
        "current"
    )

ne843RetireDc1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 17)
)
ne843RetireDc1Vla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Vla.setStatus(
        "current"
    )

ne843RetireDc1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 18)
)
ne843RetireDc1Mfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Mfa.setStatus(
        "current"
    )

ne843RetireDc1Rtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 19)
)
ne843RetireDc1Rtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rtl.setStatus(
        "current"
    )

ne843RetireDc1Rrtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 20)
)
ne843RetireDc1Rrtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rrtl.setStatus(
        "current"
    )

ne843RetireDc1Rls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 21)
)
ne843RetireDc1Rls.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rls.setStatus(
        "current"
    )

ne843RetireDc1Mman = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 22)
)
ne843RetireDc1Mman.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Mman.setStatus(
        "current"
    )

ne843RetireDc1Macf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 23)
)
ne843RetireDc1Macf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Macf.setStatus(
        "current"
    )

ne843RetireDc1Bda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 24)
)
ne843RetireDc1Bda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Bda.setStatus(
        "current"
    )

ne843RetireDc1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 25)
)
ne843RetireDc1Hva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Hva.setStatus(
        "current"
    )

ne843RetireDc1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 26)
)
ne843RetireDc1Hfv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Hfv.setStatus(
        "current"
    )

ne843RetirePs1Epr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 27)
)
ne843RetirePs1Epr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Epr.setStatus(
        "current"
    )

ne843RetirePs1Pfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 28)
)
ne843RetirePs1Pfd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Pfd.setStatus(
        "current"
    )

ne843RetirePs1Exl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 29)
)
ne843RetirePs1Exl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Exl.setStatus(
        "current"
    )

ne843RetirePs1Bbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 30)
)
ne843RetirePs1Bbl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Bbl.setStatus(
        "current"
    )

ne843RetirePs1Clc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 31)
)
ne843RetirePs1Clc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Clc.setStatus(
        "current"
    )

ne843RetirePs1Stf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 32)
)
ne843RetirePs1Stf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Stf.setStatus(
        "current"
    )

ne843RetirePs1Pgi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 33)
)
ne843RetirePs1Pgi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Pgi.setStatus(
        "current"
    )

ne843RetirePs1Cch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 34)
)
ne843RetirePs1Cch.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Cch.setStatus(
        "current"
    )

ne843RetirePs1Hcl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 35)
)
ne843RetirePs1Hcl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Hcl.setStatus(
        "current"
    )

ne843RetirePs1Ax1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 36)
)
ne843RetirePs1Ax1.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax1.setStatus(
        "current"
    )

ne843RetirePs1Ax2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 37)
)
ne843RetirePs1Ax2.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax2.setStatus(
        "current"
    )

ne843RetirePs1Ax3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 38)
)
ne843RetirePs1Ax3.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax3.setStatus(
        "current"
    )

ne843RetirePs1Ax4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 39)
)
ne843RetirePs1Ax4.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax4.setStatus(
        "current"
    )

ne843RetirePs1Ax5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 40)
)
ne843RetirePs1Ax5.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax5.setStatus(
        "current"
    )

ne843RetirePs1Ax6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 41)
)
ne843RetirePs1Ax6.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax6.setStatus(
        "current"
    )

ne843RetirePs1Fan24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 42)
)
ne843RetirePs1Fan24.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Fan24.setStatus(
        "current"
    )

ne843RetirePs1Fan48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 43)
)
ne843RetirePs1Fan48.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Fan48.setStatus(
        "current"
    )

ne843RetirePs1Faj24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 44)
)
ne843RetirePs1Faj24.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Faj24.setStatus(
        "current"
    )

ne843RetirePs1Faj48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 45)
)
ne843RetirePs1Faj48.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Faj48.setStatus(
        "current"
    )

ne843RetireAt1Ata = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 46)
)
ne843RetireAt1Ata.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireAt1Ata.setStatus(
        "current"
    )

ne843RetireAt1Atb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 47)
)
ne843RetireAt1Atb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireAt1Atb.setStatus(
        "current"
    )

ne843RetireCp1Cfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 48)
)
ne843RetireCp1Cfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Cfa.setStatus(
        "current"
    )

ne843RetireCp1Cfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 49)
)
ne843RetireCp1Cfn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Cfn.setStatus(
        "current"
    )

ne843RetireCp1Cfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 50)
)
ne843RetireCp1Cfj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Cfj.setStatus(
        "current"
    )

ne843RetireCp1Dfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 51)
)
ne843RetireCp1Dfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Dfa.setStatus(
        "current"
    )

ne843RetireCp1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 52)
)
ne843RetireCp1Did.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Did.setStatus(
        "current"
    )

ne843RetireCp1Icc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 53)
)
ne843RetireCp1Icc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Icc.setStatus(
        "current"
    )

ne843RetireCp1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 54)
)
ne843RetireCp1Mfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Mfa.setStatus(
        "current"
    )

ne843RetireCp1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 55)
)
ne843RetireCp1Hva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Hva.setStatus(
        "current"
    )

ne843RetireCp1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 56)
)
ne843RetireCp1Hfv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Hfv.setStatus(
        "current"
    )

ne843RetireCp1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 57)
)
ne843RetireCp1Vla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Vla.setStatus(
        "current"
    )

ne843RetireCp1Rl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 58)
)
ne843RetireCp1Rl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Rl.setStatus(
        "current"
    )

ne843RetireBr1Bta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 59)
)
ne843RetireBr1Bta.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Bta.setStatus(
        "current"
    )

ne843RetireBr1Bfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 60)
)
ne843RetireBr1Bfa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Bfa.setStatus(
        "current"
    )

ne843RetireBr1Scda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 61)
)
ne843RetireBr1Scda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Scda.setStatus(
        "current"
    )

ne843RetireBr1Isda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 62)
)
ne843RetireBr1Isda.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Isda.setStatus(
        "current"
    )

ne843RetireBr1Mdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 63)
)
ne843RetireBr1Mdp.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Mdp.setStatus(
        "current"
    )

ne843RetireBr1Mzd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 64)
)
ne843RetireBr1Mzd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Mzd.setStatus(
        "current"
    )

ne843RetireBr1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 65)
)
ne843RetireBr1Btha.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Btha.setStatus(
        "current"
    )

ne843RetireCn1Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 66)
)
ne843RetireCn1Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn1Cno.setStatus(
        "current"
    )

ne843RetireCn1Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 67)
)
ne843RetireCn1Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn1Cnf.setStatus(
        "current"
    )

ne843RetireCn2Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 68)
)
ne843RetireCn2Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn2Cno.setStatus(
        "current"
    )

ne843RetireCn2Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 69)
)
ne843RetireCn2Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn2Cnf.setStatus(
        "current"
    )

ne843RetireCn3Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 70)
)
ne843RetireCn3Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn3Cno.setStatus(
        "current"
    )

ne843RetireCn3Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 71)
)
ne843RetireCn3Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn3Cnf.setStatus(
        "current"
    )

ne843RetireCn4Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 72)
)
ne843RetireCn4Cno.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn4Cno.setStatus(
        "current"
    )

ne843RetireCn4Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 73)
)
ne843RetireCn4Cnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCn4Cnf.setStatus(
        "current"
    )

ne843RetireCm1Cof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 74)
)
ne843RetireCm1Cof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCm1Cof.setStatus(
        "current"
    )

ne843RetireCm1Cor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 75)
)
ne843RetireCm1Cor.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCm1Cor.setStatus(
        "current"
    )

ne843RetireCm1Nnc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 76)
)
ne843RetireCm1Nnc.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCm1Nnc.setStatus(
        "current"
    )

ne843RetirePo1Por = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 77)
)
ne843RetirePo1Por.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePo1Por.setStatus(
        "current"
    )

ne843RetireRp1Rf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 78)
)
ne843RetireRp1Rf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rf.setStatus(
        "current"
    )

ne843RetireRp1Rpff = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 79)
)
ne843RetireRp1Rpff.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rpff.setStatus(
        "current"
    )

ne843RetireRp1Rprl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 80)
)
ne843RetireRp1Rprl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rprl.setStatus(
        "current"
    )

ne843RetireRp1Rpfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 81)
)
ne843RetireRp1Rpfj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rpfj.setStatus(
        "current"
    )

ne843RetireRp1Rpxj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 82)
)
ne843RetireRp1Rpxj.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rpxj.setStatus(
        "current"
    )

ne843RetireRp1Rpxn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 83)
)
ne843RetireRp1Rpxn.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rpxn.setStatus(
        "current"
    )

ne843RetireRp1Rcdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 84)
)
ne843RetireRp1Rcdp.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireRp1Rcdp.setStatus(
        "current"
    )

ne843RetireUserDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 85)
)
ne843RetireUserDefined.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireUserDefined.setStatus(
        "current"
    )

ne843RetireDc1Emd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 86)
)
ne843RetireDc1Emd.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Emd.setStatus(
        "current"
    )

ne843RetireDc1Pfs = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 87)
)
ne843RetireDc1Pfs.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Pfs.setStatus(
        "current"
    )

ne843RetireDc1Rif = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 88)
)
ne843RetireDc1Rif.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Rif.setStatus(
        "current"
    )

ne843RetireDc1Lsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 89)
)
ne843RetireDc1Lsf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Lsf.setStatus(
        "current"
    )

ne843RetirePs1Ax7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 90)
)
ne843RetirePs1Ax7.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax7.setStatus(
        "current"
    )

ne843RetirePs1Ax8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 91)
)
ne843RetirePs1Ax8.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax8.setStatus(
        "current"
    )

ne843RetirePs1Ax9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 92)
)
ne843RetirePs1Ax9.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax9.setStatus(
        "current"
    )

ne843RetirePs1Ax10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 93)
)
ne843RetirePs1Ax10.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax10.setStatus(
        "current"
    )

ne843RetirePs1Ax11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 94)
)
ne843RetirePs1Ax11.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax11.setStatus(
        "current"
    )

ne843RetirePs1Ax12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 95)
)
ne843RetirePs1Ax12.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Ax12.setStatus(
        "current"
    )

ne843RetireBr1Btla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 96)
)
ne843RetireBr1Btla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Btla.setStatus(
        "current"
    )

ne843RetireBr1Btvh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 97)
)
ne843RetireBr1Btvh.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Btvh.setStatus(
        "current"
    )

ne843RetireBr1Btvl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 98)
)
ne843RetireBr1Btvl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Btvl.setStatus(
        "current"
    )

ne843RetireGn1Gnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 99)
)
ne843RetireGn1Gnr.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireGn1Gnr.setStatus(
        "current"
    )

ne843RetireGn1Gnm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 100)
)
ne843RetireGn1Gnm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireGn1Gnm.setStatus(
        "current"
    )

ne843RetireGn1Gnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 101)
)
ne843RetireGn1Gnf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireGn1Gnf.setStatus(
        "current"
    )

ne843RetirePs1Amtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 102)
)
ne843RetirePs1Amtl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Amtl.setStatus(
        "current"
    )

ne843RetirePs1Amth = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 103)
)
ne843RetirePs1Amth.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Amth.setStatus(
        "current"
    )

ne843RetireAco1Aac = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 104)
)
ne843RetireAco1Aac.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireAco1Aac.setStatus(
        "current"
    )

ne843RetireBr1Rba = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 105)
)
ne843RetireBr1Rba.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireBr1Rba.setStatus(
        "current"
    )

ne843RetireCp1Cin = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 106)
)
ne843RetireCp1Cin.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireCp1Cin.setStatus(
        "current"
    )

ne843RetireDc1Bof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 107)
)
ne843RetireDc1Bof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Bof.setStatus(
        "current"
    )

ne843RetireDc1Sof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 108)
)
ne843RetireDc1Sof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Sof.setStatus(
        "current"
    )

ne843RetireDc1Der = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 109)
)
ne843RetireDc1Der.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Der.setStatus(
        "current"
    )

ne843RetireGn1Gns = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 110)
)
ne843RetireGn1Gns.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireGn1Gns.setStatus(
        "current"
    )

ne843RetireIvp1Ilvi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 111)
)
ne843RetireIvp1Ilvi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ilvi.setStatus(
        "current"
    )

ne843RetireIvp1Ihvi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 112)
)
ne843RetireIvp1Ihvi.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ihvi.setStatus(
        "current"
    )

ne843RetireIvp1Ita = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 113)
)
ne843RetireIvp1Ita.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ita.setStatus(
        "current"
    )

ne843RetireIvp1If = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 114)
)
ne843RetireIvp1If.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1If.setStatus(
        "current"
    )

ne843RetireIvp1Ilv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 115)
)
ne843RetireIvp1Ilv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ilv.setStatus(
        "current"
    )

ne843RetireIvp1Ifa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 116)
)
ne843RetireIvp1Ifa.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ifa.setStatus(
        "current"
    )

ne843RetireIvp1Ihv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 117)
)
ne843RetireIvp1Ihv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ihv.setStatus(
        "current"
    )

ne843RetireIvp1Ida = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 118)
)
ne843RetireIvp1Ida.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Ida.setStatus(
        "current"
    )

ne843RetireIvp1Iof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 119)
)
ne843RetireIvp1Iof.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Iof.setStatus(
        "current"
    )

ne843RetireIvp1Idid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 120)
)
ne843RetireIvp1Idid.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Idid.setStatus(
        "current"
    )

ne843RetireIvp1Iirm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 121)
)
ne843RetireIvp1Iirm.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Iirm.setStatus(
        "current"
    )

ne843RetireIvp1Iipk = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 122)
)
ne843RetireIvp1Iipk.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Iipk.setStatus(
        "current"
    )

ne843RetireIvp1Icf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 123)
)
ne843RetireIvp1Icf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Icf.setStatus(
        "current"
    )

ne843RetireIvp1Mif = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 124)
)
ne843RetireIvp1Mif.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Mif.setStatus(
        "current"
    )

ne843RetireIvp1Irls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 125)
)
ne843RetireIvp1Irls.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Irls.setStatus(
        "current"
    )

ne843RetireDc1Pmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 126)
)
ne843RetireDc1Pmf.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Pmf.setStatus(
        "current"
    )

ne843RetirePs1Crt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 127)
)
ne843RetirePs1Crt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetirePs1Crt.setStatus(
        "current"
    )

ne843RetireIvp1Milv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 128)
)
ne843RetireIvp1Milv.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireIvp1Milv.setStatus(
        "current"
    )

ne843RetireDc1Faja = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 129)
)
ne843RetireDc1Faja.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Faja.setStatus(
        "current"
    )

ne843RetireDc1Buht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 130)
)
ne843RetireDc1Buht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Buht.setStatus(
        "current"
    )

ne843RetireDc1Buvht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 131)
)
ne843RetireDc1Buvht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Buvht.setStatus(
        "current"
    )

ne843RetireDc1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 132)
)
ne843RetireDc1Btha.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Btha.setStatus(
        "current"
    )

ne843RetireDc1Btvh = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 133)
)
ne843RetireDc1Btvh.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Btvh.setStatus(
        "current"
    )

ne843RetireDc1Btla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 134)
)
ne843RetireDc1Btla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Btla.setStatus(
        "current"
    )

ne843RetireDc1Btvl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 135)
)
ne843RetireDc1Btvl.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Btvl.setStatus(
        "current"
    )

ne843RetireDc1Laht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 136)
)
ne843RetireDc1Laht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Laht.setStatus(
        "current"
    )

ne843RetireDc1Lalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 137)
)
ne843RetireDc1Lalt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Lalt.setStatus(
        "current"
    )

ne843RetireDc1Raht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 138)
)
ne843RetireDc1Raht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Raht.setStatus(
        "current"
    )

ne843RetireDc1Ravht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 139)
)
ne843RetireDc1Ravht.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Ravht.setStatus(
        "current"
    )

ne843RetireDc1Ralt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 140)
)
ne843RetireDc1Ralt.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Ralt.setStatus(
        "current"
    )

ne843RetireDc1Vlva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 141)
)
ne843RetireDc1Vlva.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Vlva.setStatus(
        "current"
    )

ne843RetireDc1Vlvb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 142)
)
ne843RetireDc1Vlvb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Vlvb.setStatus(
        "current"
    )

ne843RetireDc1Ovla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 143)
)
ne843RetireDc1Ovla.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Ovla.setStatus(
        "current"
    )

ne843RetireDc1Ovlb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 144)
)
ne843RetireDc1Ovlb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Ovlb.setStatus(
        "current"
    )

ne843RetireDc1Pcaux = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 145)
)
ne843RetireDc1Pcaux.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Pcaux.setStatus(
        "current"
    )

ne843RetireDc1Slot = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 146)
)
ne843RetireDc1Slot.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Slot.setStatus(
        "current"
    )

ne843RetireDc1Fajb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 147)
)
ne843RetireDc1Fajb.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Fajb.setStatus(
        "current"
    )

ne843RetireDc1Smw = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 148)
)
ne843RetireDc1Smw.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Smw.setStatus(
        "current"
    )

ne843RetireDc1Cca = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 3, 37, 149)
)
ne843RetireDc1Cca.setObjects(
      *(("NE843-MIB", "ne843TrapDesc"),
        ("NE843-MIB", "ne843TrapSev"),
        ("NE843-MIB", "ne843TrapTime"),
        ("NE843-MIB", "ne843TrapDate"),
        ("NE843-MIB", "ne843TrapPath"))
)
if mibBuilder.loadTexts:
    ne843RetireDc1Cca.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NE843-MIB",
    **{"teps": teps,
       "controllermibs": controllermibs,
       "release": release,
       "ne843": ne843,
       "ne843Dc1": ne843Dc1,
       "ne843Dc1Ide": ne843Dc1Ide,
       "ne843Dc1Des": ne843Dc1Des,
       "ne843Dc1Typ": ne843Dc1Typ,
       "ne843Dc1Vdc": ne843Dc1Vdc,
       "ne843Dc1Adc": ne843Dc1Adc,
       "ne843Dc1Cap": ne843Dc1Cap,
       "ne843Dc1Olcap": ne843Dc1Olcap,
       "ne843Dc1Trd": ne843Dc1Trd,
       "ne843Dc1Sht": ne843Dc1Sht,
       "ne843Dc1Sha": ne843Dc1Sha,
       "ne843Dc1Stt": ne843Dc1Stt,
       "ne843Dc1Bod": ne843Dc1Bod,
       "ne843Dc1Rss": ne843Dc1Rss,
       "ne843Dc1Rsq": ne843Dc1Rsq,
       "ne843Dc1Ron": ne843Dc1Ron,
       "ne843Dc1Rot": ne843Dc1Rot,
       "ne843Dc1Nst": ne843Dc1Nst,
       "ne843Dc1Cps": ne843Dc1Cps,
       "ne843Dc1Bty": ne843Dc1Bty,
       "ne843Dc1Isd": ne843Dc1Isd,
       "ne843Dc1Rtm": ne843Dc1Rtm,
       "ne843Dc1Scap": ne843Dc1Scap,
       "ne843Dc1Mls": ne843Dc1Mls,
       "ne843Dc1Amj": ne843Dc1Amj,
       "ne843Dc1Vsf": ne843Dc1Vsf,
       "ne843Dc1Osa": ne843Dc1Osa,
       "ne843Dc1Zid": ne843Dc1Zid,
       "ne843Dc1Tpa": ne843Dc1Tpa,
       "ne843Dc1Vmf": ne843Dc1Vmf,
       "ne843Dc1Cma": ne843Dc1Cma,
       "ne843Dc1Mcm": ne843Dc1Mcm,
       "ne843Dc1Epo": ne843Dc1Epo,
       "ne843Dc1Icr": ne843Dc1Icr,
       "ne843Dc1Rfa": ne843Dc1Rfa,
       "ne843Dc1Acf": ne843Dc1Acf,
       "ne843Dc1Man": ne843Dc1Man,
       "ne843Dc1Did": ne843Dc1Did,
       "ne843Dc1Clm": ne843Dc1Clm,
       "ne843Dc1Rfn": ne843Dc1Rfn,
       "ne843Dc1Vla": ne843Dc1Vla,
       "ne843Dc1Mfa": ne843Dc1Mfa,
       "ne843Dc1Rtl": ne843Dc1Rtl,
       "ne843Dc1Rrtl": ne843Dc1Rrtl,
       "ne843Dc1Rls": ne843Dc1Rls,
       "ne843Dc1Mman": ne843Dc1Mman,
       "ne843Dc1Macf": ne843Dc1Macf,
       "ne843Dc1Bda": ne843Dc1Bda,
       "ne843Dc1Hva": ne843Dc1Hva,
       "ne843Dc1Hfv": ne843Dc1Hfv,
       "ne843Dc1Bdt": ne843Dc1Bdt,
       "ne843Dc1Ems": ne843Dc1Ems,
       "ne843Dc1Eme": ne843Dc1Eme,
       "ne843Dc1Emt": ne843Dc1Emt,
       "ne843Dc1Emo": ne843Dc1Emo,
       "ne843Dc1Poc": ne843Dc1Poc,
       "ne843Dc1Emd": ne843Dc1Emd,
       "ne843Dc1Pfs": ne843Dc1Pfs,
       "ne843Dc1Rif": ne843Dc1Rif,
       "ne843Dc1Lsf": ne843Dc1Lsf,
       "ne843Dc1Emi": ne843Dc1Emi,
       "ne843Dc1Emw": ne843Dc1Emw,
       "ne843Dc1Aseq": ne843Dc1Aseq,
       "ne843Dc1Isy": ne843Dc1Isy,
       "ne843Dc1Bofe": ne843Dc1Bofe,
       "ne843Dc1Bof": ne843Dc1Bof,
       "ne843Dc1Sof": ne843Dc1Sof,
       "ne843Dc1Der": ne843Dc1Der,
       "ne843Dc1Pmf": ne843Dc1Pmf,
       "ne843Dc1Faja": ne843Dc1Faja,
       "ne843Dc1Buht": ne843Dc1Buht,
       "ne843Dc1Buvht": ne843Dc1Buvht,
       "ne843Dc1Btha": ne843Dc1Btha,
       "ne843Dc1Btvh": ne843Dc1Btvh,
       "ne843Dc1Btla": ne843Dc1Btla,
       "ne843Dc1Btvl": ne843Dc1Btvl,
       "ne843Dc1Laht": ne843Dc1Laht,
       "ne843Dc1Lalt": ne843Dc1Lalt,
       "ne843Dc1Raht": ne843Dc1Raht,
       "ne843Dc1Ravht": ne843Dc1Ravht,
       "ne843Dc1Ralt": ne843Dc1Ralt,
       "ne843Dc1Vlva": ne843Dc1Vlva,
       "ne843Dc1Vlvb": ne843Dc1Vlvb,
       "ne843Dc1Ovla": ne843Dc1Ovla,
       "ne843Dc1Ovlb": ne843Dc1Ovlb,
       "ne843Dc1Pcaux": ne843Dc1Pcaux,
       "ne843Dc1Slot": ne843Dc1Slot,
       "ne843Dc1Bod1": ne843Dc1Bod1,
       "ne843Dc1Bdt1": ne843Dc1Bdt1,
       "ne843Dc1Poc1": ne843Dc1Poc1,
       "ne843Dc1Fajb": ne843Dc1Fajb,
       "ne843Dc1Smw": ne843Dc1Smw,
       "ne843Dc1Cca": ne843Dc1Cca,
       "ne843Ps1": ne843Ps1,
       "ne843Ps1Ide": ne843Ps1Ide,
       "ne843Ps1Des": ne843Ps1Des,
       "ne843Ps1Sid": ne843Ps1Sid,
       "ne843Ps1Sde": ne843Ps1Sde,
       "ne843Ps1Sys": ne843Ps1Sys,
       "ne843Ps1Swv": ne843Ps1Swv,
       "ne843Ps1Verw": ne843Ps1Verw,
       "ne843Ps1Verb": ne843Ps1Verb,
       "ne843Ps1Verd": ne843Ps1Verd,
       "ne843Ps1Dflt": ne843Ps1Dflt,
       "ne843Ps1Brc": ne843Ps1Brc,
       "ne843Ps1Sn": ne843Ps1Sn,
       "ne843Ps1Dat": ne843Ps1Dat,
       "ne843Ps1Dtf": ne843Ps1Dtf,
       "ne843Ps1Tim": ne843Ps1Tim,
       "ne843Ps1Tmf": ne843Ps1Tmf,
       "ne843Ps1Dls": ne843Ps1Dls,
       "ne843Ps1Lng": ne843Ps1Lng,
       "ne843Ps1Tun": ne843Ps1Tun,
       "ne843Ps1Cem": ne843Ps1Cem,
       "ne843Ps1Fpc": ne843Ps1Fpc,
       "ne843Ps1Rrf": ne843Ps1Rrf,
       "ne843Ps1Poe": ne843Ps1Poe,
       "ne843Ps1Usl": ne843Ps1Usl,
       "ne843Ps1Usr": ne843Ps1Usr,
       "ne843Ps1Ptt": ne843Ps1Ptt,
       "ne843Ps1Amt": ne843Ps1Amt,
       "ne843Ps1Fst": ne843Ps1Fst,
       "ne843Ps1Fstl": ne843Ps1Fstl,
       "ne843Ps1Fpe": ne843Ps1Fpe,
       "ne843Ps1Fpt": ne843Ps1Fpt,
       "ne843Ps1Rss": ne843Ps1Rss,
       "ne843Ps1Ast": ne843Ps1Ast,
       "ne843Ps1Dss": ne843Ps1Dss,
       "ne843Ps1Dse": ne843Ps1Dse,
       "ne843Ps1Epr": ne843Ps1Epr,
       "ne843Ps1Pfd": ne843Ps1Pfd,
       "ne843Ps1Exl": ne843Ps1Exl,
       "ne843Ps1Bbl": ne843Ps1Bbl,
       "ne843Ps1Clc": ne843Ps1Clc,
       "ne843Ps1Stf": ne843Ps1Stf,
       "ne843Ps1Pgi": ne843Ps1Pgi,
       "ne843Ps1Cch": ne843Ps1Cch,
       "ne843Ps1Hcl": ne843Ps1Hcl,
       "ne843Ps1Ax1": ne843Ps1Ax1,
       "ne843Ps1Ax2": ne843Ps1Ax2,
       "ne843Ps1Ax3": ne843Ps1Ax3,
       "ne843Ps1Ax4": ne843Ps1Ax4,
       "ne843Ps1Ax5": ne843Ps1Ax5,
       "ne843Ps1Ax6": ne843Ps1Ax6,
       "ne843Ps1Fan24": ne843Ps1Fan24,
       "ne843Ps1Fan48": ne843Ps1Fan48,
       "ne843Ps1Faj24": ne843Ps1Faj24,
       "ne843Ps1Faj48": ne843Ps1Faj48,
       "ne843Ps1Accl": ne843Ps1Accl,
       "ne843Ps1Ledl": ne843Ps1Ledl,
       "ne843Ps1Ax7": ne843Ps1Ax7,
       "ne843Ps1Ax8": ne843Ps1Ax8,
       "ne843Ps1Ax9": ne843Ps1Ax9,
       "ne843Ps1Ax10": ne843Ps1Ax10,
       "ne843Ps1Ax11": ne843Ps1Ax11,
       "ne843Ps1Ax12": ne843Ps1Ax12,
       "ne843Ps1Cid": ne843Ps1Cid,
       "ne843Ps1Lngl": ne843Ps1Lngl,
       "ne843Ps1Amtl": ne843Ps1Amtl,
       "ne843Ps1Amth": ne843Ps1Amth,
       "ne843Ps1Cc": ne843Ps1Cc,
       "ne843Ps1Clei": ne843Ps1Clei,
       "ne843Ps1Ser": ne843Ps1Ser,
       "ne843Ps1Lamt": ne843Ps1Lamt,
       "ne843Ps1Nat": ne843Ps1Nat,
       "ne843Ps1Blr": ne843Ps1Blr,
       "ne843Ps1Tzo": ne843Ps1Tzo,
       "ne843Ps1Crt": ne843Ps1Crt,
       "ne843Ps1Nhat": ne843Ps1Nhat,
       "ne843Ps1Nal": ne843Ps1Nal,
       "ne843Ps1Ncr": ne843Ps1Ncr,
       "ne843Ps1Nmj": ne843Ps1Nmj,
       "ne843Ps1Nmn": ne843Ps1Nmn,
       "ne843Ps1Nwa": ne843Ps1Nwa,
       "ne843Ps1Nre": ne843Ps1Nre,
       "ne843Ps1Ere": ne843Ps1Ere,
       "ne843At1": ne843At1,
       "ne843At1Ide": ne843At1Ide,
       "ne843At1Des": ne843At1Des,
       "ne843At1Stt": ne843At1Stt,
       "ne843At1Stg": ne843At1Stg,
       "ne843At1Lte": ne843At1Lte,
       "ne843At1Dur": ne843At1Dur,
       "ne843At1Pcr": ne843At1Pcr,
       "ne843At1Pmj": ne843At1Pmj,
       "ne843At1Pmn": ne843At1Pmn,
       "ne843At1R1": ne843At1R1,
       "ne843At1R2": ne843At1R2,
       "ne843At1R3": ne843At1R3,
       "ne843At1R4": ne843At1R4,
       "ne843At1R5": ne843At1R5,
       "ne843At1R6": ne843At1R6,
       "ne843At1R7": ne843At1R7,
       "ne843At1Ets": ne843At1Ets,
       "ne843At1Ems": ne843At1Ems,
       "ne843At1Bzi": ne843At1Bzi,
       "ne843At1Bzt": ne843At1Bzt,
       "ne843At1Irt": ne843At1Irt,
       "ne843At1Ata": ne843At1Ata,
       "ne843At1Atb": ne843At1Atb,
       "ne843At1Snt": ne843At1Snt,
       "ne843TrsTable": ne843TrsTable,
       "ne843TrsEntry": ne843TrsEntry,
       "ne843TrsEntryIndex": ne843TrsEntryIndex,
       "ne843TrsEntryIde": ne843TrsEntryIde,
       "ne843TrsEntryDes": ne843TrsEntryDes,
       "ne843TrsEntrySrc": ne843TrsEntrySrc,
       "ne843Aco1": ne843Aco1,
       "ne843Aco1Ide": ne843Aco1Ide,
       "ne843Aco1Des": ne843Aco1Des,
       "ne843Aco1Stt": ne843Aco1Stt,
       "ne843Aco1Cst": ne843Aco1Cst,
       "ne843Aco1Cae": ne843Aco1Cae,
       "ne843Aco1Cto": ne843Aco1Cto,
       "ne843Aco1Jst": ne843Aco1Jst,
       "ne843Aco1Jae": ne843Aco1Jae,
       "ne843Aco1Jto": ne843Aco1Jto,
       "ne843Aco1Nst": ne843Aco1Nst,
       "ne843Aco1Nae": ne843Aco1Nae,
       "ne843Aco1Nto": ne843Aco1Nto,
       "ne843Aco1Lbe": ne843Aco1Lbe,
       "ne843Aco1Aac": ne843Aco1Aac,
       "ne843Gm1": ne843Gm1,
       "ne843Gm1Ide": ne843Gm1Ide,
       "ne843Gm1Des": ne843Gm1Des,
       "ne843Gm1Lse": ne843Gm1Lse,
       "ne843Gm1Rme": ne843Gm1Rme,
       "ne843Gm1Fsd": ne843Gm1Fsd,
       "ne843Gm1Bsd": ne843Gm1Bsd,
       "ne843Gm1Fsp": ne843Gm1Fsp,
       "ne843Gm1Bsp": ne843Gm1Bsp,
       "ne843Gm1Fcl": ne843Gm1Fcl,
       "ne843Gm1Bcl": ne843Gm1Bcl,
       "ne843Gm1Oft": ne843Gm1Oft,
       "ne843Gm1Wie": ne843Gm1Wie,
       "ne843Gm1Sof": ne843Gm1Sof,
       "ne843Gm1Lsfe": ne843Gm1Lsfe,
       "ne843Gm1Nro": ne843Gm1Nro,
       "ne843Gm1Lst": ne843Gm1Lst,
       "ne843Gm1Nro1": ne843Gm1Nro1,
       "ne843RecTable": ne843RecTable,
       "ne843RecEntry": ne843RecEntry,
       "ne843RecEntryIndex": ne843RecEntryIndex,
       "ne843RecEntryIde": ne843RecEntryIde,
       "ne843RecEntryDes": ne843RecEntryDes,
       "ne843RecEntryTyp": ne843RecEntryTyp,
       "ne843RecEntrySn": ne843RecEntrySn,
       "ne843RecEntryAdc": ne843RecEntryAdc,
       "ne843RecEntryVdc": ne843RecEntryVdc,
       "ne843RecEntryStt": ne843RecEntryStt,
       "ne843RecEntryCap": ne843RecEntryCap,
       "ne843RecEntryVac": ne843RecEntryVac,
       "ne843RecEntryAac": ne843RecEntryAac,
       "ne843RecEntryTmp": ne843RecEntryTmp,
       "ne843RecEntrySeq": ne843RecEntrySeq,
       "ne843RecEntryRfa": ne843RecEntryRfa,
       "ne843RecEntryAcf": ne843RecEntryAcf,
       "ne843RecEntryMan": ne843RecEntryMan,
       "ne843RecEntryDid": ne843RecEntryDid,
       "ne843RecEntryClm": ne843RecEntryClm,
       "ne843RecEntryRcf": ne843RecEntryRcf,
       "ne843RecEntryRfn": ne843RecEntryRfn,
       "ne843RecEntryRif": ne843RecEntryRif,
       "ne843RecEntryLsf": ne843RecEntryLsf,
       "ne843RecEntryCc": ne843RecEntryCc,
       "ne843RecEntryClei": ne843RecEntryClei,
       "ne843RecEntrySer": ne843RecEntrySer,
       "ne843RecEntryVerp": ne843RecEntryVerp,
       "ne843RecEntryVers": ne843RecEntryVers,
       "ne843RecEntryLin": ne843RecEntryLin,
       "ne843RecEntryHin": ne843RecEntryHin,
       "ne843RecEntryBof": ne843RecEntryBof,
       "ne843RecEntrySof": ne843RecEntrySof,
       "ne843RecEntryDer": ne843RecEntryDer,
       "ne843RecEntryEcap": ne843RecEntryEcap,
       "ne843RecEntryEmod": ne843RecEntryEmod,
       "ne843RecEntryMppt": ne843RecEntryMppt,
       "ne843RecEntryRtm": ne843RecEntryRtm,
       "ne843RecEntryVan": ne843RecEntryVan,
       "ne843RecEntryVac1": ne843RecEntryVac1,
       "ne843RecEntryAac1": ne843RecEntryAac1,
       "ne843RecEntryVac2": ne843RecEntryVac2,
       "ne843RecEntryAac2": ne843RecEntryAac2,
       "ne843RecEntryVac3": ne843RecEntryVac3,
       "ne843RecEntryAac3": ne843RecEntryAac3,
       "ne843RecEntryRfa1": ne843RecEntryRfa1,
       "ne843RecEntryAcf1": ne843RecEntryAcf1,
       "ne843RecEntryMan1": ne843RecEntryMan1,
       "ne843RecEntryDid1": ne843RecEntryDid1,
       "ne843RecEntryClm1": ne843RecEntryClm1,
       "ne843RecEntryRcf1": ne843RecEntryRcf1,
       "ne843RecEntryRfn1": ne843RecEntryRfn1,
       "ne843RecEntryRif1": ne843RecEntryRif1,
       "ne843RecEntryLsf1": ne843RecEntryLsf1,
       "ne843RecEntryLin1": ne843RecEntryLin1,
       "ne843RecEntryHin1": ne843RecEntryHin1,
       "ne843RecEntryBof1": ne843RecEntryBof1,
       "ne843RecEntrySof1": ne843RecEntrySof1,
       "ne843RecEntryDer1": ne843RecEntryDer1,
       "ne843Cp1": ne843Cp1,
       "ne843Cp1Ide": ne843Cp1Ide,
       "ne843Cp1Des": ne843Cp1Des,
       "ne843Cp1Typ": ne843Cp1Typ,
       "ne843Cp1Vdc": ne843Cp1Vdc,
       "ne843Cp1Adc": ne843Cp1Adc,
       "ne843Cp1Cap": ne843Cp1Cap,
       "ne843Cp1Olcap": ne843Cp1Olcap,
       "ne843Cp1Vsp": ne843Cp1Vsp,
       "ne843Cp1Vsd": ne843Cp1Vsd,
       "ne843Cp1Clm": ne843Cp1Clm,
       "ne843Cp1Dth": ne843Cp1Dth,
       "ne843Cp1Rth": ne843Cp1Rth,
       "ne843Cp1Lvd": ne843Cp1Lvd,
       "ne843Cp1Rss": ne843Cp1Rss,
       "ne843Cp1Rme": ne843Cp1Rme,
       "ne843Cp1Rof": ne843Cp1Rof,
       "ne843Cp1Cfa": ne843Cp1Cfa,
       "ne843Cp1Cfn": ne843Cp1Cfn,
       "ne843Cp1Cfj": ne843Cp1Cfj,
       "ne843Cp1Dfa": ne843Cp1Dfa,
       "ne843Cp1Did": ne843Cp1Did,
       "ne843Cp1Icc": ne843Cp1Icc,
       "ne843Cp1Mfa": ne843Cp1Mfa,
       "ne843Cp1Hva": ne843Cp1Hva,
       "ne843Cp1Hfv": ne843Cp1Hfv,
       "ne843Cp1Vla": ne843Cp1Vla,
       "ne843Cp1Rl": ne843Cp1Rl,
       "ne843Cp1Cin": ne843Cp1Cin,
       "ne843DccTable": ne843DccTable,
       "ne843DccEntry": ne843DccEntry,
       "ne843DccEntryIndex": ne843DccEntryIndex,
       "ne843DccEntryIde": ne843DccEntryIde,
       "ne843DccEntryDes": ne843DccEntryDes,
       "ne843DccEntryTyp": ne843DccEntryTyp,
       "ne843DccEntrySn": ne843DccEntrySn,
       "ne843DccEntryAdc": ne843DccEntryAdc,
       "ne843DccEntryCap": ne843DccEntryCap,
       "ne843DccEntryStt": ne843DccEntryStt,
       "ne843DccEntryCfa": ne843DccEntryCfa,
       "ne843DccEntryDfa": ne843DccEntryDfa,
       "ne843DccEntryDid": ne843DccEntryDid,
       "ne843DccEntryCcf": ne843DccEntryCcf,
       "ne843DccEntryCfn": ne843DccEntryCfn,
       "ne843DccEntryCfa1": ne843DccEntryCfa1,
       "ne843DccEntryDfa1": ne843DccEntryDfa1,
       "ne843DccEntryDid1": ne843DccEntryDid1,
       "ne843DccEntryCcf1": ne843DccEntryCcf1,
       "ne843DccEntryCfn1": ne843DccEntryCfn1,
       "ne843Bs1": ne843Bs1,
       "ne843Bs1Ide": ne843Bs1Ide,
       "ne843Bs1Des": ne843Bs1Des,
       "ne843Bs1Stt": ne843Bs1Stt,
       "ne843Bs1Atm": ne843Bs1Atm,
       "ne843Bs1Tmd": ne843Bs1Tmd,
       "ne843Bs1Amf": ne843Bs1Amf,
       "ne843Bs1Cta": ne843Bs1Cta,
       "ne843Sc1": ne843Sc1,
       "ne843Sc1Ide": ne843Sc1Ide,
       "ne843Sc1Des": ne843Sc1Des,
       "ne843Sc1Stt": ne843Sc1Stt,
       "ne843Sc1Rve": ne843Sc1Rve,
       "ne843Sc1Ltt": ne843Sc1Ltt,
       "ne843Sc1Ntt": ne843Sc1Ntt,
       "ne843Sc1Utt": ne843Sc1Utt,
       "ne843Sc1Spt": ne843Sc1Spt,
       "ne843Sc1Lsp": ne843Sc1Lsp,
       "ne843Sc1Usp": ne843Sc1Usp,
       "ne843Sc1Fse": ne843Sc1Fse,
       "ne843BtdTable": ne843BtdTable,
       "ne843BtdEntry": ne843BtdEntry,
       "ne843BtdEntryIndex": ne843BtdEntryIndex,
       "ne843BtdEntryIde": ne843BtdEntryIde,
       "ne843BtdEntryDes": ne843BtdEntryDes,
       "ne843BtdEntryBty": ne843BtdEntryBty,
       "ne843BtdEntryBtc": ne843BtdEntryBtc,
       "ne843BtdEntryCap": ne843BtdEntryCap,
       "ne843Br1": ne843Br1,
       "ne843Br1Ide": ne843Br1Ide,
       "ne843Br1Des": ne843Br1Des,
       "ne843Br1Adc": ne843Br1Adc,
       "ne843Br1Hbt": ne843Br1Hbt,
       "ne843Br1Cap": ne843Br1Cap,
       "ne843Br1Olcap": ne843Br1Olcap,
       "ne843Br1Btr": ne843Br1Btr,
       "ne843Br1Tth": ne843Br1Tth,
       "ne843Br1Cle": ne843Br1Cle,
       "ne843Br1Clt": ne843Br1Clt,
       "ne843Br1Cev": ne843Br1Cev,
       "ne843Br1Bts": ne843Br1Bts,
       "ne843Br1Mtt": ne843Br1Mtt,
       "ne843Br1Tev": ne843Br1Tev,
       "ne843Br1Tmd": ne843Br1Tmd,
       "ne843Br1Bte": ne843Br1Bte,
       "ne843Br1Btv": ne843Br1Btv,
       "ne843Br1Ath": ne843Br1Ath,
       "ne843Br1Tin": ne843Br1Tin,
       "ne843Br1Atw": ne843Br1Atw,
       "ne843Br1Atd": ne843Br1Atd,
       "ne843Br1Nvm": ne843Br1Nvm,
       "ne843Br1Ntm": ne843Br1Ntm,
       "ne843Br1Scd": ne843Br1Scd,
       "ne843Br1Scv": ne843Br1Scv,
       "ne843Br1Bta": ne843Br1Bta,
       "ne843Br1Bfa": ne843Br1Bfa,
       "ne843Br1Scda": ne843Br1Scda,
       "ne843Br1Isda": ne843Br1Isda,
       "ne843Br1Mdp": ne843Br1Mdp,
       "ne843Br1Mzd": ne843Br1Mzd,
       "ne843Br1Btha": ne843Br1Btha,
       "ne843Br1Lbt": ne843Br1Lbt,
       "ne843Br1Btla": ne843Br1Btla,
       "ne843Br1Btvh": ne843Br1Btvh,
       "ne843Br1Btvl": ne843Br1Btvl,
       "ne843Br1Rba": ne843Br1Rba,
       "ne843CntTable": ne843CntTable,
       "ne843CntEntry": ne843CntEntry,
       "ne843CntEntryIndex": ne843CntEntryIndex,
       "ne843CntEntryIde": ne843CntEntryIde,
       "ne843CntEntryDes": ne843CntEntryDes,
       "ne843CntEntryStt": ne843CntEntryStt,
       "ne843CntEntryEna": ne843CntEntryEna,
       "ne843CntEntryDth": ne843CntEntryDth,
       "ne843CntEntryDdy": ne843CntEntryDdy,
       "ne843CntEntryDam": ne843CntEntryDam,
       "ne843CntEntryDtm": ne843CntEntryDtm,
       "ne843CntEntryRth": ne843CntEntryRth,
       "ne843CntEntryRdy": ne843CntEntryRdy,
       "ne843CntEntryRam": ne843CntEntryRam,
       "ne843CntEntryRtm": ne843CntEntryRtm,
       "ne843CntEntryCno": ne843CntEntryCno,
       "ne843CntEntryCnf": ne843CntEntryCnf,
       "ne843CntEntryDvx": ne843CntEntryDvx,
       "ne843CntEntryDin": ne843CntEntryDin,
       "ne843CntEntryDix": ne843CntEntryDix,
       "ne843CntEntryDvt": ne843CntEntryDvt,
       "ne843CntEntryDtd": ne843CntEntryDtd,
       "ne843CntEntryDtp": ne843CntEntryDtp,
       "ne843CntEntryRtd": ne843CntEntryRtd,
       "ne843CntEntryRtp": ne843CntEntryRtp,
       "ne843DcnTable": ne843DcnTable,
       "ne843DcnEntry": ne843DcnEntry,
       "ne843DcnEntryIndex": ne843DcnEntryIndex,
       "ne843DcnEntryIde": ne843DcnEntryIde,
       "ne843DcnEntryDes": ne843DcnEntryDes,
       "ne843DcnEntryStt": ne843DcnEntryStt,
       "ne843DcnEntryTyp": ne843DcnEntryTyp,
       "ne843DcnEntrySn": ne843DcnEntrySn,
       "ne843DcnEntryBrc": ne843DcnEntryBrc,
       "ne843DcmTable": ne843DcmTable,
       "ne843DcmEntry": ne843DcmEntry,
       "ne843DcmEntryIndex": ne843DcmEntryIndex,
       "ne843DcmEntryIde": ne843DcmEntryIde,
       "ne843DcmEntryDes": ne843DcmEntryDes,
       "ne843DcmEntryStt": ne843DcmEntryStt,
       "ne843DcmEntryTyp": ne843DcmEntryTyp,
       "ne843DcmEntryVal": ne843DcmEntryVal,
       "ne843DcmEntrySha": ne843DcmEntrySha,
       "ne843DcmEntrySn": ne843DcmEntrySn,
       "ne843DcmEntryBrc": ne843DcmEntryBrc,
       "ne843DcmEntryKwh": ne843DcmEntryKwh,
       "ne843UdeTable": ne843UdeTable,
       "ne843UdeEntry": ne843UdeEntry,
       "ne843UdeEntryIndex": ne843UdeEntryIndex,
       "ne843UdeEntryIde": ne843UdeEntryIde,
       "ne843UdeEntryDes": ne843UdeEntryDes,
       "ne843UdeEntryFds": ne843UdeEntryFds,
       "ne843UdeEntryAst": ne843UdeEntryAst,
       "ne843UdeEntrySev": ne843UdeEntrySev,
       "ne843UdeEntryPrg": ne843UdeEntryPrg,
       "ne843UdeEntryDur": ne843UdeEntryDur,
       "ne843UdeEntryLed": ne843UdeEntryLed,
       "ne843UdeEntryLat": ne843UdeEntryLat,
       "ne843UdeEntryAcc": ne843UdeEntryAcc,
       "ne843UdeEntryDly": ne843UdeEntryDly,
       "ne843UdeEntryNoo": ne843UdeEntryNoo,
       "ne843UdeEntryNor": ne843UdeEntryNor,
       "ne843UdeEntryNag": ne843UdeEntryNag,
       "ne843UdeEntryDst": ne843UdeEntryDst,
       "ne843UdeEntryAst1": ne843UdeEntryAst1,
       "ne843Cm1": ne843Cm1,
       "ne843Cm1Ide": ne843Cm1Ide,
       "ne843Cm1Des": ne843Cm1Des,
       "ne843Cm1Ngi": ne843Cm1Ngi,
       "ne843Cm1Cof": ne843Cm1Cof,
       "ne843Cm1Cor": ne843Cm1Cor,
       "ne843Cm1Nnc": ne843Cm1Nnc,
       "ne843CopTable": ne843CopTable,
       "ne843CopEntry": ne843CopEntry,
       "ne843CopEntryIndex": ne843CopEntryIndex,
       "ne843CopEntryIde": ne843CopEntryIde,
       "ne843CopEntryDes": ne843CopEntryDes,
       "ne843CopEntryTyp": ne843CopEntryTyp,
       "ne843CopEntryPhn": ne843CopEntryPhn,
       "ne843CopEntryBdr": ne843CopEntryBdr,
       "ne843CopEntryDbt": ne843CopEntryDbt,
       "ne843CopEntryPry": ne843CopEntryPry,
       "ne843CopEntrySbt": ne843CopEntrySbt,
       "ne843CopEntryDly": ne843CopEntryDly,
       "ne843CopEntryPgr": ne843CopEntryPgr,
       "ne843CopEntryMsg": ne843CopEntryMsg,
       "ne843CoeTable": ne843CoeTable,
       "ne843CoeEntry": ne843CoeEntry,
       "ne843CoeEntryIndex": ne843CoeEntryIndex,
       "ne843CoeEntryIde": ne843CoeEntryIde,
       "ne843CoeEntryDes": ne843CoeEntryDes,
       "ne843CoeEntryAdr": ne843CoeEntryAdr,
       "ne843CoeEntryTyp": ne843CoeEntryTyp,
       "ne843SndTable": ne843SndTable,
       "ne843SndEntry": ne843SndEntry,
       "ne843SndEntryIndex": ne843SndEntryIndex,
       "ne843SndEntryIde": ne843SndEntryIde,
       "ne843SndEntryDes": ne843SndEntryDes,
       "ne843SndEntryIp": ne843SndEntryIp,
       "ne843SndEntryCs": ne843SndEntryCs,
       "ne843Po1": ne843Po1,
       "ne843Po1Ide": ne843Po1Ide,
       "ne843Po1Des": ne843Po1Des,
       "ne843Po1Phn": ne843Po1Phn,
       "ne843Po1Bdr": ne843Po1Bdr,
       "ne843Po1Dbt": ne843Po1Dbt,
       "ne843Po1Pry": ne843Po1Pry,
       "ne843Po1Sbt": ne843Po1Sbt,
       "ne843Po1Int": ne843Po1Int,
       "ne843Po1Tim": ne843Po1Tim,
       "ne843Po1Cl01": ne843Po1Cl01,
       "ne843Po1Cl02": ne843Po1Cl02,
       "ne843Po1Cl03": ne843Po1Cl03,
       "ne843Po1Cl04": ne843Po1Cl04,
       "ne843Po1Cl05": ne843Po1Cl05,
       "ne843Po1Cl06": ne843Po1Cl06,
       "ne843Po1Cl07": ne843Po1Cl07,
       "ne843Po1Cl08": ne843Po1Cl08,
       "ne843Po1Cl09": ne843Po1Cl09,
       "ne843Po1Cl10": ne843Po1Cl10,
       "ne843Po1Por": ne843Po1Por,
       "ne843Cb1": ne843Cb1,
       "ne843Cb1Ide": ne843Cb1Ide,
       "ne843Cb1Des": ne843Cb1Des,
       "ne843Cb1Stt": ne843Cb1Stt,
       "ne843Cb1Ph1": ne843Cb1Ph1,
       "ne843Cb1Br1": ne843Cb1Br1,
       "ne843Cb1Ph2": ne843Cb1Ph2,
       "ne843Cb1Br2": ne843Cb1Br2,
       "ne843Cb1Ph3": ne843Cb1Ph3,
       "ne843Cb1Br3": ne843Cb1Br3,
       "ne843Cb1Ph4": ne843Cb1Ph4,
       "ne843Cb1Br4": ne843Cb1Br4,
       "ne843Cb1Ph5": ne843Cb1Ph5,
       "ne843Cb1Br5": ne843Cb1Br5,
       "ne843Mp1": ne843Mp1,
       "ne843Mp1Ide": ne843Mp1Ide,
       "ne843Mp1Des": ne843Mp1Des,
       "ne843Mp1Stt": ne843Mp1Stt,
       "ne843Mp1Bdr": ne843Mp1Bdr,
       "ne843Mp1Dbt": ne843Mp1Dbt,
       "ne843Mp1Pry": ne843Mp1Pry,
       "ne843Mp1Sbt": ne843Mp1Sbt,
       "ne843Mp1Tmo": ne843Mp1Tmo,
       "ne843Mp1Hsh": ne843Mp1Hsh,
       "ne843Mp1Nrg": ne843Mp1Nrg,
       "ne843Mp1Wre": ne843Mp1Wre,
       "ne843Mp1Ins": ne843Mp1Ins,
       "ne843Lp1": ne843Lp1,
       "ne843Lp1Ide": ne843Lp1Ide,
       "ne843Lp1Des": ne843Lp1Des,
       "ne843Lp1Stt": ne843Lp1Stt,
       "ne843Lp1Bdr": ne843Lp1Bdr,
       "ne843Lp1Dbt": ne843Lp1Dbt,
       "ne843Lp1Pry": ne843Lp1Pry,
       "ne843Lp1Sbt": ne843Lp1Sbt,
       "ne843Lp1Tmo": ne843Lp1Tmo,
       "ne843Lp1Hsh": ne843Lp1Hsh,
       "ne843Lp1App": ne843Lp1App,
       "ne843Lp1Wre": ne843Lp1Wre,
       "ne843Tlm1": ne843Tlm1,
       "ne843Tlm1Ide": ne843Tlm1Ide,
       "ne843Tlm1Des": ne843Tlm1Des,
       "ne843Tlm1Aue": ne843Tlm1Aue,
       "ne843Tlm1Prt": ne843Tlm1Prt,
       "ne843Tlm1Tmo": ne843Tlm1Tmo,
       "ne843Tl1Table": ne843Tl1Table,
       "ne843Tl1Entry": ne843Tl1Entry,
       "ne843Tl1EntryIndex": ne843Tl1EntryIndex,
       "ne843Tl1EntryIde": ne843Tl1EntryIde,
       "ne843Tl1EntryDes": ne843Tl1EntryDes,
       "ne843Tl1EntryCds": ne843Tl1EntryCds,
       "ne843Tl1EntryAid": ne843Tl1EntryAid,
       "ne843Tl1EntryCnd": ne843Tl1EntryCnd,
       "ne843Tl1EntrySaf": ne843Tl1EntrySaf,
       "ne843Tl1EntryRpt": ne843Tl1EntryRpt,
       "ne843Net1": ne843Net1,
       "ne843Net1Ide": ne843Net1Ide,
       "ne843Net1Des": ne843Net1Des,
       "ne843Net1Ead": ne843Net1Ead,
       "ne843Net1Dhcp": ne843Net1Dhcp,
       "ne843Net1Ip": ne843Net1Ip,
       "ne843Net1Wip": ne843Net1Wip,
       "ne843Net1Sub": ne843Net1Sub,
       "ne843Net1Gtwy": ne843Net1Gtwy,
       "ne843Net1Host": ne843Net1Host,
       "ne843Net1Dom": ne843Net1Dom,
       "ne843Net1Dns": ne843Net1Dns,
       "ne843Net1Wre": ne843Net1Wre,
       "ne843Net1Tmo": ne843Net1Tmo,
       "ne843Net1Msrv": ne843Net1Msrv,
       "ne843Net1Ntp": ne843Net1Ntp,
       "ne843Net1Sma": ne843Net1Sma,
       "ne843Net1Sid": ne843Net1Sid,
       "ne843Net1Fpe": ne843Net1Fpe,
       "ne843Net1Hpe": ne843Net1Hpe,
       "ne843Net1Hse": ne843Net1Hse,
       "ne843Net1She": ne843Net1She,
       "ne843Net1Sne": ne843Net1Sne,
       "ne843Net1Tle": ne843Net1Tle,
       "ne843Net1Ip6": ne843Net1Ip6,
       "ne843Net1Gtwy6": ne843Net1Gtwy6,
       "ne843Net1Wip6": ne843Net1Wip6,
       "ne843Net1Ll6": ne843Net1Ll6,
       "ne843Net1Pl6": ne843Net1Pl6,
       "ne843Net1Wgtwy6": ne843Net1Wgtwy6,
       "ne843DrcTable": ne843DrcTable,
       "ne843DrcEntry": ne843DrcEntry,
       "ne843DrcEntryIndex": ne843DrcEntryIndex,
       "ne843DrcEntryIde": ne843DrcEntryIde,
       "ne843DrcEntryDes": ne843DrcEntryDes,
       "ne843DrcEntryVal": ne843DrcEntryVal,
       "ne843DrcEntryPrg": ne843DrcEntryPrg,
       "ne843DrcEntryUni": ne843DrcEntryUni,
       "ne843InpTable": ne843InpTable,
       "ne843InpEntry": ne843InpEntry,
       "ne843InpEntryIndex": ne843InpEntryIndex,
       "ne843InpEntryIde": ne843InpEntryIde,
       "ne843InpEntryDes": ne843InpEntryDes,
       "ne843InpEntryStt": ne843InpEntryStt,
       "ne843InpEntryTyp": ne843InpEntryTyp,
       "ne843InpEntryPol": ne843InpEntryPol,
       "ne843InpEntrySn": ne843InpEntrySn,
       "ne843InpEntryBrc": ne843InpEntryBrc,
       "ne843MsvTable": ne843MsvTable,
       "ne843MsvEntry": ne843MsvEntry,
       "ne843MsvEntryIndex": ne843MsvEntryIndex,
       "ne843MsvEntryIde": ne843MsvEntryIde,
       "ne843MsvEntryDes": ne843MsvEntryDes,
       "ne843MsvEntryStt": ne843MsvEntryStt,
       "ne843MsvEntryVal": ne843MsvEntryVal,
       "ne843MsvEntryDid": ne843MsvEntryDid,
       "ne843MsvEntryDid1": ne843MsvEntryDid1,
       "ne843Rp1": ne843Rp1,
       "ne843Rp1Ide": ne843Rp1Ide,
       "ne843Rp1Des": ne843Rp1Des,
       "ne843Rp1Frq": ne843Rp1Frq,
       "ne843Rp1Vsp": ne843Rp1Vsp,
       "ne843Rp1Ofe": ne843Rp1Ofe,
       "ne843Rp1Rme": ne843Rp1Rme,
       "ne843Rp1Rss": ne843Rp1Rss,
       "ne843Rp1Rf": ne843Rp1Rf,
       "ne843Rp1Rpff": ne843Rp1Rpff,
       "ne843Rp1Rprl": ne843Rp1Rprl,
       "ne843Rp1Rpfj": ne843Rp1Rpfj,
       "ne843Rp1Rpxj": ne843Rp1Rpxj,
       "ne843Rp1Rpxn": ne843Rp1Rpxn,
       "ne843Rp1Rcdp": ne843Rp1Rcdp,
       "ne843Rp1Cap": ne843Rp1Cap,
       "ne843Rp1Olcap": ne843Rp1Olcap,
       "ne843Rp1Va": ne843Rp1Va,
       "ne843Rp1Rrf": ne843Rp1Rrf,
       "ne843RchTable": ne843RchTable,
       "ne843RchEntry": ne843RchEntry,
       "ne843RchEntryIndex": ne843RchEntryIndex,
       "ne843RchEntryIde": ne843RchEntryIde,
       "ne843RchEntryDes": ne843RchEntryDes,
       "ne843RchEntryStt": ne843RchEntryStt,
       "ne843RchEntryVa": ne843RchEntryVa,
       "ne843RchEntryPri": ne843RchEntryPri,
       "ne843RchEntrySec": ne843RchEntrySec,
       "ne843RchEntryRf": ne843RchEntryRf,
       "ne843RchEntryRpff": ne843RchEntryRpff,
       "ne843RchEntryRpxj": ne843RchEntryRpxj,
       "ne843RchEntryRpxn": ne843RchEntryRpxn,
       "ne843RchEntryRprl": ne843RchEntryRprl,
       "ne843RchEntryRpfj": ne843RchEntryRpfj,
       "ne843RchEntryRcdp": ne843RchEntryRcdp,
       "ne843RchEntryPsn": ne843RchEntryPsn,
       "ne843RchEntryPtyp": ne843RchEntryPtyp,
       "ne843RchEntryPstt": ne843RchEntryPstt,
       "ne843RchEntrySsn": ne843RchEntrySsn,
       "ne843RchEntryStyp": ne843RchEntryStyp,
       "ne843RchEntrySstt": ne843RchEntrySstt,
       "ne843RchEntryCap": ne843RchEntryCap,
       "ne843AlarmTable": ne843AlarmTable,
       "ne843AlarmEntry": ne843AlarmEntry,
       "ne843AlarmEntryIndex": ne843AlarmEntryIndex,
       "ne843AlarmEntryDes": ne843AlarmEntryDes,
       "ne843AlarmEntryAst": ne843AlarmEntryAst,
       "ne843AlarmEntrySev": ne843AlarmEntrySev,
       "ne843AlarmEntryAcc": ne843AlarmEntryAcc,
       "ne843AlarmEntryThr": ne843AlarmEntryThr,
       "ne843AlarmEntryFth": ne843AlarmEntryFth,
       "ne843AlarmEntryBth": ne843AlarmEntryBth,
       "ne843AlarmEntryDly": ne843AlarmEntryDly,
       "ne843AlarmEntryNoo": ne843AlarmEntryNoo,
       "ne843AlarmEntryNor": ne843AlarmEntryNor,
       "ne843AlarmEntryNag": ne843AlarmEntryNag,
       "ne843AlarmEntryDst": ne843AlarmEntryDst,
       "ne843Trap": ne843Trap,
       "ne843TrapDc1Amj": ne843TrapDc1Amj,
       "ne843TrapDc1Vsf": ne843TrapDc1Vsf,
       "ne843TrapDc1Osa": ne843TrapDc1Osa,
       "ne843TrapDc1Zid": ne843TrapDc1Zid,
       "ne843TrapDc1Tpa": ne843TrapDc1Tpa,
       "ne843TrapDc1Vmf": ne843TrapDc1Vmf,
       "ne843TrapDc1Cma": ne843TrapDc1Cma,
       "ne843TrapDc1Mcm": ne843TrapDc1Mcm,
       "ne843TrapDc1Epo": ne843TrapDc1Epo,
       "ne843TrapDc1Icr": ne843TrapDc1Icr,
       "ne843TrapDc1Rfa": ne843TrapDc1Rfa,
       "ne843TrapDc1Acf": ne843TrapDc1Acf,
       "ne843TrapDc1Man": ne843TrapDc1Man,
       "ne843TrapDc1Did": ne843TrapDc1Did,
       "ne843TrapDc1Clm": ne843TrapDc1Clm,
       "ne843TrapDc1Rfn": ne843TrapDc1Rfn,
       "ne843TrapDc1Vla": ne843TrapDc1Vla,
       "ne843TrapDc1Mfa": ne843TrapDc1Mfa,
       "ne843TrapDc1Rtl": ne843TrapDc1Rtl,
       "ne843TrapDc1Rrtl": ne843TrapDc1Rrtl,
       "ne843TrapDc1Rls": ne843TrapDc1Rls,
       "ne843TrapDc1Mman": ne843TrapDc1Mman,
       "ne843TrapDc1Macf": ne843TrapDc1Macf,
       "ne843TrapDc1Bda": ne843TrapDc1Bda,
       "ne843TrapDc1Hva": ne843TrapDc1Hva,
       "ne843TrapDc1Hfv": ne843TrapDc1Hfv,
       "ne843TrapPs1Epr": ne843TrapPs1Epr,
       "ne843TrapPs1Pfd": ne843TrapPs1Pfd,
       "ne843TrapPs1Exl": ne843TrapPs1Exl,
       "ne843TrapPs1Bbl": ne843TrapPs1Bbl,
       "ne843TrapPs1Clc": ne843TrapPs1Clc,
       "ne843TrapPs1Stf": ne843TrapPs1Stf,
       "ne843TrapPs1Pgi": ne843TrapPs1Pgi,
       "ne843TrapPs1Cch": ne843TrapPs1Cch,
       "ne843TrapPs1Hcl": ne843TrapPs1Hcl,
       "ne843TrapPs1Ax1": ne843TrapPs1Ax1,
       "ne843TrapPs1Ax2": ne843TrapPs1Ax2,
       "ne843TrapPs1Ax3": ne843TrapPs1Ax3,
       "ne843TrapPs1Ax4": ne843TrapPs1Ax4,
       "ne843TrapPs1Ax5": ne843TrapPs1Ax5,
       "ne843TrapPs1Ax6": ne843TrapPs1Ax6,
       "ne843TrapPs1Fan24": ne843TrapPs1Fan24,
       "ne843TrapPs1Fan48": ne843TrapPs1Fan48,
       "ne843TrapPs1Faj24": ne843TrapPs1Faj24,
       "ne843TrapPs1Faj48": ne843TrapPs1Faj48,
       "ne843TrapAt1Ata": ne843TrapAt1Ata,
       "ne843TrapAt1Atb": ne843TrapAt1Atb,
       "ne843TrapCp1Cfa": ne843TrapCp1Cfa,
       "ne843TrapCp1Cfn": ne843TrapCp1Cfn,
       "ne843TrapCp1Cfj": ne843TrapCp1Cfj,
       "ne843TrapCp1Dfa": ne843TrapCp1Dfa,
       "ne843TrapCp1Did": ne843TrapCp1Did,
       "ne843TrapCp1Icc": ne843TrapCp1Icc,
       "ne843TrapCp1Mfa": ne843TrapCp1Mfa,
       "ne843TrapCp1Hva": ne843TrapCp1Hva,
       "ne843TrapCp1Hfv": ne843TrapCp1Hfv,
       "ne843TrapCp1Vla": ne843TrapCp1Vla,
       "ne843TrapCp1Rl": ne843TrapCp1Rl,
       "ne843TrapBr1Bta": ne843TrapBr1Bta,
       "ne843TrapBr1Bfa": ne843TrapBr1Bfa,
       "ne843TrapBr1Scda": ne843TrapBr1Scda,
       "ne843TrapBr1Isda": ne843TrapBr1Isda,
       "ne843TrapBr1Mdp": ne843TrapBr1Mdp,
       "ne843TrapBr1Mzd": ne843TrapBr1Mzd,
       "ne843TrapBr1Btha": ne843TrapBr1Btha,
       "ne843TrapCn1Cno": ne843TrapCn1Cno,
       "ne843TrapCn1Cnf": ne843TrapCn1Cnf,
       "ne843TrapCn2Cno": ne843TrapCn2Cno,
       "ne843TrapCn2Cnf": ne843TrapCn2Cnf,
       "ne843TrapCn3Cno": ne843TrapCn3Cno,
       "ne843TrapCn3Cnf": ne843TrapCn3Cnf,
       "ne843TrapCn4Cno": ne843TrapCn4Cno,
       "ne843TrapCn4Cnf": ne843TrapCn4Cnf,
       "ne843TrapCm1Cof": ne843TrapCm1Cof,
       "ne843TrapCm1Cor": ne843TrapCm1Cor,
       "ne843TrapCm1Nnc": ne843TrapCm1Nnc,
       "ne843TrapPo1Por": ne843TrapPo1Por,
       "ne843TrapRp1Rf": ne843TrapRp1Rf,
       "ne843TrapRp1Rpff": ne843TrapRp1Rpff,
       "ne843TrapRp1Rprl": ne843TrapRp1Rprl,
       "ne843TrapRp1Rpfj": ne843TrapRp1Rpfj,
       "ne843TrapRp1Rpxj": ne843TrapRp1Rpxj,
       "ne843TrapRp1Rpxn": ne843TrapRp1Rpxn,
       "ne843TrapRp1Rcdp": ne843TrapRp1Rcdp,
       "ne843TrapUserDefined": ne843TrapUserDefined,
       "ne843TrapDc1Emd": ne843TrapDc1Emd,
       "ne843TrapDc1Pfs": ne843TrapDc1Pfs,
       "ne843TrapDc1Rif": ne843TrapDc1Rif,
       "ne843TrapDc1Lsf": ne843TrapDc1Lsf,
       "ne843TrapPs1Ax7": ne843TrapPs1Ax7,
       "ne843TrapPs1Ax8": ne843TrapPs1Ax8,
       "ne843TrapPs1Ax9": ne843TrapPs1Ax9,
       "ne843TrapPs1Ax10": ne843TrapPs1Ax10,
       "ne843TrapPs1Ax11": ne843TrapPs1Ax11,
       "ne843TrapPs1Ax12": ne843TrapPs1Ax12,
       "ne843TrapBr1Btla": ne843TrapBr1Btla,
       "ne843TrapBr1Btvh": ne843TrapBr1Btvh,
       "ne843TrapBr1Btvl": ne843TrapBr1Btvl,
       "ne843TrapGn1Gnr": ne843TrapGn1Gnr,
       "ne843TrapGn1Gnm": ne843TrapGn1Gnm,
       "ne843TrapGn1Gnf": ne843TrapGn1Gnf,
       "ne843TrapPs1Amtl": ne843TrapPs1Amtl,
       "ne843TrapPs1Amth": ne843TrapPs1Amth,
       "ne843TrapAco1Aac": ne843TrapAco1Aac,
       "ne843TrapBr1Rba": ne843TrapBr1Rba,
       "ne843TrapCp1Cin": ne843TrapCp1Cin,
       "ne843TrapDc1Bof": ne843TrapDc1Bof,
       "ne843TrapDc1Sof": ne843TrapDc1Sof,
       "ne843TrapDc1Der": ne843TrapDc1Der,
       "ne843TrapGn1Gns": ne843TrapGn1Gns,
       "ne843TrapIvp1Ilvi": ne843TrapIvp1Ilvi,
       "ne843TrapIvp1Ihvi": ne843TrapIvp1Ihvi,
       "ne843TrapIvp1Ita": ne843TrapIvp1Ita,
       "ne843TrapIvp1If": ne843TrapIvp1If,
       "ne843TrapIvp1Ilv": ne843TrapIvp1Ilv,
       "ne843TrapIvp1Ifa": ne843TrapIvp1Ifa,
       "ne843TrapIvp1Ihv": ne843TrapIvp1Ihv,
       "ne843TrapIvp1Ida": ne843TrapIvp1Ida,
       "ne843TrapIvp1Iof": ne843TrapIvp1Iof,
       "ne843TrapIvp1Idid": ne843TrapIvp1Idid,
       "ne843TrapIvp1Iirm": ne843TrapIvp1Iirm,
       "ne843TrapIvp1Iipk": ne843TrapIvp1Iipk,
       "ne843TrapIvp1Icf": ne843TrapIvp1Icf,
       "ne843TrapIvp1Mif": ne843TrapIvp1Mif,
       "ne843TrapIvp1Irls": ne843TrapIvp1Irls,
       "ne843TrapDc1Pmf": ne843TrapDc1Pmf,
       "ne843TrapPs1Crt": ne843TrapPs1Crt,
       "ne843TrapIvp1Milv": ne843TrapIvp1Milv,
       "ne843TrapDc1Faja": ne843TrapDc1Faja,
       "ne843TrapDc1Buht": ne843TrapDc1Buht,
       "ne843TrapDc1Buvht": ne843TrapDc1Buvht,
       "ne843TrapDc1Btha": ne843TrapDc1Btha,
       "ne843TrapDc1Btvh": ne843TrapDc1Btvh,
       "ne843TrapDc1Btla": ne843TrapDc1Btla,
       "ne843TrapDc1Btvl": ne843TrapDc1Btvl,
       "ne843TrapDc1Laht": ne843TrapDc1Laht,
       "ne843TrapDc1Lalt": ne843TrapDc1Lalt,
       "ne843TrapDc1Raht": ne843TrapDc1Raht,
       "ne843TrapDc1Ravht": ne843TrapDc1Ravht,
       "ne843TrapDc1Ralt": ne843TrapDc1Ralt,
       "ne843TrapDc1Vlva": ne843TrapDc1Vlva,
       "ne843TrapDc1Vlvb": ne843TrapDc1Vlvb,
       "ne843TrapDc1Ovla": ne843TrapDc1Ovla,
       "ne843TrapDc1Ovlb": ne843TrapDc1Ovlb,
       "ne843TrapDc1Pcaux": ne843TrapDc1Pcaux,
       "ne843TrapDc1Slot": ne843TrapDc1Slot,
       "ne843TrapDc1Fajb": ne843TrapDc1Fajb,
       "ne843TrapDc1Smw": ne843TrapDc1Smw,
       "ne843TrapDc1Cca": ne843TrapDc1Cca,
       "ne843TrapInfo": ne843TrapInfo,
       "ne843TrapDesc": ne843TrapDesc,
       "ne843TrapSev": ne843TrapSev,
       "ne843TrapTime": ne843TrapTime,
       "ne843TrapDate": ne843TrapDate,
       "ne843TrapPath": ne843TrapPath,
       "ne843Retire": ne843Retire,
       "ne843RetireDc1Amj": ne843RetireDc1Amj,
       "ne843RetireDc1Vsf": ne843RetireDc1Vsf,
       "ne843RetireDc1Osa": ne843RetireDc1Osa,
       "ne843RetireDc1Zid": ne843RetireDc1Zid,
       "ne843RetireDc1Tpa": ne843RetireDc1Tpa,
       "ne843RetireDc1Vmf": ne843RetireDc1Vmf,
       "ne843RetireDc1Cma": ne843RetireDc1Cma,
       "ne843RetireDc1Mcm": ne843RetireDc1Mcm,
       "ne843RetireDc1Epo": ne843RetireDc1Epo,
       "ne843RetireDc1Icr": ne843RetireDc1Icr,
       "ne843RetireDc1Rfa": ne843RetireDc1Rfa,
       "ne843RetireDc1Acf": ne843RetireDc1Acf,
       "ne843RetireDc1Man": ne843RetireDc1Man,
       "ne843RetireDc1Did": ne843RetireDc1Did,
       "ne843RetireDc1Clm": ne843RetireDc1Clm,
       "ne843RetireDc1Rfn": ne843RetireDc1Rfn,
       "ne843RetireDc1Vla": ne843RetireDc1Vla,
       "ne843RetireDc1Mfa": ne843RetireDc1Mfa,
       "ne843RetireDc1Rtl": ne843RetireDc1Rtl,
       "ne843RetireDc1Rrtl": ne843RetireDc1Rrtl,
       "ne843RetireDc1Rls": ne843RetireDc1Rls,
       "ne843RetireDc1Mman": ne843RetireDc1Mman,
       "ne843RetireDc1Macf": ne843RetireDc1Macf,
       "ne843RetireDc1Bda": ne843RetireDc1Bda,
       "ne843RetireDc1Hva": ne843RetireDc1Hva,
       "ne843RetireDc1Hfv": ne843RetireDc1Hfv,
       "ne843RetirePs1Epr": ne843RetirePs1Epr,
       "ne843RetirePs1Pfd": ne843RetirePs1Pfd,
       "ne843RetirePs1Exl": ne843RetirePs1Exl,
       "ne843RetirePs1Bbl": ne843RetirePs1Bbl,
       "ne843RetirePs1Clc": ne843RetirePs1Clc,
       "ne843RetirePs1Stf": ne843RetirePs1Stf,
       "ne843RetirePs1Pgi": ne843RetirePs1Pgi,
       "ne843RetirePs1Cch": ne843RetirePs1Cch,
       "ne843RetirePs1Hcl": ne843RetirePs1Hcl,
       "ne843RetirePs1Ax1": ne843RetirePs1Ax1,
       "ne843RetirePs1Ax2": ne843RetirePs1Ax2,
       "ne843RetirePs1Ax3": ne843RetirePs1Ax3,
       "ne843RetirePs1Ax4": ne843RetirePs1Ax4,
       "ne843RetirePs1Ax5": ne843RetirePs1Ax5,
       "ne843RetirePs1Ax6": ne843RetirePs1Ax6,
       "ne843RetirePs1Fan24": ne843RetirePs1Fan24,
       "ne843RetirePs1Fan48": ne843RetirePs1Fan48,
       "ne843RetirePs1Faj24": ne843RetirePs1Faj24,
       "ne843RetirePs1Faj48": ne843RetirePs1Faj48,
       "ne843RetireAt1Ata": ne843RetireAt1Ata,
       "ne843RetireAt1Atb": ne843RetireAt1Atb,
       "ne843RetireCp1Cfa": ne843RetireCp1Cfa,
       "ne843RetireCp1Cfn": ne843RetireCp1Cfn,
       "ne843RetireCp1Cfj": ne843RetireCp1Cfj,
       "ne843RetireCp1Dfa": ne843RetireCp1Dfa,
       "ne843RetireCp1Did": ne843RetireCp1Did,
       "ne843RetireCp1Icc": ne843RetireCp1Icc,
       "ne843RetireCp1Mfa": ne843RetireCp1Mfa,
       "ne843RetireCp1Hva": ne843RetireCp1Hva,
       "ne843RetireCp1Hfv": ne843RetireCp1Hfv,
       "ne843RetireCp1Vla": ne843RetireCp1Vla,
       "ne843RetireCp1Rl": ne843RetireCp1Rl,
       "ne843RetireBr1Bta": ne843RetireBr1Bta,
       "ne843RetireBr1Bfa": ne843RetireBr1Bfa,
       "ne843RetireBr1Scda": ne843RetireBr1Scda,
       "ne843RetireBr1Isda": ne843RetireBr1Isda,
       "ne843RetireBr1Mdp": ne843RetireBr1Mdp,
       "ne843RetireBr1Mzd": ne843RetireBr1Mzd,
       "ne843RetireBr1Btha": ne843RetireBr1Btha,
       "ne843RetireCn1Cno": ne843RetireCn1Cno,
       "ne843RetireCn1Cnf": ne843RetireCn1Cnf,
       "ne843RetireCn2Cno": ne843RetireCn2Cno,
       "ne843RetireCn2Cnf": ne843RetireCn2Cnf,
       "ne843RetireCn3Cno": ne843RetireCn3Cno,
       "ne843RetireCn3Cnf": ne843RetireCn3Cnf,
       "ne843RetireCn4Cno": ne843RetireCn4Cno,
       "ne843RetireCn4Cnf": ne843RetireCn4Cnf,
       "ne843RetireCm1Cof": ne843RetireCm1Cof,
       "ne843RetireCm1Cor": ne843RetireCm1Cor,
       "ne843RetireCm1Nnc": ne843RetireCm1Nnc,
       "ne843RetirePo1Por": ne843RetirePo1Por,
       "ne843RetireRp1Rf": ne843RetireRp1Rf,
       "ne843RetireRp1Rpff": ne843RetireRp1Rpff,
       "ne843RetireRp1Rprl": ne843RetireRp1Rprl,
       "ne843RetireRp1Rpfj": ne843RetireRp1Rpfj,
       "ne843RetireRp1Rpxj": ne843RetireRp1Rpxj,
       "ne843RetireRp1Rpxn": ne843RetireRp1Rpxn,
       "ne843RetireRp1Rcdp": ne843RetireRp1Rcdp,
       "ne843RetireUserDefined": ne843RetireUserDefined,
       "ne843RetireDc1Emd": ne843RetireDc1Emd,
       "ne843RetireDc1Pfs": ne843RetireDc1Pfs,
       "ne843RetireDc1Rif": ne843RetireDc1Rif,
       "ne843RetireDc1Lsf": ne843RetireDc1Lsf,
       "ne843RetirePs1Ax7": ne843RetirePs1Ax7,
       "ne843RetirePs1Ax8": ne843RetirePs1Ax8,
       "ne843RetirePs1Ax9": ne843RetirePs1Ax9,
       "ne843RetirePs1Ax10": ne843RetirePs1Ax10,
       "ne843RetirePs1Ax11": ne843RetirePs1Ax11,
       "ne843RetirePs1Ax12": ne843RetirePs1Ax12,
       "ne843RetireBr1Btla": ne843RetireBr1Btla,
       "ne843RetireBr1Btvh": ne843RetireBr1Btvh,
       "ne843RetireBr1Btvl": ne843RetireBr1Btvl,
       "ne843RetireGn1Gnr": ne843RetireGn1Gnr,
       "ne843RetireGn1Gnm": ne843RetireGn1Gnm,
       "ne843RetireGn1Gnf": ne843RetireGn1Gnf,
       "ne843RetirePs1Amtl": ne843RetirePs1Amtl,
       "ne843RetirePs1Amth": ne843RetirePs1Amth,
       "ne843RetireAco1Aac": ne843RetireAco1Aac,
       "ne843RetireBr1Rba": ne843RetireBr1Rba,
       "ne843RetireCp1Cin": ne843RetireCp1Cin,
       "ne843RetireDc1Bof": ne843RetireDc1Bof,
       "ne843RetireDc1Sof": ne843RetireDc1Sof,
       "ne843RetireDc1Der": ne843RetireDc1Der,
       "ne843RetireGn1Gns": ne843RetireGn1Gns,
       "ne843RetireIvp1Ilvi": ne843RetireIvp1Ilvi,
       "ne843RetireIvp1Ihvi": ne843RetireIvp1Ihvi,
       "ne843RetireIvp1Ita": ne843RetireIvp1Ita,
       "ne843RetireIvp1If": ne843RetireIvp1If,
       "ne843RetireIvp1Ilv": ne843RetireIvp1Ilv,
       "ne843RetireIvp1Ifa": ne843RetireIvp1Ifa,
       "ne843RetireIvp1Ihv": ne843RetireIvp1Ihv,
       "ne843RetireIvp1Ida": ne843RetireIvp1Ida,
       "ne843RetireIvp1Iof": ne843RetireIvp1Iof,
       "ne843RetireIvp1Idid": ne843RetireIvp1Idid,
       "ne843RetireIvp1Iirm": ne843RetireIvp1Iirm,
       "ne843RetireIvp1Iipk": ne843RetireIvp1Iipk,
       "ne843RetireIvp1Icf": ne843RetireIvp1Icf,
       "ne843RetireIvp1Mif": ne843RetireIvp1Mif,
       "ne843RetireIvp1Irls": ne843RetireIvp1Irls,
       "ne843RetireDc1Pmf": ne843RetireDc1Pmf,
       "ne843RetirePs1Crt": ne843RetirePs1Crt,
       "ne843RetireIvp1Milv": ne843RetireIvp1Milv,
       "ne843RetireDc1Faja": ne843RetireDc1Faja,
       "ne843RetireDc1Buht": ne843RetireDc1Buht,
       "ne843RetireDc1Buvht": ne843RetireDc1Buvht,
       "ne843RetireDc1Btha": ne843RetireDc1Btha,
       "ne843RetireDc1Btvh": ne843RetireDc1Btvh,
       "ne843RetireDc1Btla": ne843RetireDc1Btla,
       "ne843RetireDc1Btvl": ne843RetireDc1Btvl,
       "ne843RetireDc1Laht": ne843RetireDc1Laht,
       "ne843RetireDc1Lalt": ne843RetireDc1Lalt,
       "ne843RetireDc1Raht": ne843RetireDc1Raht,
       "ne843RetireDc1Ravht": ne843RetireDc1Ravht,
       "ne843RetireDc1Ralt": ne843RetireDc1Ralt,
       "ne843RetireDc1Vlva": ne843RetireDc1Vlva,
       "ne843RetireDc1Vlvb": ne843RetireDc1Vlvb,
       "ne843RetireDc1Ovla": ne843RetireDc1Ovla,
       "ne843RetireDc1Ovlb": ne843RetireDc1Ovlb,
       "ne843RetireDc1Pcaux": ne843RetireDc1Pcaux,
       "ne843RetireDc1Slot": ne843RetireDc1Slot,
       "ne843RetireDc1Fajb": ne843RetireDc1Fajb,
       "ne843RetireDc1Smw": ne843RetireDc1Smw,
       "ne843RetireDc1Cca": ne843RetireDc1Cca,
       "ne843Acd1": ne843Acd1,
       "ne843Acd1Ide": ne843Acd1Ide,
       "ne843Acd1Des": ne843Acd1Des,
       "ne843Acd1Brc": ne843Acd1Brc,
       "ne843Acd1Sn": ne843Acd1Sn,
       "ne843Acd1Prd": ne843Acd1Prd,
       "ne843Acd1Psd": ne843Acd1Psd,
       "ne843Acd1Ptd": ne843Acd1Ptd,
       "ne843Acd1Prv": ne843Acd1Prv,
       "ne843Acd1Psv": ne843Acd1Psv,
       "ne843Acd1Ptv": ne843Acd1Ptv,
       "ne843Acd1Pra": ne843Acd1Pra,
       "ne843Acd1Psa": ne843Acd1Psa,
       "ne843Acd1Pta": ne843Acd1Pta,
       "ne843Acd1Prf": ne843Acd1Prf,
       "ne843Acd1Psf": ne843Acd1Psf,
       "ne843Acd1Ptf": ne843Acd1Ptf,
       "ne843Acd1Prk": ne843Acd1Prk,
       "ne843Acd1Psk": ne843Acd1Psk,
       "ne843Acd1Ptk": ne843Acd1Ptk,
       "ne843Acd1Syk": ne843Acd1Syk,
       "ne843Acd1Prx": ne843Acd1Prx,
       "ne843Acd1Psx": ne843Acd1Psx,
       "ne843Acd1Ptx": ne843Acd1Ptx,
       "ne843Gn1": ne843Gn1,
       "ne843Gn1Ide": ne843Gn1Ide,
       "ne843Gn1Des": ne843Gn1Des,
       "ne843Gn1Rt": ne843Gn1Rt,
       "ne843Gn1Trt": ne843Gn1Trt,
       "ne843Gn1Gnr": ne843Gn1Gnr,
       "ne843Gn1Gnm": ne843Gn1Gnm,
       "ne843Gn1Gnf": ne843Gn1Gnf,
       "ne843Gn1Clt": ne843Gn1Clt,
       "ne843Gn1Tv": ne843Gn1Tv,
       "ne843Gn1Tvd": ne843Gn1Tvd,
       "ne843Gn1Tp": ne843Gn1Tp,
       "ne843Gn1Tpd": ne843Gn1Tpd,
       "ne843Gn1Tct": ne843Gn1Tct,
       "ne843Gn1Tctd": ne843Gn1Tctd,
       "ne843Gn1Tht": ne843Gn1Tht,
       "ne843Gn1Thtd": ne843Gn1Thtd,
       "ne843Gn1Pv": ne843Gn1Pv,
       "ne843Gn1Pvd": ne843Gn1Pvd,
       "ne843Gn1Pi": ne843Gn1Pi,
       "ne843Gn1Pid": ne843Gn1Pid,
       "ne843Gn1Pp": ne843Gn1Pp,
       "ne843Gn1Ppd": ne843Gn1Ppd,
       "ne843Gn1Pct": ne843Gn1Pct,
       "ne843Gn1Pctd": ne843Gn1Pctd,
       "ne843Gn1Pht": ne843Gn1Pht,
       "ne843Gn1Phtd": ne843Gn1Phtd,
       "ne843Gn1Mrt": ne843Gn1Mrt,
       "ne843Gn1Tve": ne843Gn1Tve,
       "ne843Gn1Tpe": ne843Gn1Tpe,
       "ne843Gn1Cte": ne843Gn1Cte,
       "ne843Gn1Hte": ne843Gn1Hte,
       "ne843Gn1Pve": ne843Gn1Pve,
       "ne843Gn1Pie": ne843Gn1Pie,
       "ne843Gn1Ppe": ne843Gn1Ppe,
       "ne843Gn1Nv": ne843Gn1Nv,
       "ne843Gn1Nva": ne843Gn1Nva,
       "ne843Gn1Ode": ne843Gn1Ode,
       "ne843Gn1Odr": ne843Gn1Odr,
       "ne843Gn1Ocd": ne843Gn1Ocd,
       "ne843Gn1Gns": ne843Gn1Gns,
       "ne843Gn1Aue": ne843Gn1Aue,
       "ne843Gn1Mod": ne843Gn1Mod,
       "ne843Gn1Stt": ne843Gn1Stt,
       "ne843BatTable": ne843BatTable,
       "ne843BatEntry": ne843BatEntry,
       "ne843BatEntryIndex": ne843BatEntryIndex,
       "ne843BatEntryIde": ne843BatEntryIde,
       "ne843BatEntryDes": ne843BatEntryDes,
       "ne843BatEntryCon": ne843BatEntryCon,
       "ne843BatEntryStt": ne843BatEntryStt,
       "ne843BatEntryNst": ne843BatEntryNst,
       "ne843BatEntryBty": ne843BatEntryBty,
       "ne843BatEntryCap": ne843BatEntryCap,
       "ne843BatEntryDat": ne843BatEntryDat,
       "ne843BatEntryMpv": ne843BatEntryMpv,
       "ne843BatEntryAdc": ne843BatEntryAdc,
       "ne843Eco1": ne843Eco1,
       "ne843Eco1Ide": ne843Eco1Ide,
       "ne843Eco1Des": ne843Eco1Des,
       "ne843Eco1Sofs": ne843Eco1Sofs,
       "ne843Eco1Ntrd": ne843Eco1Ntrd,
       "ne843Eco1Strd": ne843Eco1Strd,
       "ne843Eco1Nkwh": ne843Eco1Nkwh,
       "ne843Eco1Skwh": ne843Eco1Skwh,
       "ne843Eco1Ncap": ne843Eco1Ncap,
       "ne843Eco1Nocap": ne843Eco1Nocap,
       "ne843Ivp1": ne843Ivp1,
       "ne843Ivp1Ide": ne843Ivp1Ide,
       "ne843Ivp1Des": ne843Ivp1Des,
       "ne843Ivp1Cap": ne843Ivp1Cap,
       "ne843Ivp1Irm": ne843Ivp1Irm,
       "ne843Ivp1Vac": ne843Ivp1Vac,
       "ne843Ivp1Adc": ne843Ivp1Adc,
       "ne843Ivp1Vdc": ne843Ivp1Vdc,
       "ne843Ivp1Frq": ne843Ivp1Frq,
       "ne843Ivp1Lst": ne843Ivp1Lst,
       "ne843Ivp1Ste": ne843Ivp1Ste,
       "ne843Ivp1Rlse": ne843Ivp1Rlse,
       "ne843Ivp1Dth": ne843Ivp1Dth,
       "ne843Ivp1Rth": ne843Ivp1Rth,
       "ne843Ivp1Lvd": ne843Ivp1Lvd,
       "ne843Ivp1Hce": ne843Ivp1Hce,
       "ne843Ivp1Hipe": ne843Ivp1Hipe,
       "ne843Ivp1Hrme": ne843Ivp1Hrme,
       "ne843Ivp1Ilvi": ne843Ivp1Ilvi,
       "ne843Ivp1Ihvi": ne843Ivp1Ihvi,
       "ne843Ivp1Ita": ne843Ivp1Ita,
       "ne843Ivp1If": ne843Ivp1If,
       "ne843Ivp1Ilv": ne843Ivp1Ilv,
       "ne843Ivp1Ifa": ne843Ivp1Ifa,
       "ne843Ivp1Ihv": ne843Ivp1Ihv,
       "ne843Ivp1Ida": ne843Ivp1Ida,
       "ne843Ivp1Iof": ne843Ivp1Iof,
       "ne843Ivp1Idid": ne843Ivp1Idid,
       "ne843Ivp1Iirm": ne843Ivp1Iirm,
       "ne843Ivp1Iipk": ne843Ivp1Iipk,
       "ne843Ivp1Icf": ne843Ivp1Icf,
       "ne843Ivp1Mif": ne843Ivp1Mif,
       "ne843Ivp1Irls": ne843Ivp1Irls,
       "ne843Ivp1Milv": ne843Ivp1Milv,
       "ne843InvTable": ne843InvTable,
       "ne843InvEntry": ne843InvEntry,
       "ne843InvEntryIndex": ne843InvEntryIndex,
       "ne843InvEntryIde": ne843InvEntryIde,
       "ne843InvEntryDes": ne843InvEntryDes,
       "ne843InvEntryTyp": ne843InvEntryTyp,
       "ne843InvEntrySn": ne843InvEntrySn,
       "ne843InvEntryAdc": ne843InvEntryAdc,
       "ne843InvEntryVdc": ne843InvEntryVdc,
       "ne843InvEntryVac": ne843InvEntryVac,
       "ne843InvEntryStt": ne843InvEntryStt,
       "ne843InvEntryCap": ne843InvEntryCap,
       "ne843InvEntryCva": ne843InvEntryCva,
       "ne843InvEntryIpk": ne843InvEntryIpk,
       "ne843InvEntryIrm": ne843InvEntryIrm,
       "ne843InvEntryFrq": ne843InvEntryFrq,
       "ne843InvEntryCf": ne843InvEntryCf,
       "ne843InvEntryPwr": ne843InvEntryPwr,
       "ne843InvEntryVnom": ne843InvEntryVnom,
       "ne843InvEntryNcl": ne843InvEntryNcl,
       "ne843InvEntryIlvi": ne843InvEntryIlvi,
       "ne843InvEntryIta": ne843InvEntryIta,
       "ne843InvEntryIf": ne843InvEntryIf,
       "ne843InvEntryIlv": ne843InvEntryIlv,
       "ne843InvEntryIfa": ne843InvEntryIfa,
       "ne843InvEntryDid": ne843InvEntryDid,
       "ne843InvEntryIcmf": ne843InvEntryIcmf,
       "ne843InvEntryIcf": ne843InvEntryIcf,
       "ne843InvEntryIda": ne843InvEntryIda,
       "ne843InvEntryIhv": ne843InvEntryIhv,
       "ne843InvEntryIhvi": ne843InvEntryIhvi,
       "ne843InvEntryIipk": ne843InvEntryIipk,
       "ne843InvEntryIirm": ne843InvEntryIirm,
       "ne843InvEntryIof": ne843InvEntryIof,
       "ne843InvEntryIlvi1": ne843InvEntryIlvi1,
       "ne843InvEntryIta1": ne843InvEntryIta1,
       "ne843InvEntryIf1": ne843InvEntryIf1,
       "ne843InvEntryIlv1": ne843InvEntryIlv1,
       "ne843InvEntryIfa1": ne843InvEntryIfa1,
       "ne843InvEntryDid1": ne843InvEntryDid1,
       "ne843InvEntryIcmf1": ne843InvEntryIcmf1,
       "ne843InvEntryIcf1": ne843InvEntryIcf1,
       "ne843InvEntryIda1": ne843InvEntryIda1,
       "ne843InvEntryIhv1": ne843InvEntryIhv1,
       "ne843InvEntryIhvi1": ne843InvEntryIhvi1,
       "ne843InvEntryIipk1": ne843InvEntryIipk1,
       "ne843InvEntryIirm1": ne843InvEntryIirm1,
       "ne843InvEntryIof1": ne843InvEntryIof1,
       "ne843Rpt1": ne843Rpt1,
       "ne843Rpt1Ide": ne843Rpt1Ide,
       "ne843Rpt1Des": ne843Rpt1Des,
       "ne843Rpt1Ena": ne843Rpt1Ena,
       "ne843Rpt1Int": ne843Rpt1Int,
       "ne843Rpt1D001": ne843Rpt1D001,
       "ne843Rpt1D002": ne843Rpt1D002,
       "ne843Rpt1D003": ne843Rpt1D003,
       "ne843Rpt1D004": ne843Rpt1D004,
       "ne843Rpt1D005": ne843Rpt1D005,
       "ne843Rpt1D006": ne843Rpt1D006,
       "ne843Rpt1D007": ne843Rpt1D007,
       "ne843Rpt1D008": ne843Rpt1D008,
       "ne843Rpt1D009": ne843Rpt1D009,
       "ne843Rpt1D010": ne843Rpt1D010,
       "ne843Rpt1D011": ne843Rpt1D011,
       "ne843Rpt1D012": ne843Rpt1D012,
       "ne843Rpt1D013": ne843Rpt1D013,
       "ne843Rpt1D014": ne843Rpt1D014,
       "ne843Rpt1D015": ne843Rpt1D015,
       "ne843Rpt1D016": ne843Rpt1D016,
       "ne843Rpt1D017": ne843Rpt1D017,
       "ne843Rpt1D018": ne843Rpt1D018,
       "ne843Rpt1D019": ne843Rpt1D019,
       "ne843Rpt1D020": ne843Rpt1D020,
       "ne843Rpt1D021": ne843Rpt1D021,
       "ne843Rpt1D022": ne843Rpt1D022,
       "ne843Rpt1D023": ne843Rpt1D023,
       "ne843Rpt1D024": ne843Rpt1D024,
       "ne843Rpt1D025": ne843Rpt1D025,
       "ne843Rpt1D026": ne843Rpt1D026,
       "ne843Rpt1D027": ne843Rpt1D027,
       "ne843Rpt1D028": ne843Rpt1D028,
       "ne843Rpt1D029": ne843Rpt1D029,
       "ne843Rpt1D030": ne843Rpt1D030,
       "ne843Rpt1D031": ne843Rpt1D031,
       "ne843Rpt1D032": ne843Rpt1D032,
       "ne843Rpt1D033": ne843Rpt1D033,
       "ne843Rpt1D034": ne843Rpt1D034,
       "ne843Rpt1D035": ne843Rpt1D035,
       "ne843Rpt1D036": ne843Rpt1D036,
       "ne843Rpt1D037": ne843Rpt1D037,
       "ne843Rpt1D038": ne843Rpt1D038,
       "ne843Rpt1D039": ne843Rpt1D039,
       "ne843Rpt1D040": ne843Rpt1D040,
       "ne843Rpt1D041": ne843Rpt1D041,
       "ne843Rpt1D042": ne843Rpt1D042,
       "ne843Rpt1D043": ne843Rpt1D043,
       "ne843Rpt1D044": ne843Rpt1D044,
       "ne843Rpt1D045": ne843Rpt1D045,
       "ne843Rpt1D046": ne843Rpt1D046,
       "ne843Rpt1D047": ne843Rpt1D047,
       "ne843Rpt1D048": ne843Rpt1D048,
       "ne843Rpt1D049": ne843Rpt1D049,
       "ne843Rpt1D050": ne843Rpt1D050,
       "ne843Rpt1D051": ne843Rpt1D051,
       "ne843Rpt1D052": ne843Rpt1D052,
       "ne843Rpt1D053": ne843Rpt1D053,
       "ne843Rpt1D054": ne843Rpt1D054,
       "ne843Rpt1D055": ne843Rpt1D055,
       "ne843Rpt1D056": ne843Rpt1D056,
       "ne843Rpt1D057": ne843Rpt1D057,
       "ne843Rpt1D058": ne843Rpt1D058,
       "ne843Rpt1D059": ne843Rpt1D059,
       "ne843Rpt1D060": ne843Rpt1D060,
       "ne843Rpt1D061": ne843Rpt1D061,
       "ne843Rpt1D062": ne843Rpt1D062,
       "ne843Rpt1D063": ne843Rpt1D063,
       "ne843Rpt1D064": ne843Rpt1D064,
       "ne843Rpt1D065": ne843Rpt1D065,
       "ne843Rpt1D066": ne843Rpt1D066,
       "ne843Rpt1D067": ne843Rpt1D067,
       "ne843Rpt1D068": ne843Rpt1D068,
       "ne843Rpt1D069": ne843Rpt1D069,
       "ne843Rpt1D070": ne843Rpt1D070,
       "ne843Rpt1D071": ne843Rpt1D071,
       "ne843Rpt1D072": ne843Rpt1D072,
       "ne843Rpt1D073": ne843Rpt1D073,
       "ne843Rpt1D074": ne843Rpt1D074,
       "ne843Rpt1D075": ne843Rpt1D075,
       "ne843Rpt1D076": ne843Rpt1D076,
       "ne843Rpt1D077": ne843Rpt1D077,
       "ne843Rpt1D078": ne843Rpt1D078,
       "ne843Rpt1D079": ne843Rpt1D079,
       "ne843Rpt1D080": ne843Rpt1D080,
       "ne843Rpt1D081": ne843Rpt1D081,
       "ne843Rpt1D082": ne843Rpt1D082,
       "ne843Rpt1D083": ne843Rpt1D083,
       "ne843Rpt1D084": ne843Rpt1D084,
       "ne843Rpt1D085": ne843Rpt1D085,
       "ne843Rpt1D086": ne843Rpt1D086,
       "ne843Rpt1D087": ne843Rpt1D087,
       "ne843Rpt1D088": ne843Rpt1D088,
       "ne843Rpt1D089": ne843Rpt1D089,
       "ne843Rpt1D090": ne843Rpt1D090,
       "ne843Rpt1D091": ne843Rpt1D091,
       "ne843Rpt1D092": ne843Rpt1D092,
       "ne843Rpt1D093": ne843Rpt1D093,
       "ne843Rpt1D094": ne843Rpt1D094,
       "ne843Rpt1D095": ne843Rpt1D095,
       "ne843Rpt1D096": ne843Rpt1D096,
       "ne843Rpt1D097": ne843Rpt1D097,
       "ne843Rpt1D098": ne843Rpt1D098,
       "ne843Rpt1D099": ne843Rpt1D099,
       "ne843Rpt1D100": ne843Rpt1D100,
       "ne843Rpt1D101": ne843Rpt1D101,
       "ne843Rpt1D102": ne843Rpt1D102,
       "ne843Rpt1D103": ne843Rpt1D103,
       "ne843Rpt1D104": ne843Rpt1D104,
       "ne843Rpt1D105": ne843Rpt1D105,
       "ne843Rpt1D106": ne843Rpt1D106,
       "ne843Rpt1D107": ne843Rpt1D107,
       "ne843Rpt1D108": ne843Rpt1D108,
       "ne843Rpt1D109": ne843Rpt1D109,
       "ne843Rpt1D110": ne843Rpt1D110,
       "ne843Rpt1D111": ne843Rpt1D111,
       "ne843Rpt1D112": ne843Rpt1D112,
       "ne843Rpt1D113": ne843Rpt1D113,
       "ne843Rpt1D114": ne843Rpt1D114,
       "ne843Rpt1D115": ne843Rpt1D115,
       "ne843Rpt1D116": ne843Rpt1D116,
       "ne843Rpt1D117": ne843Rpt1D117,
       "ne843Rpt1D118": ne843Rpt1D118,
       "ne843Rpt1D119": ne843Rpt1D119,
       "ne843Rpt1D120": ne843Rpt1D120,
       "ne843Rpt1D121": ne843Rpt1D121,
       "ne843Rpt1D122": ne843Rpt1D122,
       "ne843Rpt1D123": ne843Rpt1D123,
       "ne843Rpt1D124": ne843Rpt1D124,
       "ne843Rpt1D125": ne843Rpt1D125,
       "ne843Rpt1D126": ne843Rpt1D126,
       "ne843Rpt1D127": ne843Rpt1D127,
       "ne843Rpt1D128": ne843Rpt1D128,
       "ne843Rpt1D129": ne843Rpt1D129,
       "ne843Rpt1D130": ne843Rpt1D130,
       "ne843Rpt1D131": ne843Rpt1D131,
       "ne843Rpt1D132": ne843Rpt1D132,
       "ne843Rpt1D133": ne843Rpt1D133,
       "ne843Rpt1D134": ne843Rpt1D134,
       "ne843Rpt1D135": ne843Rpt1D135,
       "ne843Rpt1D136": ne843Rpt1D136,
       "ne843Rpt1D137": ne843Rpt1D137,
       "ne843Rpt1D138": ne843Rpt1D138,
       "ne843Rpt1D139": ne843Rpt1D139,
       "ne843Rpt1D140": ne843Rpt1D140,
       "ne843Rpt1D141": ne843Rpt1D141,
       "ne843Rpt1D142": ne843Rpt1D142,
       "ne843Rpt1D143": ne843Rpt1D143,
       "ne843Rpt1D144": ne843Rpt1D144,
       "ne843Rpt1D145": ne843Rpt1D145,
       "ne843Rpt1D146": ne843Rpt1D146,
       "ne843Rpt1D147": ne843Rpt1D147,
       "ne843Rpt1D148": ne843Rpt1D148,
       "ne843Rpt1D149": ne843Rpt1D149,
       "ne843Rpt1D150": ne843Rpt1D150,
       "ne843PicTable": ne843PicTable,
       "ne843PicEntry": ne843PicEntry,
       "ne843PicEntryIndex": ne843PicEntryIndex,
       "ne843PicEntryIde": ne843PicEntryIde,
       "ne843PicEntryDes": ne843PicEntryDes,
       "ne843PicEntrySn": ne843PicEntrySn,
       "ne843PicEntryCc": ne843PicEntryCc,
       "ne843PicEntrySer": ne843PicEntrySer,
       "ne843PicEntryClei": ne843PicEntryClei,
       "ne843PicEntryCustpn2": ne843PicEntryCustpn2,
       "ne843PicEntryAsstag2": ne843PicEntryAsstag2,
       "ne843PicEntryStt": ne843PicEntryStt,
       "ne843PicEntryTyp": ne843PicEntryTyp,
       "ne843PicEntryNst": ne843PicEntryNst,
       "ne843PicEntryNvt": ne843PicEntryNvt,
       "ne843PicEntryVera": ne843PicEntryVera,
       "ne843PicEntryPid": ne843PicEntryPid,
       "ne843PicEntryPcf": ne843PicEntryPcf,
       "ne843PicEntryNumslot": ne843PicEntryNumslot,
       "ne843PicEntryCbf": ne843PicEntryCbf,
       "ne843PicEntryFajae": ne843PicEntryFajae,
       "ne843PicEntryFajrly": ne843PicEntryFajrly,
       "ne843PicEntryOsae": ne843PicEntryOsae,
       "ne843PicEntryOsarly": ne843PicEntryOsarly,
       "ne843PicEntryTmpe": ne843PicEntryTmpe,
       "ne843PicEntryTmprly": ne843PicEntryTmprly,
       "ne843PicEntryVlvs": ne843PicEntryVlvs,
       "ne843PicEntryVlvlat": ne843PicEntryVlvlat,
       "ne843PicEntryVlvae": ne843PicEntryVlvae,
       "ne843PicEntryVlvath": ne843PicEntryVlvath,
       "ne843PicEntryVlvbe": ne843PicEntryVlvbe,
       "ne843PicEntryVlvbth": ne843PicEntryVlvbth,
       "ne843PicEntryVlvrly": ne843PicEntryVlvrly,
       "ne843PicEntryOvls": ne843PicEntryOvls,
       "ne843PicEntryOlvlat": ne843PicEntryOlvlat,
       "ne843PicEntryOvlae": ne843PicEntryOvlae,
       "ne843PicEntryOvlath": ne843PicEntryOvlath,
       "ne843PicEntryOvlbe": ne843PicEntryOvlbe,
       "ne843PicEntryOvlbth": ne843PicEntryOvlbth,
       "ne843PicEntryOvlrly": ne843PicEntryOvlrly,
       "ne843PicEntryEpoe": ne843PicEntryEpoe,
       "ne843PicEntryEporly": ne843PicEntryEporly,
       "ne843PicEntryPcauxe": ne843PicEntryPcauxe,
       "ne843PicEntryPcauxr": ne843PicEntryPcauxr,
       "ne843PicEntrySlote": ne843PicEntrySlote,
       "ne843PicEntrySlotrly": ne843PicEntrySlotrly,
       "ne843PicEntryDpmode": ne843PicEntryDpmode,
       "ne843PicEntryPnldes": ne843PicEntryPnldes,
       "ne843PicEntryMdl": ne843PicEntryMdl,
       "ne843PicEntryPnlsn": ne843PicEntryPnlsn,
       "ne843PicEntryPnlcc": ne843PicEntryPnlcc,
       "ne843PicEntryPnlser": ne843PicEntryPnlser,
       "ne843PicEntryPnlclei": ne843PicEntryPnlclei,
       "ne843PicEntryCustpn1": ne843PicEntryCustpn1,
       "ne843PicEntryAsstag1": ne843PicEntryAsstag1,
       "ne843PicEntryRtng": ne843PicEntryRtng,
       "ne843PicEntryPnlsize": ne843PicEntryPnlsize,
       "ne843PcmTable": ne843PcmTable,
       "ne843PcmEntry": ne843PcmEntry,
       "ne843PcmEntryIndex": ne843PcmEntryIndex,
       "ne843PcmEntryIde": ne843PcmEntryIde,
       "ne843PcmEntryDes": ne843PcmEntryDes,
       "ne843PcmEntryVal": ne843PcmEntryVal,
       "ne843PcmEntrySht": ne843PcmEntrySht,
       "ne843PcmEntrySha": ne843PcmEntrySha,
       "ne843PcmEntryShv": ne843PcmEntryShv,
       "ne843PvmTable": ne843PvmTable,
       "ne843PvmEntry": ne843PvmEntry,
       "ne843PvmEntryIndex": ne843PvmEntryIndex,
       "ne843PvmEntryIde": ne843PvmEntryIde,
       "ne843PvmEntryDes": ne843PvmEntryDes,
       "ne843PvmEntryVal": ne843PvmEntryVal,
       "ne843PtmTable": ne843PtmTable,
       "ne843PtmEntry": ne843PtmEntry,
       "ne843PtmEntryIndex": ne843PtmEntryIndex,
       "ne843PtmEntryIde": ne843PtmEntryIde,
       "ne843PtmEntryDes": ne843PtmEntryDes,
       "ne843PtmEntryBamt": ne843PtmEntryBamt,
       "ne843PtmEntryNat": ne843PtmEntryNat,
       "ne843PtmEntryHamt": ne843PtmEntryHamt,
       "ne843PtmEntryLamt": ne843PtmEntryLamt,
       "ne843PtmEntryNtm": ne843PtmEntryNtm,
       "ne843PtmEntryHbt": ne843PtmEntryHbt,
       "ne843PtmEntryLbt": ne843PtmEntryLbt,
       "ne843PtmEntryNbut": ne843PtmEntryNbut,
       "ne843PtmEntryHbut": ne843PtmEntryHbut,
       "ne843PtmEntryLbut": ne843PtmEntryLbut,
       "ne843PcsTable": ne843PcsTable,
       "ne843PcsEntry": ne843PcsEntry,
       "ne843PcsEntryIndex": ne843PcsEntryIndex,
       "ne843PcsEntryIde": ne843PcsEntryIde,
       "ne843PcsEntryDes": ne843PcsEntryDes,
       "ne843PcsEntryStt": ne843PcsEntryStt,
       "ne843PcsEntryTyp": ne843PcsEntryTyp,
       "ne843PcsEntryPole": ne843PcsEntryPole,
       "ne843PcsEntryPolp": ne843PcsEntryPolp,
       "ne843PcsEntryPopn": ne843PcsEntryPopn,
       "ne843PcsEntryTrp": ne843PcsEntryTrp,
       "ne843PcsEntryBad": ne843PcsEntryBad,
       "ne843PcsEntryCbf": ne843PcsEntryCbf,
       "ne843PcsEntrySlv": ne843PcsEntrySlv,
       "ne843PcsEntryRtng": ne843PcsEntryRtng,
       "ne843DbyTable": ne843DbyTable,
       "ne843DbyEntry": ne843DbyEntry,
       "ne843DbyEntryIndex": ne843DbyEntryIndex,
       "ne843DbyEntryIde": ne843DbyEntryIde,
       "ne843DbyEntryDes": ne843DbyEntryDes,
       "ne843DbyEntrySn": ne843DbyEntrySn,
       "ne843DbyEntryStt": ne843DbyEntryStt,
       "ne843DbyEntrySha": ne843DbyEntrySha,
       "ne843DbyEntryNpl": ne843DbyEntryNpl,
       "ne843DbyEntryPmt": ne843DbyEntryPmt,
       "ne843DbyEntryIds": ne843DbyEntryIds,
       "ne843DbyEntryBze": ne843DbyEntryBze,
       "ne843DbyEntryOle": ne843DbyEntryOle,
       "ne843DbyEntryOri": ne843DbyEntryOri,
       "ne843DbyEntryCmb": ne843DbyEntryCmb,
       "ne843DbyEntrySmw": ne843DbyEntrySmw,
       "ne843DbyEntryCca": ne843DbyEntryCca,
       "ne843DpnTable": ne843DpnTable,
       "ne843DpnEntry": ne843DpnEntry,
       "ne843DpnEntryIndex": ne843DpnEntryIndex,
       "ne843DpnEntryIde": ne843DpnEntryIde,
       "ne843DpnEntryDes": ne843DpnEntryDes,
       "ne843DpnEntryAdc": ne843DpnEntryAdc,
       "ne843DpnEntryVdc": ne843DpnEntryVdc,
       "ne843DpnEntryStt": ne843DpnEntryStt,
       "ne843DpnEntryPid": ne843DpnEntryPid,
       "ne843DpnEntryEna": ne843DpnEntryEna,
       "ne843DpnEntryOld": ne843DpnEntryOld,
       "ne843DpnEntryOlt": ne843DpnEntryOlt,
       "ne843DpnEntryOlr": ne843DpnEntryOlr,
       "ne843DpnEntryPlt": ne843DpnEntryPlt,
       "ne843DpnEntryCct": ne843DpnEntryCct,
       "ne843DpnEntryVlv": ne843DpnEntryVlv,
       "ne843DpnEntryOvl": ne843DpnEntryOvl,
       "ne843DpnEntryFaja": ne843DpnEntryFaja,
       "ne843DpnEntryFajb": ne843DpnEntryFajb,
       "prototypes": prototypes}
)
